# [풀 시나리오 명세] 02. 장난감 순서 정하기와 차례 지키기
## : Fast Track Session 14 & 15 기반 공정한 순서 결정 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/02_누가_먼저할지_공정하게_순서정하기.md`  
> **원전 레퍼런스:** 《Fast Track Friendship Group Manual》 Unit III, Session 14 (Deciding Who Goes First) & Session 15 (Taking Turns)  
> **에피소드 코드:** `CONTENT-02-DECIDING-TURNS`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 충동 조절 훈련 필요 아동  
> **핵심 가치:** "내가 먼저 하고 싶을 땐 소리 지르지 않고 가위바위보! 2번째 순서가 되어도 괜찮아요!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🦊 **여우 친구 '폭시':** `Graphic/social/animation/foxy_kid_turnaround.png`
* 🏫 **[3D 유치원 태블릿 게임존 배경]:** `Graphic/social/animation/game_room_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '현우' (장난기 있는 7세 남아):** `Graphic/social/real/real_peer_hyunwoo_turnaround.png`
* 📱 **실사 인터랙티브 태블릿 레이싱 게임 소품**
* 🏫 **[실사 유치원 자유놀이 매트 배경]:** `Graphic/social/real/real_kindergarten_mat_bg.png`

---

## 🎬 STEP 1: Pre-Story (누가 먼저 할까?)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션

### 1-1. 인기 많은 태블릿 게임기 (도입)
* **길이:** 8초 | **구도:** 3인칭 풀 샷
* **콘티:** 유치원 놀이방에 반짝반짝 빛나는 신형 공룡 레이싱 게임기가 1대 놓여 있음. 곰돌이 코코와 여우 폭시가 동시에 눈을 반짝이며 달려옴.
* **AI 프롬프트:**
  * **[영문]:** `3D cute animated style, Mario 3D World aesthetic. A glowing colorful toy arcade tablet on a table in a cozy kindergarten. A fluffy teddy bear and a cute little fox run toward it with excited sparkling eyes. 8 seconds`
  * **[한글]:** `3D 애니메이션 스타일. 아늑한 유치원 테이블 위에 반짝이는 장난감 게임기. 곰돌이와 작은 여우가 신나서 눈을 반짝이며 달려오는 장면, 8초`

### 1-2. 내가 1번이야! (갈등)
* **길이:** 8초 | **구도:** 3인칭 미디엄 샷
* **콘티:** 코코와 폭시가 서로 "내가 먼저!"라며 게임기 양쪽을 잡아당김. 화면이 흔들리며 게임기 화면이 꺼질 뻔함.
* **AI 프롬프트:**
  * **[영문]:** `3D animated style. The teddy bear and fox tug at the toy tablet from both sides with angry faces. Warning red sparkles. 8 seconds`
  * **[한글]:** `3D 애니메이션 스타일. 곰돌이와 여우가 화난 표정으로 태블릿 양쪽을 잡아당기는 모습. 빨간 경고 불꽃, 8초`

### 1-3. 가위바위보와 공정한 순서 (해결책)
* **길이:** 14초 | **구도:** 3인칭 풀 샷
* **콘티:** 선생님이 "가위바위보로 1번, 2번을 정해요!" 가이드 ➔ 폭시가 이겨서 먼저 하고, 코코가 모래시계를 보며 얌전히 기다린 뒤 번갈아 탐.
* **AI 프롬프트:**
  * **[영문]:** `3D animated style. The bear and fox play rock-paper-scissors cheerfully. The fox plays first while the bear happily watches a 3-second hourglass timer, then they switch turns smoothly with smiles. 14 seconds`
  * **[한글]:** `3D 애니메이션 스타일. 곰과 여우가 가위바위보를 하고, 여우가 먼저 하는 동안 곰이 모래시계를 보며 기다린 뒤 번갈아 즐겁게 게임을 하는 모습, 14초`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 📱 1. 게임 발견 ] ➔ [ ✌️ 2. 가위바위보 ] ➔ [ ⏳ 3. 3초 대기 ] ➔ [ 🎮 4. 내 차례! ] ➔ [ 🎁 5. 보상 ]
```

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 힘으로 뺏고 울기
* **길이:** 10초 | **콘티:** 코코가 게임기를 힘으로 빼앗아 도망치자 폭시가 엉엉 울고 게임기가 바닥에 떨어져 금이 감. 속마음 `[💭 "치사해! 다시는 너랑 안 놀아!"]` 😭.
* **AI 프롬프트:** `3D animated style. Teddy bear snatches tablet and runs away, fox cries. Sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 2번째 순서 씩씩하게 인정하기
* **길이:** 15초 | **콘티:** 가위바위보에서 진 코코가 "폭시 먼저 해! 다음은 내 차례지?" 하고 웃으며 옆에서 응원 ➔ 폭시가 1판 후 "코코야 이제 네 차례야!" 건넴.
* **AI 프롬프트:** `3D animated style. Bear accepts losing rock-paper-scissors with a smile, cheers for the fox, then happily receives the tablet for its turn. 15 seconds`
* **전환 나레이션:** "코코도 멋지게 순서를 지켰어요! 이제 OO이 차례예요!" ➔ **Step 4(1인칭 실사) 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 태블릿 게임기 잡기 (Reach for the Game)
* **화면 연출 (1인칭 POV):** 책상 위 신형 공룡 레이싱 태블릿. 내 1인칭 손과 친구(현우)의 손이 동시에 태블릿을 잡음.
* **현우 대사:** "내가 먼저 잡았어! 내가 1등으로 할 거야!"
* **인터랙션 (QTE):** 태블릿 손잡이 영역을 잡고 유지 (Hold 1초).

### 🎬 Chapter 2: 가위바위보 제안하기 (Propose RPS)
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ ✌️ ✊ 🖐️ "가위바위보 하자!" ]  |    |     [ 💥 힘으로 잡아당기기 ]     |
  |  "이긴 사람이 1번, 진 사람이 2번!" |    |    현우 손 쳐내고 뺏어 달아나기   |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[가위바위보 하자]` 선택 시 현우가 고개를 끄덕이며 "그래! 가위바위보 하자!" (`fair_selection: +30`).

### 🎬 Chapter 3: 가위바위보 미니게임 (Interactive RPS)
* **인터랙티브 UI:** 화면에 `[ ✊ 바위 ]`, `[ ✌️ 가위 ]`, `[ 🖐️ 보 ]` 버튼 팝업.
* **사운드:** 현우 목소리 "안 내면 진 거 가위 바위 보!"
* **결과:** 내가 🖐️(보)를 선택 ➔ 현우가 ✌️(가위)를 내서 **현우가 승리!**

### 🎬 Chapter 4: 2번째 순서 수용 및 3초 대기 (Hold 3-sec Countdown)
* **현우 대사:** "야호! 내가 이겼다! 나 먼저 1판 할게!"
* **내면 감정:** 살짝 아쉽지만 쿨하게 인정하는 순간.
* **인터랙션 (Hold QTE):**
  * 화면 중앙 3초 모래시계를 **3초간 길게 누르기(Hold)**.
  * `3... 2... 1...` 누르는 동안 현우가 자동차를 1바퀴 달리고 "야호! 골인!" 외침 (`second_turn_calmness: 100`).

### 🎬 Chapter 5: 내 차례 플레이 (My Turn Play)
* **화면 연출:** 현우가 약속대로 태블릿을 두 손으로 건넴: "OO아, 이제 네 차례야! 진짜 재밌어!"
* **인터랙션 (Swipe Race):** 화면의 레이싱 핸들을 좌우로 돌리며 코인을 먹고 골인선 통과!

### 🎬 Chapter 6: 칭찬 스탬프 및 보상 (Stamp & Reward)
* **화면 연출:** 현우와 양손 하이파이브!
* **보상:** 상단 5개 아이콘 체크(✅) 점등 + `[⚖️ 공정한 차례왕 황금 스탬프]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 순서 다툼 시 [가위바위보 ➔ 2번째 차례 인정]    │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   "내가 먼저 할 거야!" 소리 지를 때:                        │
│   👉 "소리 지르는 사람 안 줘요! 가위바위보로 1번 정하자!"    │
│      공정한 룰을 즉시 적용해 주세요.                        │
│                                                           │
│ 📱 잠금화면 큐카드: [1. ✌️✊🖐️ 가위바위보 ➔ 2. ⏳ 3초 대기]  │
└───────────────────────────────────────────────────────────┘
```
