# [풀 시나리오 명세] 06. 친구의 반어법(비꼬기)과 진짜 칭찬 구별하기
## : UCLA PEERS / Frankel & Wood Chapter 5 기반 비유어·풍자 감지 4-Step 풀 인터랙티브 에피소드

> **시나리오 매핑:** `Docs/Social/scenario/06_비꼬기와_진짜칭찬_구별하기.md`  
> **원전 레퍼런스:** 《Social Skills Success for Students with Autism》 Chapter 5 (Figurative Language, Irony, and Sarcasm)  
> **에피소드 코드:** `CONTENT-06-SARCASM-DETECTION`  
> **대상:** 3~9세 발달지연, 자폐스펙트럼(ASD), 문자 그대로 해석 경향 아동  
> **핵심 가치:** "상황과 반대로 말하는 늘어지는 말투는 비꼬는 장난! 화내지 않고 쿨한 유머로 넘겨요!"

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/social/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** `Graphic/social/animation/coco_bear_turnaround.png`
* 🦊 **여우 친구 '폭시':** `Graphic/social/animation/foxy_kid_turnaround.png`
* 🏃 **[3D 운동장 달리기 트랙 배경]:** `Graphic/social/animation/running_track_bg.png`

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/social/real/`)
* 👦 **실사 또래 친구 '태오' (장난기 많은 8세 남아):** `Graphic/social/real/real_peer_taeo_turnaround.png`
* 🏃 **실사 체육관 달리기 콘 및 바닥 소품**
* 🏫 **[실사 체육관 배경]:** `Graphic/social/real/real_gym_bg.png`

---

## 🎬 STEP 1: Pre-Story (말과 표정이 다를 때)

> **형식:** 30초 3인칭 3D 파스텔 톤 애니메이션

### 1-1. 달리기에서 넘어진 코코 (도입)
* **길이:** 8초 | **콘티:** 코코 곰돌이가 달리기 시합 중 발이 엉켜 털썩 넘어짐. 꼴찌로 결승선에 들어옴.
* **AI 프롬프트:** `3D cute animated style. A chubby teddy bear stumbles and falls clumsily on a running track, crossing the finish line last. 8 seconds`

### 1-2. 폭시의 늘어지는 말투 (갈등)
* **길이:** 8초 | **콘티:** 여우 폭시가 눈을 위로 굴리며 "우~~와~~ 너 진짜 번개처럼 빠르다~~" 과장되게 말함. 코코가 혼란스러워함.
* **AI 프롬프트:** `3D animated style. Little fox rolls eyes with arms crossed, speaking in an exaggerated sarcastic manner. Teddy bear looks confused with question marks. 8 seconds`

### 1-3. 비꼬기 감지와 쿨한 유머 (해결책)
* **길이:** 14초 | **콘티:** 코코가 상황과 반대임을 눈치채고 "하하! 넘어지는 건 내가 1등이었지?" 어깨를 으쓱하자, 폭시가 씩 웃으며 손을 잡고 일으켜 세워줌.
* **AI 프롬프트:** `3D animated style. Teddy bear shrugs coolly with a playful smile. Fox laughs and helps the bear stand up. Bright sparkles, 14 seconds`

---

## 🧭 STEP 2: Visual Schedule (상시 5단계 일정표 HUD)

```
[ 🏃 1. 달리기 ] ➔ [ ⚡ 2. 비꼬기 감지 ] ➔ [ 💭 3. 속마음 확인 ] ➔ [ 😎 4. 쿨한 유머 ] ➔ [ 🎁 5. 보상 ]
```

---

## 🎬 STEP 3: Model-First (코코의 대비 모델링)

### 3-1. [서툰 행동]: 문자 그대로 믿거나 주먹 쥐고 화내기
* **길이:** 10초 | **콘티:** 코코가 "나 안 빠른데 왜 놀려!" 하고 소리 지르며 폭시를 밀침. 속마음 `[💭 "장난친 건데 왜 때려..."]` 🥺.
* **AI 프롬프트:** `3D animated style. Bear yells angrily and pushes the fox. Fox looks shocked with a sad thought bubble. 10 seconds`

### 3-2. [올바른 행동]: 어깨 으쓱하며 쿨하게 맞받아치기
* **길이:** 15초 | **콘티:** 리와인드 후 코코가 능청스럽게 어깨를 으쓱하며 "그러게, 슬라이딩 1등이지?" ➔ 폭시가 "크큭, 안 다쳤냐?" 하며 하이파이브.
* **AI 프롬프트:** `3D animated style. Rewind effect. Bear shrugs with a cool smile and humorous remark. Fox laughs and high-fives. 15 seconds`
* **전환 나레이션:** "코코가 비꼬는 장난을 쿨하게 넘겼어요! 이제 OO이 차례예요!" ➔ **Step 4 전환!**

---

## 🎬 STEP 4: Interactive POV Simulation (1인칭 실사 6개 챕터 풀 체험)

### 🎬 Chapter 1: 달리기 실패 상황 (The Fall)
* **화면 연출 (1인칭 POV):** 체육관 매트. 달리다가 털썩 주저앉아 꼴찌로 들어옴.
* **친구 태오의 표정과 대사:**
  * 태오가 팔짱을 끼고 눈을 위로 굴리며(Eye-roll) 씩 웃음.
  * 과장된 말투 음성: "우~~와~~ 너 진짜 우사인 볼트처럼 빠르다~~"

### 🎬 Chapter 2: 비꼬기 레이더 작동 (Sarcasm Radar)
* **나레이션:** "잠깐! 태오의 말과 상황이 반대예요! 태오의 진짜 속마음은 무엇일까요?"
* **인터랙션 (Sarcasm Tap):**
  * 화면 중앙의 `[ ⭕ 진짜 칭찬 ]` vs `[ ⚡ 비꼬는 장난 (Sarcasm) ]` 중 **[비꼬는 장난 ⚡]** 탭!
  * 태오 속마음 팝업: `[💭 "넘어진 게 웃겨서 반대로 장난친 거야!"]` 😜 (`sarcasm_detection_accuracy: 100`).

### 🎬 Chapter 3: 쿨한 대처 선택하기 (Cool Response Choice)
* **PECS 카드 선택:**
  ```
  +----------------------------------+    +----------------------------------+
  |    [ 😎 🤷 쿨하게 인정 & 유머 ]   |    |     [ 😡 소리 지르며 때리기 ]    |
  |  "하하, 넘어지는 건 1등이었지?"   |    |    "나 안 빠른데 왜 놀려!" 주먹 |
  +----------------------------------+    +----------------------------------+
  ```
* **결과 연출:** `[쿨하게 인정]` 선택 시 1인칭 손이 바지를 툭툭 털며 능청스럽게 대답함.

### 🎬 Chapter 4: 어깨 으쓱 제스처 QTE (Shrug QTE)
* **인터랙션:** 화면의 양 어깨 아이콘을 위로 슥- 올리는 제스처 (Swipe Up).
* **내 음성:** "하하, 슬라이딩하는 건 내가 1등이었지?"

### 🎬 Chapter 5: 태오의 리액션 (Peer Reaction)
* **화면 연출:** 태오가 당황하다가 씩 웃으며 손을 내밂: "크큭, 그러게! 안 다쳤냐? 털고 일어나라!"
* **인터랙션:** 태오의 손을 잡고 벌떡 일어나기.

### 🎬 Chapter 6: 보상 획득 (Reward)
* **보상:** `[🎭 화용 언어 마스터 탐정 배지]` 획득!

---

## 📱 STEP 5: Home Bridge Card (보호자 실전 카드)

```
┌───────────────────────────────────────────────────────────┐
│              🏠 CocoLink Social 홈 브릿지 실전 카드         │
├───────────────────────────────────────────────────────────┤
│ [학습 주제] 비꼬기/반어법 시 [어깨 으쓱 ➔ 쿨한 유머 대처]   │
│                                                           │
│ 📌 보호자 코칭 멘트:                                       │
│   "말투가 길게 늘어지고 상황과 반대면 [장난]이야!           │
│   👉 화내지 말고 '그러게 말이야~' 하고 쿨하게 넘기자!"     │
│                                                           │
│ 📱 잠금화면 큐카드: [1. ⚡ 반어법 감지 ➔ 2. 🤷 어깨 으쓱 ➔ 3. 😎 쿨]│
└───────────────────────────────────────────────────────────┘
```
