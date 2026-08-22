# [풀 시나리오 명세] 07. 대화가 어색해졌을 때 살려내기 (대화 복구)
## : UCLA PEERS / Frankel & Wood Chapter 6 기반 대화 복구(Conversation Repair) 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/07_대화가_어색해졌을때_살려내기.md`  
> **원전 레퍼런스:** 《Social Skills Success for Students with Autism》 Chapter 6 (Conversational Comprehension & Repair Strategies)  
> **에피소드 코드:** `CONTENT-07-CONVERSATION-REPAIR`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 대화 단절 및 침묵 불안 아동  
> **핵심 가치:** "말을 못 알아들었을 땐 '다시 말해줄래?' 되묻고, 침묵이 흐를 땐 질문으로 대화를 살려내요!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🦊 **여우 친구 '폭시':** `Graphic/social/animation/foxy_kid_turnaround.png`
* 🍱 **[3D 유치원 급식실 테이블 배경]:** `Graphic/social/animation/cafeteria_table_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '동현' (친절한 7세 남아):** `Graphic/social/real/real_peer_donghyun_turnaround.png`
* 🍱 **실사 식판 및 수저 소품**
* 🏫 **[실사 급식실 배경]:** `Graphic/social/real/real_cafeteria_bg.png`

---

## 🎬 STEP 1: Pre-Story (대화가 뚝 끊겼을 때)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션

### 1-1. 웅얼거리는 친구와 침묵 (도입)
* **길이:** 8초 | **콘티:** 곰돌이 코코와 여우 폭시가 급식실에서 밥을 먹음. 폭시가 밥을 먹으며 웅얼웅얼 말하자 코코가 못 알아듣고 멍하니 침묵이 흐름.
* **AI 프롬프트:** `3D cute animated style. A teddy bear and fox sitting at a cafeteria table. Fox speaks with mouth full (muffled), bear looks puzzled with silence and awkward sweatdrop icon. 8 seconds`

### 1-2. 엉뚱한 대답의 위험 (갈등)
* **길이:** 8초 | **콘티:** 코코가 아는 척하며 엉뚱한 대답을 하자 폭시가 "어? 내 말 못 들었구나..." 하고 어색해하며 등을 돌림.
* **AI 프롬프트:** `3D animated style. Teddy bear gives an awkward unrelated answer. Fox looks confused and silent. 8 seconds`

### 1-3. 대화 심폐소생술 (해결책)
* **길이:** 14초 | **콘티:** 코코가 귀에 손을 대며 "미안, 다시 말해줄래?" 되묻고, "너는 주말에 뭐 했어?" 질문을 던지자 대화가 활짝 꽃피움!
* **AI 프롬프트:** `3D animated style. Teddy bear politely asks for repetition, then asks a friendly question. The fox lights up with excitement, chatting joyfully. Bright chat bubble icons, 14 seconds`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 👂 1. 안 들림 ] ➔ [ 💬 2. 다시 묻기 ] ➔ [ ❓ 3. 질문 토스 ] ➔ [ 🗣️ 4. 신나는 대화 ] ➔ [ 🎁 5. 보상 ]
```

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 못 알아듣고 바닥만 보며 침묵하기
* **길이:** 10초 | **콘티:** 코코가 못 들었는데 가만히 바닥만 봄. 어색한 침묵 속에 폭시가 자리를 뜸. 속마음 `[💭 "나랑 이야기하기 싫은가 봐"]` 🥺.
* **AI 프롬프트:** `3D animated style. Bear stares at floor silently. Fox feels ignored and leaves with sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 솔직하게 되묻고 질문 던지기
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 "폭시야, 밥 먹느라 못 들었어! 다시 말해줘!" ➔ 폭시가 다시 말해줌 ➔ 코코가 "너는 어떤 만화 좋아해?" 질문 성공.
* **AI 프롬프트:** `3D animated style. Rewind effect. Bear politely asks fox to repeat, then asks about favorite cartoons. They talk excitedly. 15 seconds`
* **전환 나레이션:** "코코가 대화를 멋지게 살려냈어요! 이제 OO이 차례예요!" ➔ **Step 4 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 웅얼거리는 친구 (Unclear Speech)
* **화면 연출 (1인칭 POV):** 급식실 테이블. 맞은편 친구 동현이가 밥을 먹으며 웅얼웅얼 말함: "우물우물... 뫄뫄... 어제 로봇... 웅얼..."
* **내면 당황:** "무슨 말인지 하나도 안 들렸어... 어떡하지?"

### 🎬 Chapter 2: 정중하게 되묻기 (Ask to Repeat)
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ 👂 💬 "다시 말해줄래?" ]      |    |     [ 🤐 멍하니 딴청 피우기 ]     |
  |  "미안, 밥 먹느라 못 들었어!     |    |    못 알아듣고 바닥만 쳐다보기   |
  |   한 번만 다시 말해줘!"          |    |                                  |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[다시 말해줄래]` 선택 시 동현이가 꿀꺽 삼키고 또렷하게 말함: "아! 어제 새로 나온 변신 로봇 만화 봤냐고 물어봤어!" (`clarification_confidence: +40`).

### 🎬 Chapter 3: 대답과 어색한 침묵 (Short Answer & Silence)
* **화면 연출:** 내가 "응, 봤어." 한마디 하고 3초간 어색한 침묵이 흐름. 
* **효과음:** `귀뚜라미 우는 소리 찌르르...`

### 🎬 Chapter 4: 질문 다리 놓기 (Question Bridge)
* **PECS 멘트 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |  [ ❓ "너는 어떤 로봇 좋아해?" ]  |    |     [ 🤐 가만히 밥만 먹기 ]       |
  |  (동현이 관심사 물어보기)         |    |    아무 말 없이 숟가락질만 하기  |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[너는 어떤 로봇 좋아해]` 선택 시 동현이가 눈을 번쩍이며 "나는 파란색 드래곤 로봇! 불 뿜는 게 대박이었어!"라며 신나게 대답함 (`conversation_repair_skill: 100`).

### 🎬 Chapter 5: 맞장구치기 (Active Listening)
* **인터랙션 (Nod Tap):** 고개를 끄덕이는 제스처 탭 (Tap).
* **내 멘트:** "우와! 나도 드래곤 로봇 멋있더라!"

### 🎬 Chapter 6: 보상 획득 (Reward)
* **보상:** `[🎙️ 대화 심폐소생술 마스터 배지]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 대화 끊겼을 때 ["다시 말해줘" ➔ 질문 토스]     │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   집에서 대화가 끊겼을 때:                                  │
│   👉 "대화가 멈췄을 땐 상대방에게 [너는 어때?]라고 질문을  │
│      던지면 대화가 다시 살아난단다!" 가르쳐 주세요.         │
│                                                           │
│ 📱 잠금화면 큐카드: [1. 👂 "다시 말해줘" ➔ 2. ❓ "너는 어때?"] │
└───────────────────────────────────────────────────────────┘
```
