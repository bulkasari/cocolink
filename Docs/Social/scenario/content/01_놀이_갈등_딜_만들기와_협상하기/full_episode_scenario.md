# [풀 시나리오 명세] 01. 놀이 갈등 딜(Deal) 만들기와 협상하기
## : Fast Track Session 11 & 12 기반 상호 타협 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/01_딜_만들기와_협상하기.md`  
> **원전 레퍼런스:** 《Fast Track Friendship Group Manual》 Unit III, Session 11 & 12 (Planning Together and Making a Deal)  
> **에피소드 코드:** `CONTENT-01-DEAL-MAKING`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 화용언어 지연 아동  
> **핵심 가치:** "하고 싶은 놀이가 달라도 싸우지 않아요! 합치거나 시간을 나누는 딜(Deal)이 있어요!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🐰 **토끼 친구 '로미':** `Graphic/social/animation/romi_rabbit_turnaround.png`
* 🦊 **여우 선생님 '폭시':** `Graphic/social/animation/foxy_teacher_turnaround.png`
* 🏫 **[3D 유치원 놀이방 배경]:** `Graphic/social/animation/kindergarten_playroom_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '지호' (활발한 7세 남아):** `Graphic/social/real/real_peer_jiho_turnaround.png`
* 👩‍🏫 **실사 담임 선생님:** `Graphic/social/real/real_teacher_turnaround.png`
* 🏫 **[실사 유치원 교실 바닥/테이블]:** `Graphic/social/real/real_classroom_floor_bg.png`

---

## 🎬 STEP 1: Pre-Story (친구와 생각이 다를 때)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션 (마리오 3D 월드 비닐 질감)

### 1-1. 서로 다른 장난감 (갈등 도입)
* **길이:** 8초 | **구도:** 3인칭 풀 샷
* **콘티:** 곰돌이 코코는 블록을 안고 있고, 토끼 로미는 장난감 레이싱카를 쥐고 있음. 서로 자기 장난감이 최고라며 가리킴.
* **AI 비디오 프롬프트:**
  * **[영문]:** `3D cute pastel animated style, Mario 3D World aesthetic, smooth vinyl toy texture. A fluffy teddy bear holding colorful building blocks and a cute white rabbit holding a toy race car, gesturing excitedly at their toys in a cozy kindergarten room. Bright soft lighting, 8 seconds`
  * **[한글]:** `3D 귀여운 파스텔 애니메이션 스타일 (마리오 3D 월드 감성). 알록달록한 블록을 든 곰돌이와 레이싱카를 든 흰 토끼가 아늑한 유치원 방에서 각자 장난감을 가리키며 옥신각신하는 장면. 밝고 부드러운 조명, 8초`

### 1-2. 고집부리면 아무도 못 놀아요 (문제 인식)
* **길이:** 8초 | **구도:** 3인칭 미디엄 샷
* **콘티:** 둘 다 "내 거 먼저 해!" 고집부리다가 장난감이 바닥에 뒹굴고, 서로 등을 돌리고 뾰루퉁하게 앉음.
* **AI 비디오 프롬프트:**
  * **[영문]:** `3D cute animated style. The teddy bear and rabbit turn their backs with arms crossed and pouting grumpy faces. Scattered blocks and toy cars on the mat. Soft melancholy lighting, 8 seconds`
  * **[한글]:** `3D 애니메이션 스타일. 곰돌이와 토끼가 팔짱을 끼고 뾰루퉁한 얼굴로 등을 돌리고 앉아 있는 모습. 매트 위에 흩어진 블록과 자동차. 8초`

### 1-3. 마법의 타협안 '딜(Deal)' (해결책 제시)
* **길이:** 14초 | **구도:** 3인칭 클로즈업 ➔ 풀 샷
* **콘티:** 여우 선생님이 빛나는 전구 카드를 보여줌. 코코와 로미가 블록으로 자동차 터널을 만들어 신나게 통과시키며 하이파이브!
* **AI 비디오 프롬프트:**
  * **[영문]:** `3D cute animated style. A friendly fox teacher presents a glowing deal card. The bear and rabbit joyfully build a block tunnel together and race the toy car through it, high-fiving with huge smiles. 14 seconds`
  * **[한글]:** `3D 애니메이션 스타일. 친절한 여우 선생님이 빛나는 딜 카드를 제시함. 곰과 토끼가 기쁘게 블록 터널을 짓고 차를 통과시키며 활짝 웃으며 하이파이브함. 14초`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 🗣️ 1. 대화하기 ] ➔ [ 👂 2. 친구 듣기 ] ➔ [ 🤝 3. 딜 제안 ] ➔ [ 🚗 4. 함께 놀기 ] ➔ [ 🎁 5. 보상 ]
```
* 화면 상단 고정 48px 바. 활성 단계는 1.2배 스케일 업 + 노란색 펄스 테두리.

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 장난감 뺏고 떼쓰기
* **길이:** 10초 | **콘티:** 코코가 로미의 자동차를 낚아채려다 로미가 울음을 터뜨림. 화면 정지 및 속마음 팝업 `[💭 "뺏겨서 너무 슬퍼!"]` 😭.
* **AI 프롬프트:** `3D animated style. Teddy bear grabs a toy car from a crying rabbit. Screen freezes with a sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 딜 제안하고 함께 놀기
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 "우리 블록으로 주차장 만들어서 같이 놀자!" 제안 ➔ 로미가 활짝 웃으며 수락 ➔ 둘이 함께 완성!
* **AI 프롬프트:** `3D animated style. Rewind effect. The teddy bear politely offers a deal to the rabbit. They joyfully construct a parking garage with blocks together. 15 seconds`
* **전환 나레이션:** "코코도 멋진 딜을 성공했어요! 이제 OO이 차례예요!" ➔ **Step 4(1인칭 실사) 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 친구 지호에게 다가가기 (Approach & Eye Contact)
* **화면 연출 (1인칭 POV):** 교실 바닥. 또래 친구(지호)가 바닥에서 빨간 미니카를 만지작거리고 있음.
* **인터랙션 (QTE):** 지호 주변 노란색 펄스 링 ➔ **[가볍게 어깨 탭(Tap)]**
* **결과 연출:** 1인칭 시점이 지호 앞 50cm 거리로 다가가며 눈맞춤. 지호가 "안녕 OO아!" 밝게 인사 (`peer_rapport: +20`).

### 🎬 Chapter 2: 하고 싶은 놀이 말하기 & 경청 (Say & Listen)
* **화면 연출:** 내 손에 든 파란색 공룡 블록이 보임.
* **지호 대사:** "OO아, 나랑 이 미니카로 속도 경주할래?"
* **지호 속마음:** `[💭 "새로 산 미니카 자랑하고 싶어!"]` 🏎️
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ 🦖 💬 "나 블록 하고 싶어" ] |    |     [ 💥 미니카 발로 차기 ]      |
  |  "나는 공룡 성 만들고 싶어!"     |    |    지호 미니카 발로 차고 소리치기 |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[나 블록 하고 싶어]` 선택 시 또렷하게 의사를 전달함. 지호가 "어? 나는 자동차 경주 하고 싶은데..." 고개를 갸웃함.

### 🎬 Chapter 3: 딜(Deal) 인터랙션 제안 (Propose the Deal)
* **상황:** 서로 원하는 놀이가 다름.
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |  [ 🤝 🏰 ➔ 🏎️ "블록 터널 딜!" ]  |    |     [ 😒 "자동차 치워, 블록만 해" ]|
  |  "블록으로 터널이랑 도로 만들어서 |    |    지호 자동차 밀어내고 혼자 놀기 |
  |   미니카 통과시키자!"             |    |                                  |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[블록 터널 딜]` 선택 시 지호의 머리 위 속마음 `[💭 "와! 터널 통과하면 진짜 재밌겠다!"]` 😄 ➔ 지호가 "대박! 진짜 좋은 생각이다! 같이 만들자!" 환호 (`negotiation_flexibility: 100`).

### 🎬 Chapter 4: 협동 조립 QTE (Build Together)
* **화면 연출:** 1인칭 손이 나와 노란 블록으로 아치형 터널 기둥을 세움.
* **인터랙션:** 화면 좌/우 기둥을 차례로 탭하여 연결 (Tap-Tap QTE).
* **결과 연출:** 튼튼하고 멋진 고속도로 터널 완성!

### 🎬 Chapter 5: 미니카 슝- 통과시키기 (Car Racing)
* **화면 연출:** 지호가 미니카를 터널 입구에 댐.
* **인터랙션:** 손가락으로 화면을 앞으로 **[Swipe Up 슉- 밀기]**
* **결과 연출:** 미니카가 터널을 `부우웅~ 슝-!` 번개처럼 통과하며 둘이 함께 환호성!

### 🎬 Chapter 6: 하이파이브 및 보상 (High-Five & Stamp)
* **화면 연출:** 지호가 손바닥을 내밀며 "OO아 우리 최고다! 짝!"
* **인터랙션:** 지호 손바닥을 타이밍 맞춰 **[짝! 탭하기]**
* **보상:** `[🤝 최고의 협상왕 황금 트로피 배지]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 놀이 갈등 시 [블록 터널 딜(합치기)] 제안하기    │
│ [추천 적용 시기] 형제나 친구와 서로 다른 놀이를 고집할 때  │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   "싸우지 말고 아까 앱에서 한 것처럼                      │
│   👉 [블록 + 자동차 = 터널 딜] 해볼까?" 딜을 유도하세요!    │
│                                                           │
│ 📱 잠금화면 큐카드: [1. 내 생각 ➔ 2. 친구 듣기 ➔ 3. 🤝 딜]  │
└───────────────────────────────────────────────────────────┘
```
