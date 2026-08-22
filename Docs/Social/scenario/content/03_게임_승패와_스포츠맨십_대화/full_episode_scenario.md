# [풀 시나리오 명세] 03. 게임 승패와 스포츠맨십 대화
## : Fast Track Session 16 기반 승자의 겸손과 패자의 품격 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/03_이겼을때_졌을때_스포츠맨십.md`  
> **원전 레퍼런스:** 《Fast Track Friendship Group Manual》 Unit IV, Session 16 (Good Things to Say When You Win or Lose)  
> **에피소드 코드:** `CONTENT-03-SPORTSMANSHIP`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 승패 집착 및 패배 분노 아동  
> **핵심 가치:** "이겼을 땐 '너도 잘했어!' 겸손하게, 졌을 땐 '축하해!' 씩씩하게!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🐰 **토끼 친구 '로미':** `Graphic/social/animation/romi_rabbit_turnaround.png`
* 🎲 **[3D 주사위 보드게임 테이블 배경]:** `Graphic/social/animation/boardgame_table_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '민재' (순수한 7세 남아):** `Graphic/social/real/real_peer_minjae_turnaround.png`
* 🎲 **실사 보드게임판 및 알록달록 말/주사위 소품**
* 🏫 **[실사 유치원 교실 보드게임 책상 배경]:** `Graphic/social/real/real_classroom_table_bg.png`

---

## 🎬 STEP 1: Pre-Story (게임은 즐거운 친구예요)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션

### 1-1. 신나는 주사위 보드게임 (도입)
* **길이:** 8초 | **구도:** 3인칭 풀 샷
* **콘티:** 곰돌이 코코와 토끼 로미가 마주 앉아 동물 주사위 보드게임을 함. 서로 주사위를 굴리며 까르르 웃음.
* **AI 프롬프트:**
  * **[영문]:** `3D cute animated style. A chubby teddy bear and cute white rabbit sitting across a colorful board game table, taking turns rolling a big soft dice with joyful smiles. Bright cozy classroom, 8 seconds`
  * **[한글]:** `3D 귀여운 애니메이션 스타일. 통통한 아기 곰돌이와 귀여운 흰 토끼가 알록달록한 보드게임 테이블에 마주 앉아 큰 주사위를 굴리며 즐겁게 웃는 장면, 8초`

### 1-2. 이겼을 때와 졌을 때 (갈등)
* **길이:** 8초 | **구도:** 3인칭 미디엄 샷
* **콘티:** 로미가 이겼을 때 코코가 보드판을 엎어버리거나, 코코가 이겼을 때 "메롱 너 졌지!" 놀려서 로미가 우는 나쁜 예시.
* **AI 프롬프트:**
  * **[영문]:** `3D animated style. One character teasing the other with tongue out, the other crying with a flipped game board. Sad warning atmosphere, 8 seconds`
  * **[한글]:** `3D 애니메이션 스타일. 한 캐릭터가 혀를 내밀고 메롱 놀리고, 다른 캐릭터는 엎어진 보드판 앞에서 울고 있는 아쉬운 장면, 8초`

### 1-3. 멋진 스포츠맨의 말 (해결책)
* **길이:** 14초 | **구도:** 3인칭 클로즈업 ➔ 풀 샷
* **콘티:** 코코가 이겼을 때 "너도 진짜 잘했어!" 손을 내밀고, 졌을 때 "축하해! 한 판 더 하자!" 웃으며 하이파이브.
* **AI 프롬프트:**
  * **[영문]:** `3D animated style. Teddy bear and rabbit smiling warmly, shaking hands and high-fiving after a game. Glowing trophy and heart icons, cheerful celebration, 14 seconds`
  * **[한글]:** `3D 애니메이션 스타일. 곰돌이와 토끼가 따뜻하게 웃으며 게임 후 악수하고 하이파이브함. 빛나는 트로피와 하트 아이콘, 14초`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 🎲 1. 주사위 굴리기 ] ➔ [ 🏁 2. 결승선 도착 ] ➔ [ 🗣️ 3. 멋진 멘트 ] ➔ [ 🤝 4. 하이파이브 ] ➔ [ 🎁 5. 보상 ]
```

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 졌다고 보드판 엎기
* **길이:** 10초 | **콘티:** 코코가 게임에서 지자 "으앙!" 소리 지르며 말을 던져버림. 로미가 깜짝 놀라 굳음. 속마음 `[💭 "무서워... 코코랑 게임 안 할래"]` 😨.
* **AI 프롬프트:** `3D animated style. Teddy bear flips board game pieces in anger. Rabbit looks scared with sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 손뼉 치며 "축하해!" 말하기
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 숨을 `후-` 쉬고 손뼉을 치며 "로미야 축하해! 다음 판은 내가 이긴다!" 웃음 ➔ 로미가 기뻐하며 주사위를 건넴.
* **AI 프롬프트:** `3D animated style. Rewind effect. Teddy bear takes a deep breath, claps hands, and says congratulations to the rabbit with a big smile. 15 seconds`
* **전환 나레이션:** "코코도 멋진 스포츠맨이 되었어요! 이제 OO이 차례예요!" ➔ **Step 4 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 주사위 굴리기 (Roll the Dice)
* **화면 연출 (1인칭 POV):** 테이블 위 동물 보드게임판. 내 말(노란 곰)과 친구 민재의 말(파란 토끼)이 결승선 앞에 있음.
* **인터랙션 (QTE):** 화면의 빨간 주사위를 터치하여 흔들고 던지기 (Shake & Tap).
* **결과 연출:** 주사위가 데굴데굴 굴러 **'5'**가 나옴! 내 노란 말이 결승선에 먼저 쏙 들어감!

### 🎬 Chapter 2: 내가 이겼을 때의 선택 (I Won! - Good Winner)
* **화면 연출:** 민재가 시무룩한 표정으로 입술을 삐죽이며 고개를 숙임.
* **민재 속마음:** `[💭 "나도 이기고 싶었는데... 창피해"]` 🥺
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |  [ 🤝 👍 "민재야 너도 잘했어!" ]  |    |     [ 😝 "메롱! 너 완전 졌지?" ]  |
  |  "아슬아슬해서 진짜 재밌었어!"   |    |    민재 얼굴 앞에서 춤추며 놀리기 |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[너도 잘했어]` 선택 시 민재의 어깨를 툭 치며 하이파이브 ➔ 민재가 부끄럽게 웃으며 "고마워! 너 진짜 잘하더라!" 답함 (`sportsmanship_score: +50`).

### 🎬 Chapter 3: 2회차 게임 시작 (Game 2)
* **화면 연출:** 민재가 주사위를 굴림. '6'이 나오며 이번엔 민재의 파란 토끼 말이 결승선에 먼저 쏙 들어감!
* **민재 대사:** "야호! 이번엔 내가 이겼다!"

### 🎬 Chapter 4: 내가 졌을 때의 쿨다운 (I Lost! - Calming)
* **내면 감정:** 순간 가슴이 쿵 내려앉고 눈물이 날 것 같음.
* **진정 인터랙션:** 화면의 풍선을 1번 탭하며 `후-` 깊게 숨 내쉬기 (Calm Breath).

### 🎬 Chapter 5: 졌을 때 씩씩하게 축하하기 (Good Loser)
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ 👏 🏆 "민재야 축하해!" ]      |    |     [ 💥 보드판 뒤엎기 ]         |
  |  "축하해! 다음 판은 내가 이긴다!"|    |    보드판 집어 던지고 울기       |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[축하해]` 선택 시 두 손으로 짝짝 박수를 치며 "민재야 축하해!" 외침 ➔ 민재가 "고마워! 너랑 게임하니까 진짜 재밌다! 한 판 더 하자!" 주사위를 건넴 (`sportsmanship_score: 100`).

### 🎬 Chapter 6: 보상 획득 (Reward)
* **보상:** 상단 5개 아이콘 체크(✅) 점등 + `[🏆 황금 스포츠맨십 트로피 배지]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 게임 승패 시 [이겼을 땐 격려, 졌을 땐 축하]    │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   게임이 끝났을 때 승패와 상관없이 먼저 손을 내밀며:       │
│   👉 "Good Game! 진짜 멋진 승부였어!"라고 하이파이브를 유도!│
│                                                           │
│ 📱 잠금화면 큐카드: [1. 🤝 "너도 잘했어" ➔ 2. 👏 "축하해!"]  │
└───────────────────────────────────────────────────────────┘
```
