# [풀 시나리오 명세] 04. 보드게임 속임수(치팅) 충동 참기
## : Fast Track Session 17 & 18 기반 정직한 규칙 준수와 우정 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/04_속임수_치팅_충동_참기.md`  
> **원전 레퍼런스:** 《Fast Track Friendship Group Manual》 Unit IV, Session 17 (Resisting the Temptation to Cheat) & Session 18 (Putting Friendship First)  
> **에피소드 코드:** `CONTENT-04-RESIST-CHEATING`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 규칙 위반 및 치팅 충동 아동  
> **핵심 가치:** "속여서 이기는 것보다 정직하게 플레이하고 우정을 지키는 것이 최고예요!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🦊 **여우 친구 '폭시':** `Graphic/social/animation/foxy_kid_turnaround.png`
* 🐍 **[3D 뱀사다리 보드게임 배경]:** `Graphic/social/animation/snakes_boardgame_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '서준' (다정한 7세 남아):** `Graphic/social/real/real_peer_seojun_turnaround.png`
* 🎲 **실사 주사위 및 뱀사다리 게임판 소품**
* 🏫 **[실사 유치원 테이블 배경]:** `Graphic/social/real/real_playroom_table_bg.png`

---

## 🎬 STEP 1: Pre-Story (정직한 게임의 힘)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션

### 1-1. 주사위의 유혹 (도입)
* **길이:** 8초 | **콘티:** 곰돌이 코코가 뱀사다리 게임을 함. 1등을 하고 싶은 마음에 주사위 눈금을 몰래 손으로 돌리려 함.
* **AI 프롬프트:** `3D cute animated style. A chubby teddy bear looking around sneakingly, hesitating to flip a dice with its paw on a board game table. 8 seconds`

### 1-2. 속임수의 대가 (문제 인식)
* **길이:** 8초 | **콘티:** 친구 폭시가 이를 눈치채고 "너 속였지? 치사해!" 실망하며 자리를 떠남. 코코가 혼자 남아 외로워함.
* **AI 프롬프트:** `3D animated style. Little fox walks away looking disappointed, crossing arms. Teddy bear sits alone looking sad with an empty game board. 8 seconds`

### 1-3. 정직한 우정의 승리 (해결책)
* **길이:** 14초 | **콘티:** 코코가 나온 숫자 그대로 정직하게 말을 움직이자, 폭시가 "코코야 너 진짜 멋지다!" 엄지척하며 서로 믿고 끝까지 완주함.
* **AI 프롬프트:** `3D animated style. Bear plays honestly, fox gives a cheerful thumbs up. Glowing golden badge and heart particles, 14 seconds`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 🎲 1. 주사위 던지기 ] ➔ [ ⚖️ 2. 양심 저울 ] ➔ [ 🚶 3. 나온 대로 가기 ] ➔ [ 🤝 4. 정직한 하이파이브 ] ➔ [ 🎁 5. 보상 ]
```

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 몰래 주사위 돌리기
* **길이:** 10초 | **콘티:** 폭시가 물 마시는 사이에 코코가 주사위를 1에서 6으로 돌림. 폭시가 눈치채고 판을 접어버림. 속마음 `[💭 "거짓말쟁이랑은 안 놀아!"]` 😠.
* **AI 프롬프트:** `3D animated style. Bear flips dice secretly, fox notices and frowns angrily with a sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 1칸 가서 뱀을 타도 당당하게 웃기
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 1 나온 대로 말을 옮겨 뱀을 타고 내려감: "아이쿠! 하지만 다음엔 사다리 탈 거야!" 당당하게 웃음 ➔ 폭시가 "코코 최고!" 응원.
* **AI 프롬프트:** `3D animated style. Rewind effect. Bear moves 1 step honestly and laughs cheerfully. Fox smiles and cheers for the bear. 15 seconds`
* **전환 나레이션:** "정직하게 플레이하는 코코가 진짜 챔피언이에요! 이제 OO이 차례예요!" ➔ **Step 4 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 주사위 굴리기 (Roll the Dice)
* **화면 연출 (1인칭 POV):** 뱀사다리 게임판. 내 노란 말이 98번 칸에 있음. 100번이 결승선.
* **사건 발생:** 주사위를 굴렸는데 **'1'**이 나옴. 99번 칸은 거대한 뱀 머리가 있어서 20번 칸으로 미끄러지는 최악의 칸!
* **상황:** 친구 서준이가 마침 떨어진 물병을 줍느라 고개를 숙이고 있음.

### 🎬 Chapter 2: 속임수 충동과 양심 저울 (The Dilemma)
* **내면 충동:** "지금 주사위를 2로 살짝 뒤집으면 내가 1등으로 이기는데... 돌릴까?"
* **양심 저울 UI:** 화면 중앙에 [가짜 1등 ❌] vs [정직한 우정 ⭕] 저울 팝업.

### 🎬 Chapter 3: 1인칭 행동 선택 (Action Choice)
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ 🎲 정직하게 '1' 칸 가기 ]    |    |    [ 🤫 주사위 몰래 2로 돌리기 ]  |
  |  (뱀을 타고 내려가지만 당당하게)  |    |    서준이 몰래 1등 골인선 점프  |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[정직하게 1칸]` 선택 시 1인칭 손이 노란 말을 99번 뱀 머리 칸으로 옮김.

### 🎬 Chapter 4: 뱀 슬라이드 QTE (Slide Down with Smile)
* **화면 연출:** 말이 뱀을 타고 `슈우우웅-` 아래 20번 칸으로 미끄러져 내려감.
* **인터랙션:** 화면을 아래로 슥 밀며 "아이쿠 미끄러졌다!" 제스처 (Swipe Down).
* **내 멘트:** "아이쿠! 뱀을 탔네! 하지만 끝까지 따라잡을 거야!"

### 🎬 Chapter 5: 서준이의 감동 리액션 (Peer Trust)
* **화면 연출:** 고개를 든 서준이가 상황을 보고 감탄함: "우와, OO아! 너 뱀 칸인데도 안 속이고 그대로 갔구나? 너 진짜 멋있다!"
* **서준이 속마음:** `[💭 "OO이는 진짜 믿을 수 있는 최고의 친구야!"]` 😊 (`trust_rapport: 100`).

### 🎬 Chapter 6: 보상 획득 (Reward)
* **보상:** `[🛡️ 정직한 명예 게이머 황금 배지]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 게임 치팅 충동 시 [정직하게 플레이하기]         │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   아이가 지기 싫어서 룰을 어기려 할 때:                     │
│   👉 "규칙을 지키는 네가 백 배는 더 멋져! 정직이 1등이야!"   │
│      정직한 선택 자체를 극찬해 주세요.                       │
│                                                           │
│ 📱 잠금화면 큐카드: [1. 🎲 나온 대로 ➔ 2. 🤝 당당한 정직]   │
└───────────────────────────────────────────────────────────┘
```
