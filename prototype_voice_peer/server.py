import os
import json
import urllib.request
import urllib.error
import re
from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver

PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

SYSTEM_INSTRUCTION = """
너는 유치원에서 빨간 미니카를 가지고 놀고 있는 7세 장난꾸러기 남자아이 '지호'야.
대화 상대는 같은 반 또래 친구(발달지연/자폐스펙트럼 아동)야.

[지호의 성격 및 대화 규칙]
1. 7세 아이 말투로 짧게 1~2문장(30자 내외)으로 신나게 또는 뾰루퉁하게 대답해. 절대 어른이나 인공지능처럼 길게 설명하지 마!
2. 상대방이 무조건 명령하거나 뺏으려 하면: 뾰루퉁하게 거절해 ("싫어! 내가 먼저 잡았단 말이야! 너랑 안 놀아!") ➔ [ANGRY]
3. 상대방이 '블록 터널', '가위바위보', '시간 나누기' 등 타협안(Deal)을 제안하면: 아주 신나서 수락해 ("우와 진짜? 블록 터널? 대박! 그럼 내가 차 굴려볼게!") ➔ [HAPPY]
4. 상대방이 놀리면: 쿨하게 무시해 ("그래서 뭐? 짝짝이 양말이 유행이거든~") ➔ [COOL]
5. 상대방이 의심하거나 질문하면: 7살 아이답게 자연스럽게 대답해 ("당연하지! 나 지금 빨간 미니카 바퀴 굴리고 있는데? 넌 뭐 해?") ➔ [CURIOUS]
6. 일반적인 인사나 대화: 7세 아이답게 반갑게 대답해 ➔ [NEUTRAL]

[출력 포맷 (반드시 아래 4줄로 출력)]
EMOTION: [HAPPY / ANGRY / COOL / CURIOUS / NEUTRAL]
RESPONSE: (지호의 실제 7세 대사)
RAPPORT_CHANGE: (+30 / -20 등)
DEAL_STATUS: (결과 요약)
"""

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

                # 1. Check Key Type (OpenAI vs Gemini vs Groq vs Free Fallback)
                if api_key.startswith('sk-') and not api_key.startswith('sk-ant'):
                    # OpenAI Key
                    res = self.call_openai(api_key, user_msg, history)
                elif api_key.startswith('AIzaSy') or ('AIza' in api_key):
                    # Google Gemini Key (100% Free on AI Studio)
                    res = self.call_gemini(api_key, user_msg, history)
                elif api_key.startswith('gsk_'):
                    # Groq Key (Free Llama 3)
                    res = self.call_groq(api_key, user_msg, history)
                elif api_key:
                    # Generic try Gemini then OpenAI
                    try:
                        res = self.call_gemini(api_key, user_msg, history)
                    except:
                        res = self.call_openai(api_key, user_msg, history)
                else:
                    # Smart Dynamic Free Rule Brain (No API Key needed at all!)
                    res = self.dynamic_free_brain(user_msg, history)

                self.send_json_response(res)

            except Exception as e:
                # If any error occurs, fall back to smart dynamic brain instead of failing!
                res = self.dynamic_free_brain(user_msg, history)
                res['note'] = f'API 호출 대신 스마트 엔진으로 응답함 ({str(e)[:50]})'
                self.send_json_response(res)
        else:
            self.send_error(404, "Endpoint not found")

    def call_gemini(self, api_key, user_msg, history):
        models_to_try = [
            'gemini-1.5-flash-latest',
            'gemini-1.5-flash',
            'gemini-2.0-flash',
            'gemini-1.5-pro',
            'gemini-pro'
        ]
        
        contents = [
            {"role": "user", "parts": [{"text": SYSTEM_INSTRUCTION + "\n\n이제 대화를 시작해."}]},
            {"role": "model", "parts": [{"text": "EMOTION: NEUTRAL\nRESPONSE: 안녕! 난 7살 지호야! 지금 빨간 미니카로 속도 대결할 건데, 넌 무슨 놀이 할 거야?\nRAPPORT_CHANGE: 0\nDEAL_STATUS: 대화 시작 💬"}]}
        ]

        for h in history[-4:]:
            r = "user" if h.get('sender') == 'user' else "model"
            contents.append({"role": r, "parts": [{"text": h.get('text', '')}]})
        
        contents.append({"role": "user", "parts": [{"text": user_msg}]})

        for m in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={api_key}"
            payload = json.dumps({
                "contents": contents,
                "generationConfig": {"temperature": 0.7, "maxOutputTokens": 150}
            }).encode('utf-8')

            req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
            try:
                with urllib.request.urlopen(req, timeout=8) as response:
                    if response.status == 200:
                        data = json.loads(response.read().decode('utf-8'))
                        raw_text = data['candidates'][0]['content']['parts'][0]['text']
                        return self.parse_structured_output(raw_text, f'Gemini ({m})')
            except Exception as e:
                continue
        
        raise Exception("모든 Gemini 모델 엔드포인트 응답 실패")

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

        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read().decode('utf-8'))
            raw_text = data['choices'][0]['message']['content']
            return self.parse_structured_output(raw_text, 'OpenAI (gpt-4o-mini)')

    def dynamic_free_brain(self, user_msg, history):
        """Smart contextual rule engine when no API key is provided or offline"""
        text = user_msg.lower()

        # 1. 뺏기 / 소리치기 / 공격
        if any(w in text for w in ['내놔', '내놓', '뺏', '비켜', '죽을', '빨리 줘', '소리', '야!']):
            return {
                'text': "싫어! 내가 먼저 잡았단 말이야! 왜 소리 질러? 너랑 안 놀아!",
                'emotion': 'ANGRY',
                'rapportChange': -20,
                'dealStatus': '거절 ❌',
                'engine': '스마트 프리 두뇌'
            }

        # 2. 블록 / 터널 / 자동차 합체 딜
        if any(w in text for w in ['블록', '터널', '도로', '합치', '통과', '같이 만들']):
            return {
                'text': "우와 진짜? 블록으로 터널 만든다고? 대박! 그럼 내가 차 슝- 통과시킬게!",
                'emotion': 'HAPPY',
                'rapportChange': +30,
                'dealStatus': '딜 성공 🤝 (결합 딜)',
                'engine': '스마트 프리 두뇌'
            }

        # 3. 가위바위보 / 순서 / 차례
        if any(w in text for w in ['가위바위보', '순서', '차례', '이긴 사람', '먼저']):
            return {
                'text': "좋아! 가위바위보 하자! 안 내면 진 거 가위 바위 보! 내가 이기면 나 먼저 1판 할게!",
                'emotion': 'HAPPY',
                'rapportChange': +25,
                'dealStatus': '순서 딜 ✌️',
                'engine': '스마트 프리 두뇌'
            }

        # 4. 놀림 / 장난
        if any(w in text for w in ['바보', '짝짝이', '메롱', '느림보', '괴물', '못생']):
            return {
                'text': "흥, 짝짝이 양말이 요즘 유행이거든? 그래서 뭐? 난 내 차 굴릴 거야~",
                'emotion': 'COOL',
                'rapportChange': 0,
                'dealStatus': '쿨방어 🛡️',
                'engine': '스마트 프리 두뇌'
            }

        # 5. 의심 / 확인 ("되는 거냐고", "진짜야?", "아닌 거 같은데")
        if any(w in text for w in ['되는', '아닌', '진짜', '거짓말', '맞아', '뭐해', '누구']):
            responses = [
                "당연하지! 나 지금 빨간 미니카 바퀴 굴리고 있는데? 너 뭐 하는데?",
                "진짜라니까! 내 차 엄청 빠르거든? 너도 만져볼래?",
                "응! 난 7살 지호야! 너 지금 무슨 장난감 갖고 있어?"
            ]
            import random
            return {
                'text': random.choice(responses),
                'emotion': 'CURIOUS',
                'rapportChange': +5,
                'dealStatus': '대화 중 💬',
                'engine': '스마트 프리 두뇌'
            }

        # 6. 일반 대화
        return {
            'text': f"응! 난 미니카 경주가 제일 재밌어! 너는 무슨 놀이 제일 좋아해?",
            'emotion': 'NEUTRAL',
            'rapportChange': +10,
            'dealStatus': '질문 토스 🏓',
            'engine': '스마트 프리 두뇌'
        }

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
