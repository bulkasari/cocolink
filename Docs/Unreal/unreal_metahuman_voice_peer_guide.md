# [언리얼 엔진 5] 메타휴먼 실시간 AI 음성 대화 & 립싱크 구현 가이드

본 문서는 **Unreal Engine 5**에서 **에픽게임즈 메타휴먼(MetaHuman)**과 **Georgy's Runtime Lip Sync** 플러그인을 사용하여, 우리 **CocoLink Gemini AI 백엔드와 실시간으로 음성 대화하고 표정과 입모양을 완벽하게 움직이는 전체 구현 가이드**입니다.

---

## 🏗️ 1. 전체 데이터 파이프라인

```
[ 🎙️ 아동 마이크 입력 ] 
       ⬇️ (언리얼 Audio Capture)
[ 🌐 HTTP POST /api/unreal/chat ] ➔ 로컬/클라우드 server.py 전송
       ⬇️ (Gemini 1.5 Flash 7세 페르소나 두뇌 처리)
[ 📦 JSON 응답 수신 ] ➔ { "text": "...", "emotion": "HAPPY", "unrealPayload": {...} }
       ⬇️
[ 🗣️ TTS 오디오 생성 및 재생 ] (Runtime Audio Importer / Windows TTS)
       ⬇️ (동시 트리거)
[ 🎭 Georgy 런타임 립싱크 + 표정 모프(Blendshapes) ] ➔ 메타휴먼 얼굴 실시간 연기!
```

---

## 🛠️ 2. 언리얼 엔진 5 필수 플러그인 셋업

1. **에픽게임즈 런처 ➔ 언리얼 엔진 5.3 / 5.4 / 5.5 실행** (Blank C++ or Blueprint 프로젝트 생성)
2. **필수 플러그인 활성화:**
   * `MetaHuman` (메타휴먼 기본 플러그인)
   * `Runtime MetaHuman Lip Sync` ([Georgy Dev 플러그인](https://solutions.georgy.dev/runtime-metahuman-lip-sync))
   * `Runtime Audio Importer` (실시간 오디오 WAV 로딩/재생용)
   * `VaRest` 또는 `HTTP Blueprint Support` (REST API 통신용)

---

## 🎮 3. 블루프린트(Blueprint) 핵심 로직 구현

메타휴먼 액터(`BP_MetaHuman_Jiho`) 안에 다음 3개의 블루프린트 이벤트를 연결합니다.

### ① 마이크 음성 인식 및 백엔드 전송 (Send Dialogue)
```blueprint
[ 마이크 녹음 종료 Event (Space 키 or Push-to-Talk) ]
   └──> [ VaRest / HTTP POST 호출 ]
          • URL: "http://localhost:8088/api/unreal/chat"
          • Headers: { "Content-Type": "application/json" }
          • JSON Body: {
               "message": "지호야, 우리 블록으로 터널 만들자!",
               "apiKey": "고객님_Gemini_API_KEY",
               "history": []
            }
```

### ② AI 응답 수신 및 감정 표정 세팅 (On Response Received)
```blueprint
[ HTTP On Request Complete ]
   └──> [ JSON 파싱: 'text' & 'emotion' 추출 ]
   └──> [ Switch on Emotion ('HAPPY', 'ANGRY', 'COOL', 'NEUTRAL') ]
          ├── 'HAPPY' ➔ [ Face Mesh: Set Morph Target 'mouthSmile_L/R' = 0.8 ]
          ├── 'ANGRY' ➔ [ Face Mesh: Set Morph Target 'browDown_L/R' = 0.9 ]
          └── 'COOL'  ➔ [ Face Mesh: Set Morph Target 'mouthSmile_R' = 0.5 ]
```

### ③ Georgy 런타임 립싱크 트리거 (Play & Lip Sync)
```blueprint
[ TTS Audio Buffer / SoundWave 생성 ]
   └──> [ Play Sound at Location (스피커 출력) ]
   └──> [ Georgy Runtime Lip Sync Component: 'Start Lip Sync from SoundWave' ]
          • Target Mesh: Face (메타휴먼 페이스 컴포넌트)
          • Weight: 1.0
```

---

## 🧪 4. 로컬 연동 테스트 방법 (1분 검증)

1. **우리 AI 백엔드 실행:**
   ```bash
   python "C:\Users\bulka\orca\workspaces\cocolink\cocolink\prototype_voice_peer\server.py"
   ```
2. **언리얼 엔진에서 Play (PIE) 실행**
3. 마이크로 말하거나 언리얼 UI 텍스트 박스에 *"야 인마"* 입력
4. ➔ **메타휴먼 지호가 미간을 찌푸리며(ANGRY 표정) *"야 인마라니! 너 말 그렇게 하면 안 놀아!"*를 음성으로 말하며 실시간 입모양 립싱크가 구동됩니다!**

---

## 💡 장점 요약
* **지구상 최고 그래픽:** 4K 모니터/대형 화면에서 1:1 실물 크기로 친구와 대화.
* **100% 라이선스 안전:** 언리얼 엔진 런타임 내 구동으로 에픽게임즈 라이선스 완벽 부합.
* **치료실/병원 납품용 최적:** 센터 전용 프리미엄 소프트웨어(`.exe`)로 즉시 빌드 및 배포 가능!
