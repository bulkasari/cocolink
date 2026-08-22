import os
import json
import re
from http.server import SimpleHTTPRequestHandler
import socketserver
import google.generativeai as genai
import urllib.request
import urllib.error

PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

SYSTEM_INSTRUCTION = """너는 유치원에서 빨간 미니카를 가지고 놀고 있는 7세 장난꾸러기 남자아이 '지호'야.
대화 상대는 같은 반 또래 친구(발달지연/자폐스펙트럼 아동)야.

[지호의 성격 및 대화 규칙]
1. 7세 아이 말투로 짧게 1~2문장(30자 내외)으로 신나게 또는 뾰루퉁하게 대답해. 절대 어른이나 AI처럼 장황하게 설명하지 마!
2. 상대방이 무조건 반말/명령/공격/욕/짜증을 내면 (예: "야 인마", "놀기 싫어", "내놔"):
   - 뾰루퉁하게 거절하거나 화를 내: "뭐라고? 왜 화내? 그럼 나 너랑 안 놀아 흥!" 또는 "야 인마라니! 너 말 그렇게 하면 장난감 안 빌려줘!"
   - EMOTION: ANGRY, RAPPORT_CHANGE: -15, DEAL_STATUS: 거절 ❌
3. 상대방이 '블록 터널 만들기', '가위바위보 순서 정하기', '시간 나누기' 등 타협안(Deal)을 제안하면:
   - 아주 신나서 기쁘게 수락해: "우와 진짜? 블록 터널? 대박! 그럼 내가 차 굴려볼게!"
   - EMOTION: HAPPY, RAPPORT_CHANGE: +30, DEAL_STATUS: 딜 성공 🤝
4. 상대방이 놀리거나 장난치면:
   - 어깨를 으쓱하며 쿨하게 유머로 무시해: "그래서 뭐? 짝짝이 양말이 요즘 유행이거든~"
   - EMOTION: COOL, RAPPORT_CHANGE: 0, DEAL_STATUS: 쿨방어 🛡️
5. 상대방이 의심하거나 질문하면:
   - 7살 아이답게 자연스럽게 대답해: "진짜라니까! 내 차 엄청 빠르거든? 너 뭐 해?"
   - EMOTION: CURIOUS, RAPPORT_CHANGE: +5, DEAL_STATUS: 대화 중 💬
6. 일반적인 인사나 대화:
   - 7세 아이답게 반갑게 대답해: "응 안녕! 너 오늘 유치원에 무슨 가방 메고 왔어?"
   - EMOTION: NEUTRAL, RAPPORT_CHANGE: +10, DEAL_STATUS: 대화 중 💬

[반드시 아래 4줄 형식으로만 출력할 것 (다른 설명 일체 금지)]
EMOTION: [HAPPY / ANGRY / COOL / CURIOUS / NEUTRAL]
RESPONSE: (지호의 실제 7세 대사 1~2문장)
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

                if not api_key:
                    self.send_json_response({
                        'error': '상단에 Google Gemini API Key를 입력해야 LLM이 실시간으로 생각하고 대답할 수 있습니다. 키를 입력해 주세요!'
                    }, 400)
                    return

                print(f"\n[USER INPUT]: {user_msg}")

                # Call Google Gemini official SDK directly
                if api_key.startswith('sk-') and not api_key.startswith('sk-ant'):
                    res = self.call_openai_llm(api_key, user_msg, history)
                else:
                    res = self.call_gemini_smart(api_key, user_msg, history)

                print(f"[LLM OUTPUT ({res.get('engine')})]: {res.get('text')}")
                self.send_json_response(res)

            except Exception as e:
                err_msg = str(e)
                print(f"[LLM CALL ERROR]: {err_msg}")
                self.send_json_response({
                    'error': f'Gemini LLM 호출 에러: {err_msg}'
                }, 500)
        else:
            self.send_error(404, "Endpoint not found")

    def call_gemini_smart(self, api_key, user_msg, history):
        """Pure generative Gemini LLM call with dynamic model discovery"""
        genai.configure(api_key=api_key)
        
        # Build prompt with history
        history_context = ""
        for h in history[-6:]:
            sender = "친구" if h.get('sender') == 'user' else "지호"
            history_context += f"{sender}: {h.get('text', '')}\n"

        prompt = f"""{SYSTEM_INSTRUCTION}

[지금까지의 대화 내용]:
{history_context}
[친구의 새로운 말]: {user_msg}

[7세 지호의 답변 (반드시 지정된 4줄 포맷으로만 출력)]:"""

        # 1. Discover available models for this specific API key
        try:
            available_models = []
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    available_models.append(m.name)
        except Exception as e:
            available_models = []
            print(f"list_models error: {e}")

        # Fallback list if list_models was empty
        if not available_models:
            available_models = ['models/gemini-1.5-flash', 'models/gemini-1.5-flash-latest', 'models/gemini-2.0-flash', 'models/gemini-1.5-pro', 'models/gemini-pro']

        # Sort priority: flash first
        def model_priority(m_name):
            if 'flash' in m_name: return 0
            if 'pro' in m_name: return 1
            return 2

        available_models.sort(key=model_priority)
        print(f"[Available Models for this Key]: {available_models[:4]}")

        last_error = ""
        for m_name in available_models:
            try:
                model = genai.GenerativeModel(m_name)
                response = model.generate_content(prompt)
                
                if response and response.text:
                    raw_text = response.text
                    clean_name = m_name.replace('models/', '')
                    return self.parse_structured_output(raw_text, f'Google Gemini ({clean_name})')
            except Exception as e:
                last_error = f"{m_name}: {str(e)}"
                print(f"Error on {m_name}: {e}")
                continue

        # If SDK failed, try direct REST API with standard models
        return self.call_gemini_rest_fallback(api_key, prompt, last_error)

    def call_gemini_rest_fallback(self, api_key, prompt, sdk_error):
        """Direct REST API fallback with multiple endpoints"""
        models = ['gemini-1.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash-latest', 'gemini-1.5-pro']
        last_rest_err = ""

        for m in models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={api_key}"
            payload = json.dumps({
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.7, "maxOutputTokens": 150}
            }).encode('utf-8')

            req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
            try:
                with urllib.request.urlopen(req, timeout=8) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode('utf-8'))
                        if data.get('candidates') and len(data['candidates']) > 0:
                            raw_text = data['candidates'][0]['content']['parts'][0]['text']
                            return self.parse_structured_output(raw_text, f'Gemini REST ({m})')
            except urllib.error.HTTPError as e:
                err_text = e.read().decode('utf-8')
                last_rest_err = f"{m} ({e.code}): {err_text}"
            except Exception as e:
                last_rest_err = str(e)

        raise Exception(f"API 키 인증 또는 모델 호출 실패.\n[SDK 에러]: {sdk_error}\n[REST 에러]: {last_rest_err}\n👉 Google AI Studio (https://aistudio.google.com/app/apikey)에서 발급받은 'Gemini API Key'가 맞는지 확인해 주세요.")

    def call_openai_llm(self, api_key, user_msg, history):
        """OpenAI GPT-4o-mini pure generative call"""
        url = "https://api.openai.com/v1/chat/completions"
        messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}]
        
        for h in history[-6:]:
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
            return self.parse_structured_output(raw_text, 'OpenAI GPT-4o-mini')

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
        print(f"CocoLink Pure LLM Voice Peer Server running on http://localhost:{PORT}")
        httpd.serve_forever()
