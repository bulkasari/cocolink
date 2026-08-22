# [풀 시나리오 명세] 08. 관심사 독점 방지와 주고받는 핑퐁 토크
## : UCLA PEERS / Frankel & Wood Chapter 4 & 7 기반 스몰토크 & 관심사 공유 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/08_관심사_일방통행_방지_핑퐁토크.md`  
> **원전 레퍼런스:** 《Social Skills Success for Students with Autism》 Chapter 4 (Expanding Interests) & Chapter 7 (Improving Social Conversations)  
> **에피소드 코드:** `CONTENT-08-PINGPONG-TALK`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 일방적 독점 대화(Monologue) 아동  
> **핵심 가치:** "대화는 혼자 하는 발표가 아니에요! 2문장 말하고 탁구공을 친구에게 넘겨요!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🐰 **토끼 친구 '로미':** `Graphic/social/animation/romi_rabbit_turnaround.png`
* 🏓 **[3D 핑퐁 탁구대 & 말풍선 배경]:** `Graphic/social/animation/pingpong_chat_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '도윤' (밝은 7세 남아):** `Graphic/social/real/real_peer_doyun_turnaround.png`
* 🦖 **실사 공룡 피규어 및 포켓몬 카드 소품**
* 🏫 **[실사 교실 쉬는 시간 배경]:** `Graphic/social/real/real_classroom_break_bg.png`

---

## 🎬 STEP 1: Pre-Story (대화는 탁구 핑퐁이에요)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션

### 1-1. 혼자만 말하는 코코 (도입)
* **길이:** 8초 | **콘티:** 코코 곰돌이가 거대한 공룡 책을 들고 토끼 로미에게 쉼 없이 말함. 로미는 지루해서 하품을 함.
* **AI 프롬프트:** `3D cute animated style. A chubby teddy bear holding a dinosaur book talks nonstop without pausing. White rabbit yawns and looks bored. 8 seconds`

### 1-2. 지친 친구의 표정 (갈등)
* **길이:** 8초 | **콘티:** 로미가 한마디도 끼어들지 못하고 딴 곳을 쳐다봄. 코코 주변에 말풍선이 10개 쌓여 폭발 직전.
* **AI 프롬프트:** `3D animated style. Rabbit looks away exhausted. Too many speech bubbles pile up around the bear. Warning yellow sign, 8 seconds`

### 1-3. 핑퐁 대화의 마법 (해결책)
* **길이:** 14초 | **콘티:** 코코가 말을 멈추고 탁구 라켓으로 황금 공을 로미에게 퐁! 넘김. "로미야 너는 뭐 좋아해?" 묻자 로미가 활짝 웃으며 자기 이야기를 함.
* **AI 프롬프트:** `3D animated style. Teddy bear passes a glowing ping-pong ball of speech to the rabbit. Rabbit smiles happily and shares its story. Cheerful ping-pong sound, 14 seconds`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 🗣️ 1. 내 말 2문장 ] ➔ [ 🛑 2. 멈춤 ] ➔ [ 🏓 3. 마이크 토스 ] ➔ [ 👂 4. 친구 듣기 ] ➔ [ 🎁 5. 보상 ]
```

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 공룡 이름 5분 내내 읊기
* **길이:** 10초 | **콘티:** 코코가 "그리고 티라노는, 그리고 트리케라는..." 멈추지 않자 로미가 조용히 일어나 다른 데로 가버림. 속마음 `[💭 "나도 말하고 싶은데..."]` 🥱.
* **AI 프롬프트:** `3D animated style. Bear keeps rambling about dinosaurs. Rabbit quietly walks away feeling left out. Sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 2문장 말하고 "너는?" 물어보기
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 "나는 티라노가 좋아! 로미 너는 어떤 공룡 알아?" 묻자 로미가 "나는 익룡 프테라노돈 알아!" 신나게 대답.
* **AI 프롬프트:** `3D animated style. Rewind effect. Bear says 2 sentences and asks rabbit a question. Rabbit beams and responds excitedly. 15 seconds`
* **전환 나레이션:** "코코가 멋진 핑퐁 대화를 완성했어요! 이제 OO이 차례예요!" ➔ **Step 4 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 공룡 이야기 시작 (Start the Topic)
* **화면 연출 (1인칭 POV):** 교실 책상. 친구 도윤이 앞에서 내가 든 티라노사우루스 피규어를 보여주며 말함.
* **내 멘트:** "도윤아, 이 티라노사우루스 턱 힘이 엄청 세서 뼈도 다 부순대!"

### 🎬 Chapter 2: 도윤이의 지루한 신호 감지 (Detect Boredom)
* **화면 연출:** 도윤이가 하품을 살짝 하며 발을 까딱거림.
* **도윤이 속마음:** `[💭 "나 공룡 별로 안 좋아하는데... 언제 끝나지?"]` 🥱
* **나레이션:** "잠깐! 도윤이가 지루해하고 있어요. 2문장을 말했으니 도윤이에게 마이크를 넘겨볼까요?"

### 🎬 Chapter 3: 마이크 넘기기 인터랙션 (Pass the Mic)
* **인터랙션 (Swipe QTE):** 화면의 황금 마이크 아이콘을 도윤이 쪽으로 **[오른쪽으로 슥- 스와이프(Swipe Right)]**!

### 🎬 Chapter 4: 친구 관심사 질문하기 (Ask Friend's Interest)
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |  [ 🏓 ❓ "도윤아 너는 뭐 좋아해?" ]|    |    [ 🦖 공룡 백과사전 계속 읽기 ]|
  |  "공룡 말고 너는 어떤 놀이 좋아해?"|    |    "그리고 티라노 뼈 무게는..."  |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[도윤아 너는 뭐 좋아해]` 선택 시 도윤이가 눈을 번쩍 뜨며 표정이 밝아짐: "어? 나? 나는 포켓몬 카드 모으는 거 제일 좋아해!" (`peer_engagement_level: 100`).

### 🎬 Chapter 5: 맞장구치기 (Connected Reaction)
* **PECS 리액션:** `[⚡ 👍 "포켓몬? 나 피카츄 알아! 멋지다!"]`
* **결과 연출:** 도윤이가 주머니에서 반짝이 피카츄 카드를 꺼내 보여주며 "이거 봐! 진짜 멋있지?" 둘이 함께 웃음 (`conversation_balance_ratio: 50:50`).

### 🎬 Chapter 6: 보상 획득 (Reward)
* **보상:** `[🏓 대화 핑퐁 챔피언 황금 배지]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 대화 독점 방지 [2문장 말하고 ➔ "너는?" 토스]   │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   아이가 한 가지 관심사만 계속 쏟아낼 때:                   │
│   👉 "재미있는 이야기네! 이제 탁구공을 엄마한테 넘겨줘!      │
│      '엄마는 어때요?'라고 질문해 볼까?" 핑퐁을 상기시켜 주세요.│
│                                                           │
│ 📱 잠금화면 큐카드: [1. 🗣️ 2문장 ➔ 2. 🏓 핑퐁 ➔ 3. ❓ "너는?"]   │
└───────────────────────────────────────────────────────────┘
```
