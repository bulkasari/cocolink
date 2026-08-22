# [풀 시나리오 명세] 09. 친구의 짓궂은 놀림에 쿨하게 대처하기
## : UCLA PEERS / Frankel & Wood Chapter 11 기반 놀림(Teasing) 무력화 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/09_놀림과_장난에_쿨하게_대처하기.md`  
> **원전 레퍼런스:** 《Social Skills Success for Students with Autism》 Chapter 11 (Preventing and Dealing with Victimization)  
> **에피소드 코드:** `CONTENT-09-COOL-TEASING-DEFENSE`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 놀림에 과민반응(비명/공격) 아동  
> **핵심 가치:** "놀리는 친구는 화내는 반응을 원해요! 어깨 으쓱 🤷 '그래서 뭐?' 쿨하게 넘기면 놀림이 끝나요!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🐺 **늑대 친구 '울피':** `Graphic/social/animation/wolf_kid_turnaround.png`
* 🏫 **[3D 유치원 신발장 복도 배경]:** `Graphic/social/animation/hallway_lockers_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '진우' (장난기 많은 7세 남아):** `Graphic/social/real/real_peer_jinwoo_turnaround.png`
* 🧦 **실사 짝짝이 양말 소품**
* 🏫 **[실사 유치원 신발장 복도 배경]:** `Graphic/social/real/real_hallway_shoes_bg.png`

---

## 🎬 STEP 1: Pre-Story (놀림의 비밀)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션

### 1-1. 짝짝이 양말과 놀림 (도입)
* **길이:** 8초 | **콘티:** 곰돌이 코코가 한쪽은 노란 양말, 한쪽은 파란 양말을 신고 옴. 늑대 울피가 손가락질하며 낄낄 웃음.
* **AI 프롬프트:** `3D cute animated style. A teddy bear wearing mismatched socks. A little mischievous wolf points finger and giggles playfully in a hallway. 8 seconds`

### 1-2. 화내면 더 놀려요 (갈등)
* **길이:** 8초 | **콘티:** 코코가 얼굴이 빨개져서 "놀리지 마!" 비명을 지르자, 울피가 신나서 더 크게 놀림.
* **AI 프롬프트:** `3D animated style. Bear yells with red angry face, wolf teases even louder with a big grin. Warning exclamation marks, 8 seconds`

### 1-3. 쿨가이 마법 방패 (해결책)
* **길이:** 14초 | **콘티:** 코코가 선글라스를 낀 쿨한 표정으로 어깨를 으쓱하며 "응, 짝짝이 유행이야~" 유유히 걸어가자, 울피가 시시해져서 장난을 멈춤.
* **AI 프롬프트:** `3D animated style. Bear puts on cool sunglasses, shrugs calmly and walks away peacefully. The wolf looks bored and stops teasing. Sparkling shield effect, 14 seconds`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 🧦 1. 놀림 발생 ] ➔ [ 💭 2. 속마음 간파 ] ➔ [ 🤷 3. 어깨 으쓱 ] ➔ [ 🚶 4. 쿨하게 퇴장 ] ➔ [ 🎁 5. 보상 ]
```

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 주먹 쥐고 소리 지르며 울기
* **길이:** 10초 | **콘티:** 코코가 울며 울피를 때리려다 선생님께 혼남. 속마음 `[💭 "화내니까 더 놀리고 싶다!"]` 😈.
* **AI 프롬프트:** `3D animated style. Bear cries and swings fists in anger. Wolf laughs mockingly. Sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 쿨하게 어깨 으쓱하고 지나가기
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 아무렇지 않게 "그래서 뭐? 짝짝이가 멋있는데?" 어깨를 으쓱하고 신발을 정리함 ➔ 울피가 시시해져서 가버림.
* **AI 프롬프트:** `3D animated style. Rewind effect. Bear calmly shrugs and says "So what?", putting shoes away peacefully. Wolf gets bored and walks away. 15 seconds`
* **전환 나레이션:** "코코가 놀림에 완벽하게 대처했어요! 이제 OO이 차례예요!" ➔ **Step 4 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 짓궂은 놀림 발생 (The Teasing Moment)
* **화면 연출 (1인칭 POV):** 신발장 앞. 친구 진우가 손가락질하며 낄낄거림.
* **진우 대사:** "푸하하! OO이 오늘 양말 색깔 짝짝이다! 양말도 제대로 못 신는 바보래요!"
* **내면 충동:** 얼굴이 화끈거리고 "바보 아니야!" 소리 지르고 싶은 충동 (`anger_spike: 80`).

### 🎬 Chapter 2: 놀림꾼의 속마음 간파 (See Through the Tease)
* **진우 머리 위 속마음 말풍선:** `[💭 "제발 화내고 소리 질러라! 그래야 더 재밌지!"]` 😈
* **나레이션:** "진우는 네가 화내기를 기다리고 있어요! 진우의 장난을 무력화하는 쿨한 방패를 켜볼까요?"

### 🎬 Chapter 3: 쿨한 대처 선택 (Choose Cool Response)
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ 😎 🤷 어깨 으쓱 "어쩌라고?" ]  |    |     [ 😡 😭 비명 지르며 때리기 ] |
  |  "짝짝이 양말이 유행이야~" 쿨하게 |    |    "너 죽을래?!" 멱살 잡고 울기  |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[어깨 으쓱]` 선택 시 1인칭 시점이 평온을 유지함.

### 🎬 Chapter 4: 어깨 으쓱 제스처 QTE (Shrug Gesture)
* **인터랙션 (Swipe Up):** 화면 양 어깨 아이콘을 위로 슥- 올리는 제스처!
* **내 음성:** "응, 짝짝이 양말이 요즘 유행이야. 그래서 뭐?"

### 🎬 Chapter 5: 쿨하게 신발 넣고 이동 (Walk Away)
* **화면 연출:** 신발을 신발장에 쏙 넣고 뒤돌아서 교실로 뚜벅뚜벅 걸어감.
* **진우의 반응:** 진우가 머리를 긁적이며 "어...? 재미없네..." 하고 딴 데로 가버림 (`teasing_immunity: 100`).

### 🎬 Chapter 6: 보상 획득 (Reward)
* **보상:** `[🛡️ 무적의 멘탈 수호자 황금 방패 배지]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 놀림 대처법 [어깨 으쓱 ➔ "그래서 뭐?" 쿨한 무시] │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   집에서 장난스러운 놀림 롤플레잉을 해보세요:               │
│   👉 부모가 "너 코딱지 같아!" 할 때 아이가 [어깨 으쓱 🤷]   │
│      하고 쿨하게 넘기는 연습을 반복시켜 주세요.              │
│                                                           │
│ 📱 잠금화면 큐카드: [1. 🤷 어깨 으쓱 ➔ 2. 😎 "그래서 뭐?" ➔ 3. 🚶 이동]│
└───────────────────────────────────────────────────────────┘
```
