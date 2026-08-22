import os
import json
import urllib.request
import urllib.error
import re
import random
from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

SYSTEM_INSTRUCTION = """너는 유치원에서 빨간 미니카를 가지고 놀고 있는 7세 장난꾸러기 남자아이 '지호'야.
대화 상대는 같은 반 또래 친구(발달지연/자폐스펙트럼 아동)야.

[지호의 성격 및 대화 규칙]
1. 7세 아이 말투로 짧게 1~2문장(30자 내외)으로 신나게 또는 뾰루퉁하게 대답해. 절대 어른이나 인공지능처럼 길게 설명하지 마!
2. 상대방이 무조건 반말/명령/공격/욕/짜증을 내면 (예: "야 인마", "놀기 싫어", "내놔", "비켜"):
   - 뾰루퉁하게 거절하거나 삐쳐: "뭐라고? 왜 화내? 그럼 나 혼자 놀 거야 흥!" 또는 "야 인마라니! 너 말 그렇게 하면 안 놀아!"
   - EMOTION: ANGRY, RAPPORT_CHANGE: -15, DEAL_STATUS: 거절 ❌
3. 상대방이 '블록 터널', '가위바위보', '시간 나누기' 등 타협안(Deal)을 제안하면:
   - 아주 신나서 수락해: "우와 진짜? 블록 터널? 대박! 그럼 내가 차 굴려볼게!"
   - EMOTION: HAPPY, RAPPORT_CHANGE: +30, DEAL_STATUS: 딜 성공 🤝
4. 상대방이 놀리면: 쿨하게 무시해 ("그래서 뭐? 짝짝이 양말이 유행이거든~") ➔ [COOL]
5. 상대방이 의심하거나 질문하면: 7살 아이답게 자연스럽게 대답해 ("진짜라니까! 내 차 엄청 빠르거든? 너 뭐 해?") ➔ [CURIOUS]
6. 일반적인 인사나 대화: 7세 아이답게 반갑게 대답해 ➔ [NEUTRAL]

[출력 포맷 (반드시 아래 4줄로 출력)]
EMOTION: [HAPPY / ANGRY / COOL / CURIOUS / NEUTRAL]
RESPONSE: (지호의 실제 7세 대사)
RAPPORT_CHANGE: (+30 / -20 등)
DEAL_STATUS: (결과 요약)"""

class PeerProxyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                req_json = json.loads(post_data.decode('utf-8'))
                user_msg = req_json.get('message', '').strip()
                api_key = req_json.get('apiKey', '').strip()
                history = req_json.get('history', [])

                if not user_msg:
                    self.send_json_response({'error': '메시지가 비어 있습니다.'}, 400)
                    return

                print(f"[USER]: {user_msg} (Key length: {len(api_key)})")

                # If user provided API key, try AI call
                if api_key:
                    if api_key.startswith('sk-') and not api_key.startswith('sk-ant'):
                        res = self.call_openai(api_key, user_msg, history)
                    else:
                        res = self.call_gemini(api_key, user_msg, history)
                else:
                    res = self.dynamic_free_brain(user_msg, history)

                print(f"[JIHO]: {res.get('text')} ({res.get('engine')})")
                self.send_json_response(res)

            except Exception as e:
                print(f"[ERROR]: {str(e)}")
                # Return explicit error so frontend knows, but also provide a dynamic child answer
                fallback = self.dynamic_free_brain(user_msg, history)
                fallback['apiError'] = str(e)
                self.send_json_response(fallback)
        else:
            self.send_error(404, "Endpoint not found")

    def call_gemini(self, api_key, user_msg, history):
        # Format history string
        hist_text = ""
        for h in history[-4:]:
            sender = "친구" if h.get('sender') == 'user' else "지호"
            hist_text += f"{sender}: {h.get('text', '')}\n"

        prompt_payload = f"{SYSTEM_INSTRUCTION}\n\n[이전 대화 기록]:\n{hist_text}\n[친구의 새로운 말]: {user_msg}\n\n[지호의 답변]:"

        models = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-pro']
        last_err = ""

        for m in models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={api_key}"
            
            body = json.dumps({
                "contents": [
                    {
                        "parts": [{"text": prompt_payload}]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 150
                }
            }).encode('utf-8')

            req = urllib.request.Request(
                url,
                data=body,
                headers={'Content-Type': 'application/json'}
            )

            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode('utf-8'))
                        if data.get('candidates') and len(data['candidates']) > 0:
                            raw_text = data['candidates'][0]['content']['parts'][0]['text']
                            return self.parse_structured_output(raw_text, f'Gemini ({m})')
            except urllib.error.HTTPError as e:
                err_content = e.read().decode('utf-8')
                last_err = f"Gemini {m} ({e.code}): {err_content}"
                print(f"HTTPError: {last_err}")
                continue
            except Exception as e:
                last_err = str(e)
                print(f"Error calling {m}: {last_err}")
                continue

        raise Exception(f"Gemini API 호출 실패: {last_err}")

    def call_openai(self, api_key, user_msg, history):
        url = "https://api.openai.com/v1/chat/completions"
        messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}]
        
        for h in history[-4:]:
            r = "user" if h.get('sender') == 'user' else "assistant"
            messages.append({"role": r, "content": h.get('text', '')})
            
        messages.append({"role": "user", "content": user_msg})

        payload = json.dumps({
            "model": "gpt-4o-mini",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 150
        }).encode('utf-8')

        req = urllib.request.Request(url, data=payload, headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        })

        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            raw_text = data['choices'][0]['message']['content']
            return self.parse_structured_output(raw_text, 'OpenAI (gpt-4o-mini)')

    def dynamic_free_brain(self, user_msg, history):
        """Dynamic responsive child persona (never repeats same line)"""
        text = user_msg.lower().strip()

        # 1. 공격 / 화냄 / 짜증 / 욕설 ("야 인마", "내놔", "놀기 싫어", "짜증나", "꺼져")
        if any(w in text for w in ['야 인마', '인마', '놈', '내놔', '뺏', '비켜', '죽을', '싫어', '안 놀', '꺼져', '짜증', '바보']):
            angry_replies = [
                ("야 인마라니! 너 말 그렇게 하면 나 너랑 진짜 안 놀아!", -15, "거절 ❌"),
                ("놀기 싫으면 말아! 나 혼자 자동차 경주할 거야 흥!", -10, "토라짐 😤"),
                ("왜 화를 내? 난 그냥 미니카 굴리고 있었는데!", -10, "방어 🛡️"),
                ("소리 지르지 마! 너랑 안 놀고 블록 쌓으러 갈 거야!", -20, "거절 ❌")
            ]
            reply, rapport, deal = random.choice(angry_replies)
            return {'text': reply, 'emotion': 'ANGRY', 'rapportChange': rapport, 'dealStatus': deal, 'engine': '지능형 아동 두뇌'}

        # 2. 딜 제안 (블록, 터널, 도로, 합치기)
        if any(w in text for w in ['블록', '터널', '도로', '합치', '통과', '같이 만', '딜']):
            happy_replies = [
                ("우와 진짜? 블록으로 터널 만든다고? 대박! 그럼 내가 차 슝- 통과시킬게!", +30, "딜 성공 🤝"),
                ("좋아 좋아! 네가 노란 블록으로 기둥 세워주면 내가 도로 연결할게!", +25, "딜 성공 🤝"),
                ("블록 터널 딜 완전 찬성! 우리 같이 엄청 길게 만들자!", +30, "딜 성공 🤝")
            ]
            reply, rapport, deal = random.choice(happy_replies)
            return {'text': reply, 'emotion': 'HAPPY', 'rapportChange': rapport, 'dealStatus': deal, 'engine': '지능형 아동 두뇌'}

        # 3. 순서 딜 (가위바위보, 순서, 차례)
        if any(w in text for w in ['가위바위보', '순서', '차례', '이긴', '먼저']):
            return {
                'text': "좋아! 가위바위보 하자! 안 내면 진 거 가위 바위 보! 내가 이기면 나 먼저 1판 달린다?",
                'emotion': 'HAPPY',
                'rapportChange': +25,
                'dealStatus': '순서 딜 ✌️',
                'engine': '지능형 아동 두뇌'
            }

        # 4. 의심 / 확인 ("되는 거냐고", "진짜야?", "아닌 거 같은데", "맞아?")
        if any(w in text for w in ['되는', '아닌', '진짜', '거짓', '맞아', '누구', '왜']):
            curious_replies = [
                ("당연히 되지! 나 지금 빨간 미니카 바퀴 굴리고 있는데? 너 뭐 하는데?", +5, "대화 중 💬"),
                ("진짜라니까! 내 차 바퀴에 불도 반짝여! 너도 만져볼래?", +10, "대화 중 💬"),
                ("아니긴 뭐가 아니야~ 나 유치원 햇살반 7살 지호 맞거든?", +5, "대화 중 💬")
            ]
            reply, rapport, deal = random.choice(curious_replies)
            return {'text': reply, 'emotion': 'CURIOUS', 'rapportChange': rapport, 'dealStatus': deal, 'engine': '지능형 아동 두뇌'}

        # 5. 인사 및 일상 질문
        neutral_replies = [
            ("응 안녕! 너 오늘 유치원에 무슨 가방 메고 왔어?", +10, "질문 토스 🏓"),
            ("난 자동차 경주가 제일 재밌어! 너는 공룡 좋아해 아니면 로봇 좋아해?", +10, "질문 토스 🏓"),
            ("우리 오늘 간식으로 핫도그 나온대! 너도 핫도그 좋아해?", +10, "질문 토스 🏓"),
            ("응! 너 심심하면 나랑 저기서 미끄럼틀 탈래?", +15, "대화 중 💬")
        ]
        reply, rapport, deal = random.choice(neutral_replies)
        return {'text': reply, 'emotion': 'NEUTRAL', 'rapportChange': rapport, 'dealStatus': deal, 'engine': '지능형 아동 두뇌'}

    def parse_structured_output(self, raw_text, engine_name):
        emotion = 'NEUTRAL'
        response_text = raw_text
        rapport_delta = 0
        deal_status = '대화 중 💬'

        for line in raw_text.split('\n'):
            line = line.strip()
            if line.startswith('EMOTION:'):
                emotion = line.replace('EMOTION:', '').strip()
            elif line.startswith('RESPONSE:'):
                response_text = line.replace('RESPONSE:', '').strip()
            elif line.startswith('RAPPORT_CHANGE:'):
                try:
                    rapport_delta = int(re.sub(r'[^0-9\-]', '', line.replace('RAPPORT_CHANGE:', '')))
                except:
                    rapport_delta = 0
            elif line.startswith('DEAL_STATUS:'):
                deal_status = line.replace('DEAL_STATUS:', '').strip()

        return {
            'text': response_text,
            'emotion': emotion,
            'rapportChange': rapport_delta,
            'dealStatus': deal_status,
            'engine': engine_name
        }

    def send_json_response(self, data, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), PeerProxyHandler) as httpd:
        print(f"CocoLink Multi-AI Peer Server running on http://localhost:{PORT}")
        httpd.serve_forever()
