import os
import json
import urllib.request
import urllib.error
from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver

PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class PeerProxyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                req_json = json.loads(post_data.decode('utf-8'))
                user_msg = req_json.get('message', '')
                api_key = req_json.get('apiKey', '').strip()
                history = req_json.get('history', [])
                model_name = req_json.get('model', 'gemini-1.5-flash').strip()

                if not api_key:
                    self.send_json_response({'error': 'API 키가 입력되지 않았습니다. 상단에 Gemini API Key를 입력해 주세요.'}, 400)
                    return

                # Clean model name
                clean_model = model_name.replace('models/', '')
                
                # Gemini system prompt & history formatting
                system_instruction = """
너는 유치원에서 빨간 미니카를 가지고 놀고 있는 7세 장난꾸러기 남자아이 '지호'야.
대화 상대는 같은 반 또래 친구(발달지연/자폐스펙트럼 아동)야.

[지호의 성격 및 사회성 훈련 규칙]
1. 7세 아이 말투로 짧게 1~2문장(30자 내외)으로 신나게 또는 뾰루퉁하게 대답해. 절대 어른이나 인공지능처럼 길게 설명하지 마!
2. 상대방이 무조건 명령하거나 장난감을 뺏으려 하면(예: "내놔", "빨리 줘", "소리치기"):
   - 뾰루퉁하게 거절해: "싫어! 내가 먼저 잡았단 말이야! 너랑 안 놀아!"
   - EMOTION: ANGRY, RAPPORT_CHANGE: -20, DEAL_STATUS: 거절 ❌
3. 상대방이 '블록 터널 만들기', '가위바위보 순서 정하기', '시간 나누기' 등 타협안(Deal)을 제안하면:
   - 아주 신나고 기쁘게 수락해: "우와 진짜? 블록 터널? 대박! 그럼 내가 차 굴려볼게!"
   - EMOTION: HAPPY, RAPPORT_CHANGE: +30, DEAL_STATUS: 딜 성공 🤝
4. 상대방이 놀리거나 장난치면(예: "짝짝이 양말 바보"):
   - 어깨를 으쓱하며 쿨하게 유머로 무시해: "그래서 뭐? 짝짝이 양말이 요즘 유행이거든~"
   - EMOTION: COOL, RAPPORT_CHANGE: 0, DEAL_STATUS: 쿨방어 🛡️
5. 상대방이 질문하거나 딴소리/의심할 때(예: "되는 거냐고", "진짜야?"):
   - 7살 아이답게 당당하게 대답해: "당연하지! 나 지금 빨간 미니카 바퀴 굴리고 있는데? 너 뭐 하는데?"
   - EMOTION: CURIOUS, RAPPORT_CHANGE: +5, DEAL_STATUS: 대화 중 💬
6. 일반적인 인사나 질문:
   - 7세 아이답게 신나게 답변하고 질문을 던져.
   - EMOTION: NEUTRAL, RAPPORT_CHANGE: +10, DEAL_STATUS: 대화 중 💬

[반드시 아래 4줄 형식으로만 출력할 것]
EMOTION: [HAPPY / ANGRY / COOL / CURIOUS / NEUTRAL]
RESPONSE: (지호의 실제 7세 대사)
RAPPORT_CHANGE: (+30 / -20 등 숫자)
DEAL_STATUS: (결과 요약)
"""

                # Build Gemini API payload
                contents = []
                # Add context
                contents.append({
                    "role": "user",
                    "parts": [{"text": system_instruction + "\n\n이제 대화를 시작해."}]
                })
                contents.append({
                    "role": "model",
                    "parts": [{"text": "EMOTION: NEUTRAL\nRESPONSE: 안녕! 난 7살 지호야! 지금 빨간 미니카로 속도 대결할 건데, 넌 무슨 놀이 할 거야?\nRAPPORT_CHANGE: 0\nDEAL_STATUS: 대화 시작 💬"}]
                })

                # Append history
                for h in history[-6:]:
                    r = "user" if h.get('sender') == 'user' else "model"
                    contents.append({
                        "role": r,
                        "parts": [{"text": h.get('text', '')}]
                    })

                # Append latest user message
                contents.append({
                    "role": "user",
                    "parts": [{"text": user_msg}]
                })

                # Try models in order: requested model, then fallbacks
                models_to_try = [clean_model, 'gemini-1.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash-latest', 'gemini-1.5-pro', 'gemini-pro']
                # Remove duplicates while preserving order
                unique_models = []
                for m in models_to_try:
                    if m not in unique_models:
                        unique_models.append(m)

                last_error = ""
                success_data = None

                for m in unique_models:
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={api_key}"
                    payload = json.dumps({
                        "contents": contents,
                        "generationConfig": {
                            "temperature": 0.7,
                            "maxOutputTokens": 150
                        }
                    }).encode('utf-8')

                    req = urllib.request.Request(
                        url,
                        data=payload,
                        headers={'Content-Type': 'application/json'}
                    )

                    try:
                        with urllib.request.urlopen(req, timeout=10) as response:
                            if response.status == 200:
                                res_body = response.read().decode('utf-8')
                                success_data = json.loads(res_body)
                                break
                    except urllib.error.HTTPError as e:
                        err_text = e.read().decode('utf-8')
                        last_error = f"Model {m} error ({e.code}): {err_text}"
                        continue
                    except Exception as e:
                        last_error = str(e)
                        continue

                if not success_data or 'candidates' not in success_data or not success_data['candidates']:
                    self.send_json_response({'error': f'Gemini 호출 실패: {last_error}'}, 500)
                    return

                raw_text = success_data['candidates'][0]['content']['parts'][0]['text']

                # Parse lines
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
                            rapport_delta = int(line.replace('RAPPORT_CHANGE:', '').replace('+', '').strip())
                        except:
                            rapport_delta = 0
                    elif line.startswith('DEAL_STATUS:'):
                        deal_status = line.replace('DEAL_STATUS:', '').strip()

                self.send_json_response({
                    'text': response_text,
                    'emotion': emotion,
                    'rapportChange': rapport_delta,
                    'dealStatus': deal_status,
                    'raw': raw_text
                })

            except Exception as e:
                self.send_json_response({'error': f'서버 처리 오류: {str(e)}'}, 500)
        else:
            self.send_error(404, "Endpoint not found")

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
        print(f"CocoLink Voice Peer Server running on http://localhost:{PORT}")
        httpd.serve_forever()
