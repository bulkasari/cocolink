# [앱 풀 시나리오 명세] CocoLink Social: 딜(Deal) 만들기와 순서 정하기
## : 마스터 기획서 기반 4-Step 풀 인터랙티브 에피소드 & AI 프롬프트 명세

> **에피소드 코드:** `APP-EP01-DEAL-AND-TURNS`  
> **기준 프레임워크:** Fast Track Unit III (Session 11~15) & CocoLink 4-Step App Architecture  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 화용언어 지연 아동  
> **핵심 학습 목표:** "하고 싶은 놀이가 다를 때, 싸우지 않고 가위바위보와 딜(Deal)로 함께 놀기"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🐰 **토끼 친구 '로미':** `Graphic/social/animation/romi_rabbit_turnaround.png`
* 🦊 **여우 친구 '폭시':** `Graphic/social/animation/foxy_fox_turnaround.png`
* 🏫 **[3D 유치원 놀이방 배경]:** `Graphic/social/animation/kindergarten_playroom_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 친구 '지호' (밝고 활발한 또래 남아):** `Graphic/social/real/real_peer_jiho_turnaround.png`
* 👧 **실사 친구 '수아' (다정하고 차분한 또래 여아):** `Graphic/social/real/real_peer_sua_turnaround.png`
* 👩‍🏫 **실사 담임 선생님:** `Graphic/social/real/real_teacher_turnaround.png`
* 🏫 **[실사 유치원 자유놀이 교실 배경]:** `Graphic/social/real/real_classroom_play_bg.png`

---

## 🎬 STEP 1: Pre-Story (친구와 생각이 다를 때)

> **목적:** 친구와 하고 싶은 놀이가 다를 때 왜 싸우지 않고 타협해야 하는지 3인칭 동화로 사전 개념 형성.  
> **형식:** 30초 3D 부드러운 파스텔 톤 애니메이션 (마리오 3D 월드 감성)

### 1-1. 서로 다른 장난감 (갈등 도입)
* **참조 캐릭터:** 🐻 `coco_bear_turnaround.png`, 🐰 `romi_rabbit_turnaround.png`
* **길이:** 8초 | **구도:** 3인칭 풀 샷
* **콘티:** 코코 곰돌이는 거대한 블록 성을 만들고 싶어 하고, 토끼 로미는 미니카 트랙을 만들고 싶어 함. 서로 자기 장난감을 가리키며 옥신각신함.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D cute pastel animated style, Mario 3D World aesthetic, smooth vinyl toy texture. A cute fluffy young teddy bear holding colorful toy blocks and a little rabbit holding a toy race car, gesturing at their toys in a cozy kindergarten playroom. Bright warm lighting, 8 seconds`
  * **[한글 해석]:**
    > `3D 귀여운 파스텔 애니메이션 스타일 (마리오 3D 월드 감성, 매끄러운 비닐 질감). 알록달록한 장난감 블록을 든 귀여운 아기 곰돌이와 장난감 레이싱카를 든 작은 토끼가 아늑한 유치원 놀이방에서 각자 장난감을 가리키는 장면. 밝고 따뜻한 조명, 8초`

### 1-2. 싸우면 아무도 못 놀아요 (문제 인식)
* **길이:** 8초 | **구도:** 3인칭 미디엄 샷
* **콘티:** 서로 자기 것만 하겠다고 고집부리다가 블록과 미니카가 엉켜 쓰러짐. 둘 다 속상해서 뾰루퉁하게 등을 돌림.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D cute animated style. The teddy bear and rabbit turn their backs to each other with grumpy pouting faces, arms crossed. Scattered toy blocks and cars on the floor. Soft sad lighting, 8 seconds`
  * **[한글 해석]:**
    > `3D 귀여운 애니메이션 스타일. 곰돌이와 토끼가 팔짱을 끼고 뾰루퉁한 표정으로 서로 등을 돌리고 앉아 있는 장면. 바닥에 흩어진 블록과 자동차. 부드러운 아쉬운 조명, 8초`

### 1-3. 마법의 딜(Deal) 만들기 (해결책 제시)
* **길이:** 14초 | **구도:** 3인칭 클로즈업 ➔ 풀 샷
* **콘티:** 여우 선생님이 나타나 전구 아이콘을 띄움. 블록으로 미니카 터널을 만들어 함께 놀자 두 친구가 활짝 웃으며 하이파이브! "우리에겐 마법의 '딜(Deal)'이 있어요!" 나레이션.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D cute animated style. A friendly fox teacher gently suggests an idea with a glowing lightbulb icon. The teddy bear and rabbit happily combine blocks into a car tunnel, racing the toy car through it, high-fiving with big smiles. Cheerful atmosphere, 14 seconds`
  * **[한글 해석]:**
    > `3D 귀여운 애니메이션 스타일. 친절한 여우 선생님이 빛나는 전구 아이콘과 함께 아이디어를 제안함. 곰돌이와 토끼가 기쁘게 블록으로 자동차 터널을 만들고 그 사이로 미니카를 달리며 활짝 웃으며 하이파이브함. 화사하고 경쾌한 분위기, 14초`

---

## 🎨 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 🗣️ 1. 대화 ] ➔ [ ✌️ 2. 가위바위보 ] ➔ [ 🤝 3. 딜 만들기 ] ➔ [ 🎮 4. 함께 놀기 ] ➔ [ 🎁 5. 보상 ]
```
* 화면 최상단 40px 고정 HUD. 현재 단계는 황금빛 테두리 펄스 애니메이션.

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링 관찰)

> **형식:** 3인칭 3D 캐주얼 애니메이션 (What Went Wrong ➔ Positive Model)

### 3-1. [서툰 행동]: 코코의 떼쓰기 실패
* **길이:** 10초 | **콘티:** 코코가 친구 토끼의 자동차를 홱 뺏음 ➔ 토끼가 울음을 터뜨리고 선생님이 다가와 타임아웃을 줌.
* **속마음 말풍선:** 토끼 로미 `[💭 "내 자동차 뺏겨서 너무 슬퍼!"]` 😭
* **AI 프롬프트:**
  > `3D animated style. A young teddy bear snatches a toy car from a crying rabbit. The screen pauses with a sad thought bubble above the rabbit. 10 seconds`

### 3-2. [올바른 행동]: 코코의 가위바위보 & 딜 성공
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 손을 내밀어 "가위바위보 하자!" 제안 ➔ 이긴 토끼가 먼저 차 굴리기 ➔ 1분 뒤 코코가 블록 터널 설치 ➔ 성공!
* **AI 프롬프트:**
  > `3D animated style. Rewind effect. The teddy bear plays rock-paper-scissors with the rabbit, smiling politely. They take turns playing with the car and blocks together happily. 15 seconds`
* **전환 나레이션:** "코코도 멋지게 타협했어요! 이제 OO이 차례예요!" ➔ **Step 4(1인칭 실사)로 전환!**

---

## 🎬 STEP 4: Interactive Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 친구에게 다가가기 & 눈맞춤 (Approach & Eye Contact)
* **화면 연출 (1인칭 POV):** 교실 바닥. 또래 친구(지호)가 바닥에 앉아 빨간색 미니카를 굴리고 있음.
* **인터랙션 (QTE):** 지호의 어깨 주변에 노란 펄스 링 ➔ **[가볍게 탭(Tap)하기]**
* **결과 연출:** 1인칭 시점이 지호 앞 50cm 거리로 다가가며 지호와 자연스럽게 눈을 맞춤. 지호가 고개를 들며 "안녕 OO아!" 미소. (`peer_rapport: +20`).

---

### 🎬 Chapter 2: 하고 싶은 놀이 말하기 & 경청 (Express & Listen)
* **화면 연출:** 내 손에 든 파란색 공룡 블록이 보임.
* **지호 대사:** "OO아, 나랑 이 미니카로 속도 대결할래?"
* **속마음 말풍선:** 지호 머리 위 `[💭 "새로 산 미니카 자랑하고 싶은데!"]` 🏎️
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ 🦖 💬 "나 블록 하고 싶어" ] |    |    [ 💥 미니카 발로 차기 ]       |
  |  "나는 공룡 블록 만들고 싶어!"   |    |    지호 미니카 발로 차고 소리치기 |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[나 블록 하고 싶어]` 선택 시:
  * 1인칭 손으로 블록을 보여주며 또렷하게 말함: "나는 공룡 블록 만들고 싶은데!"
  * 지호가 머리를 긁적임: "어? 나는 자동차 놀이 하고 싶은데..." (`social_dialogue: +30`).

---

### 🎬 Chapter 3: 가위바위보 순서 정하기 (Rock-Paper-Scissors Minigame)
* **상황:** 서로 하고 싶은 놀이가 다름.
* **PECS 멘트 제안:** `[✌️ ✊ 🖐️ "가위바위보로 순서 정하자!"]`
* **인터랙티브 미니게임:**
  * 화면 하단에 `[ ✊ 바위 ]`, `[ ✌️ 가위 ]`, `[ 🖐️ 보 ]` 3개 버튼 등장.
  * 지호가 손을 흔들며 "안 내면 진 거 가위 바위 보!"
  * **(플레이어가 🖐️ 보를 냄 ➔ 지호가 ✌️ 가위를 내어 지호가 이김)**

---

### 🎬 Chapter 4: 2번째 순서 수용 & 3초 대기 (Accept 2nd Turn)
* **상황:** 내가 가위바위보에서 져서 지호가 먼저 자동차를 굴림.
* **지호 대사:** "야호! 내가 이겼다! 나 먼저 1판 달릴게!"
* **내면 감정:** 살짝 아쉽지만 약속을 지키는 순간.
* **인터랙션 (Hold 3-sec Countdown):**
  * 화면 중앙에 3초 모래시계 아이콘 등장.
  * **화면을 3초간 꾹 누르고 있기(Hold)** ➔ `3... 2... 1...`
  * 지호가 자동차를 `부우웅~` 1바퀴 굴리고 만족스럽게 웃음. (`fairness_index: +40`).

---

### 🎬 Chapter 5: 결합형 딜 만들기 (Make the Combined Deal)
* **화면 연출:** 지호가 자동차를 멈추고 나를 바라봄: "이제 OO이 차례야! 뭐 할래?"
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |  [ 🤝 🏰 ➔ 🏎️ "블록 터널 딜!" ]  |    |     [ 😒 "자동차 치워, 블록만 해" ]|
  |  "블록으로 터널이랑 도로 만들어서 |    |    지호 자동차 밀어내고 혼자 놀기 |
  |   미니카 통과시키자!"             |    |                                  |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[블록 터널 딜]` 선택 시:
  * 1인칭 손이 나와 노란색, 파란색 블록으로 아치형 터널을 바닥에 척척 설치함.
  * 지호의 눈이 휘둥그레짐: "우와 대박! 진짜 터널이다! 내가 여기로 차 통과시킬게!"
  * 지호가 터널 사이로 미니카를 `슝-!` 통과시키며 둘이 함께 환호함 (`peer_rapport: 100`).

---

### 🎬 Chapter 6: 하이파이브 & 보상 (High-Five & Reward)
* **화면 연출:** 지호가 손바닥을 쫙 펴며 정면 카메라를 향해 다가옴: "OO아, 우리 다음에도 이렇게 놀자! 짝!"
* **인터랙션 (High-Five Tap):** 지호의 손바닥을 타이밍에 맞춰 **[짝! 탭하기]**
* **보상 연출:**
  * 상단 Visual Schedule의 5개 아이콘이 모두 황금색 체크(✅)로 점등!
  * 팡파레 음악과 함께 `[🤝 최고의 딜 메이커 황금 트로피 스티커]`가 스탬프 북에 쿵! 찍힘.

---

## 📱 STEP 5: Home Bridge (부모/치료사 요약 화면)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 리포트            │
├───────────────────────────────────────────────────────────┤
│ [학습 완료] 딜(Deal) 만들기와 가위바위보 순서 정하기        │
│ [아동 성취도] 협상 유연성 100점 | 공정성 수용 100점        │
│                                                           │
│ 📌 보호자 오늘 실전 적용 가이드:                           │
│   오늘 저녁 식사 후 형제/또래와 놀 때 갈등이 생기면:       │
│   👉 "우리 코코링크에서 배운 [블록 터널 딜]처럼 합쳐볼까?"    │
│      마법의 단어 "딜(Deal)"을 상기시켜 주세요!              │
│                                                           │
│ 📱 잠금화면 큐카드: [1. ✌️ 가위바위보 ➔ 2. 🤝 합치기 딜]   │
└───────────────────────────────────────────────────────────┘
```
