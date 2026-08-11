# [시나리오 마스터 명세] CocoLink: 소아과 병원 적응 4단계 풀 시나리오
## : 마스터 기획서(cocolink_hospital_master_spec.md) 기반 4-Step 통합 시나리오

> **대상:** 자폐스펙트럼(ASD), 발달지연, 무언어/언어지연, 사회불안이 높은 유아·아동 (3~9세)  
> **핵심 원칙:** 3인칭 개념 학습(Pre-Story) ➔ 시각적 일정 안내(Visual Schedule) ➔ 3인칭 관찰(Model-First) ➔ 1인칭 실사 인터랙션(Interactive Simulation)

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

> **💡 영상/이미지 AI 생성 시 사용할 3D 애니메이션 & 실사 레퍼런스 이미지 분리 구조:**

### 1. 🎬 Step 1 ~ Step 3 전용 (3D 애니메이션 스타일: `Graphic/hospital/animation/`)
* 🐻 **아기 곰돌이 '코코' (주인공):** [`Graphic/hospital/animation/coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/coco_bear_character_turnaround.png)
* 🐻 **엄마 곰돌이 '엄마 코코':** [`Graphic/hospital/animation/mother_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/mother_bear_character_turnaround.png)
* 👨‍⚕️ **의사 곰돌이 '드림 선생님':** [`Graphic/hospital/animation/doctor_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/doctor_bear_character_turnaround.png)
* 🐰 **간호사 토끼 '분홍이':** [`Graphic/hospital/animation/nurse_rabbit_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/nurse_rabbit_character_turnaround.png)
* 🏥 **[입구] 3D 외관:** [`Graphic/hospital/animation/hospital_exterior_background.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/hospital_exterior_background.png)
* 📋 **[접수/대기실] 3D 대기실:** [`Graphic/hospital/animation/reception_waiting_background.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/reception_waiting_background.png)
* 🚪 **[복도] 3D 복도:** [`Graphic/hospital/animation/clinic_hallway_background.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/clinic_hallway_background.png)
* 🩺 **[진료실] 3D 진료실:** [`Graphic/hospital/animation/doctor_room_background.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/animation/doctor_room_background.png)

### 2. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/hospital/real/`)
* 👨‍⚕️ **실사 의사 선생님:** [`Graphic/hospital/real/real_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_turnaround.png)
* 👩‍⚕️ **실사 간호사 선생님:** [`Graphic/hospital/real/real_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_nurse_turnaround.png)
* 🏥 **[입구] 실사 외관:** [`Graphic/hospital/real/real_hospital_exterior.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_hospital_exterior.png)
* 📋 **[접수/대기실] 실사 대기실:** [`Graphic/hospital/real/real_reception_waiting.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_reception_waiting.png)
* 🚪 **[복도] 실사 복도:** [`Graphic/hospital/real/real_clinic_hallway.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_clinic_hallway.png)
* 🩺 **[진료실] 실사 진료실:** [`Graphic/hospital/real/real_doctor_room.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_room.png)

---

## 🎬 STEP 1: Pre-Story (병원은 안전한 곳이에요)

> **목적:** 병원이 어떤 곳인지 전혀 모르는 아이에게 "왜 가야 하는지", "누가 있는지" 3인칭 동화로 사전 개념 형성.  
> **형식:** 30초 3인칭 2D/3D 부드러운 파스텔 톤 애니메이션

### 1-1. 기침과 열 (아픈 상태 이해)
* **참조 캐릭터:** 🐻 [`coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/coco_bear_character_turnaround.png), 🐻 [`mother_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/mother_bear_character_turnaround.png)
* **길이:** 8초 | **구도:** 3인칭 풀 샷
* **콘티:** 곰돌이 캐릭터 '코코'가 콜록콜록 기침을 하며 이마에 빨간 열 아이콘이 뜸. 엄마 곰돌이가 다정하게 안아주며 "열이 나네? 의사 선생님 만나러 가자!" 하고 말함.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D cute pastel animated style, a fluffy young teddy bear coughing with a glowing red fever icon above its head. A warm mother bear gently hugs the young bear. Cute friendly cartoon style, soft pastel lighting, 8 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `3D 귀여운 파스텔 애니메이션 스타일. 머리 위에 빛나는 빨간 열 아이콘이 뜬 채 콜록콜록 기침하는 푹신한 아기 곰돌이. 따뜻한 엄마 곰돌이가 아기 곰돌이를 다정하게 안아줌. 귀엽고 친근한 카툰 스타일, 부드러운 파스텔 조명, 8초`

### 1-2. 병원 건물의 모습 (장소 인지)
* **참조 이미지:** 🏥 [`hospital_exterior_background.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital_exterior_background.png), 👨‍⚕️ [`doctor_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_bear_character_turnaround.png), 🐰 [`nurse_rabbit_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/nurse_rabbit_character_turnaround.png)
* **길이:** 8초 | **구도:** 3인칭 와이드 샷
* **콘티:** 알록달록한 동물이 그려진 소아과 병원 건물 전경. 유리 자동문이 열리고, 의사와 간호사 캐릭터가 손을 흔들며 환하게 웃음.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D cute animated style, exterior of a colorful cheerful pediatric clinic building with cute animal wall paintings. Automatic glass doors open smoothly. A friendly male doctor and female nurse wave hands happily at the entrance. Warm welcoming atmosphere, 8 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `3D 귀여운 애니메이션 스타일. 귀여운 동물 벽화가 그려진 알록달록하고 화사한 소아과 병원 건물 외관. 유리 자동문이 부드럽게 열림. 입구에서 친근한 남성 의사와 여성 간호사가 기쁘게 손을 흔듦. 따뜻하게 환영하는 분위기, 8초`

### 1-3. 의사 선생님은 친구예요 (안전감 형성)
* **참조 이미지:** 🩺 [`doctor_room_background.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_room_background.png), 👨‍⚕️ [`doctor_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_bear_character_turnaround.png), 🐻 [`coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/coco_bear_character_turnaround.png)
* **길이:** 14초 | **구도:** 3인칭 미디엄 샷
* **콘티:** 의사 선생님이 청진기로 곰돌이의 가슴 소리를 듣고, 칭찬 스티커를 주며 웃음. "의사 선생님은 우리 아픈 곳을 낫게 해주는 친절한 친구예요!" 나레이션.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D animated style, a kind male doctor bear gently listening to a young teddy bear's chest with a stethoscope. The doctor smiles warmly and gives a shiny star sticker. Cute comforting animation, 14 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `3D 애니메이션 스타일. 친절한 남성 의사 곰돌이가 청진기로 아기 곰돌이의 가슴 소리를 부드럽게 듣는 장면. 의사가 따뜻하게 웃으며 반짝이는 별 스티커를 줌. 귀엽고 안심시키는 애니메이션, 14초`

---

## 🎨 STEP 2: Visual Schedule (오늘의 순서 카드 UI)

> **목적:** 아이에게 "언제 집에 가는지" 전체 진행 과정을 상시 아이콘으로 보여주어 불안 차단.

### 2-1. 상단 일정표 UI 구성 (HUD)
```
[ 🏥 1. 입구 ] ➔ [ 📋 2. 접수 ] ➔ [ 🩺 3. 진료 ] ➔ [ 💉 4. 주사 ] ➔ [ 🎁 5. 보상 ]
```
* **동작 규칙:**
  * 진행 중인 단계: 반짝이는 하이라이트 + 통둥통둥 애니메이션
  * 완료된 단계: 초록색 체크 표시(✅)로 전환
  * 무언어 모드(모드 B): 그림 아이콘 강조 (글자 최소화)

---

## 🎬 STEP 3: Model-First (곰돌이의 병원 체험 관찰)

> **목적:** 관찰 학습(Modeling)을 통해 실제 기구 검사 및 진료 과정을 3인칭 3D 애니메이션으로 먼저 보여주어 공포 완화.  
> **형식:** 3인칭 3D 캐주얼 애니메이션 (Step 1과 동일한 그래픽 스타일)

### 3-1. 곰돌이 진료실 입장
* **참조 이미지:** 🩺 [`doctor_room_background.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_room_background.png), 👨‍⚕️ [`doctor_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_bear_character_turnaround.png), 🐻 [`coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/coco_bear_character_turnaround.png)
* **길이:** 10초 | **콘티:** 아기 곰돌이 '코코'가 진료실 의자에 앉음. 의사 곰돌이 '드림 선생님'이 다정하게 인사하고 코코 귀를 가볍게 만져줌.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D casual animated style, Mario 3D World aesthetic, smooth toy-like vinyl texture. A kind doctor bear in white coat sitting a cute chubby teddy bear Coco on a clinic chair, gently touching its ear with a warm smile. Cozy animated pediatric doctor room background, 10 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `3D 캐주얼 애니메이션 스타일 (마리오 3D 월드 감성, 매끈한 장난감 비닐 질감). 흰 가운의 친절한 의사 곰돌이가 귀여운 아기 곰돌이 코코를 진료실 의자에 앉히고, 귀를 부드럽게 만져주며 따뜻하게 미소 지음. 아늑한 3D 소아과 진료실 배경, 10초`

### 3-2. 곰돌이 청진기 & 이경 검사
* **참조 이미지:** 🩺 [`doctor_room_background.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_room_background.png), 👨‍⚕️ [`doctor_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_bear_character_turnaround.png), 🐻 [`coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/coco_bear_character_turnaround.png)
* **길이:** 15초 | **콘티:** 의사 곰돌이가 코코 가슴에 청진기를 대고 "차갑지 않지? 간지럽지?" 하며 웃음. 귀를 이경으로 살짝 비춰봄. 코코가 가만히 잘 참음.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D casual animated style, Mario 3D World aesthetic. A friendly doctor bear placing a toy dinosaur stethoscope on teddy bear Coco's chest with a playful smile, then gently shining a light into its ear with an otoscope. Warm 3D clinic background, 15 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `3D 캐주얼 애니메이션 스타일. 친근한 의사 곰돌이가 장난스러운 미소로 공룡 장난감 청진기를 곰돌이 코코 가슴에 대고, 이어서 이경으로 귀 안에 부드럽게 빛을 비춰봄. 코코가 가만히 잘 참음. 따뜻한 3D 진료실 배경, 15초`

### 3-3. 곰돌이 칭찬 스티커 획득
* **참조 이미지:** 🩺 [`doctor_room_background.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_room_background.png), 👨‍⚕️ [`doctor_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/doctor_bear_character_turnaround.png), 🐻 [`coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/coco_bear_character_turnaround.png)
* **길이:** 20초 | **콘티:** 의사 곰돌이가 "우와! 코코 정말 용감하다!" 하고 별 스티커를 코코 이마에 붙여줌. 코코가 기뻐하며 엄지척!
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `3D casual animated style, Mario 3D World aesthetic. A joyful doctor bear placing a shiny star reward sticker on teddy bear Coco's forehead and giving a thumbs up. Cute celebration animation, bright colors, 20 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `3D 캐주얼 애니메이션 스타일. 기쁜 의사 곰돌이가 곰돌이 코코 이마에 반짝이는 별 보상 스티커를 붙여주고 엄지척을 해줌. 코코가 기뻐함. 귀여운 축하 애니메이션, 화사한 색감, 20초`
* **전환 나레이션:** "곰돌이도 해냈어요! 이제 OO이 차례예요! 준비됐나요?" ➔ **Step 4(1인칭 실사)로 전환!**

---

## 🎬 STEP 4: Interactive Simulation (1인칭 실사 6개 챕터 체험)

> **목적:** 실제 소아과 1인칭 POV 실사 비디오로 직접 선택하고 탭하며 병원 순응 학습.  
> **인터랙션 피처:** PECS 그림 카드 선택지 + 사전 감각 예고 (❄️차갑다! / 💡반짝! / 🌵따끔!)

---

### 📍 챕터 1: 병원 도착 & 입구

* **[일정표 상태]:** `[ 🏥 1. 입구 ]` 하이라이트

#### 🎬 C1_Arrive — 병원 입구 도착 (5초)
* **참조 이미지:** 🏥 [`real_hospital_exterior.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_hospital_exterior.png), 👩‍⚕️ [`real_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_nurse_turnaround.png)
* **카메라 워크:** Slow Dolly-In (1인칭 아이 눈높이 전진)
* **콘티:** 자동문이 열리고 파스텔 핑크 스크럽의 간호사 선생님이 접수대 너머에서 손을 흔듦.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV child's eye level, slow dolly-in movement approaching warm Korean pediatric clinic entrance. Automatic glass doors slide open revealing cheerful interior. Friendly female nurse in pastel pink scrubs behind reception desk smiles warmly and waves hand directly at camera. Photorealistic cinematic quality, warm soft lighting, 16:9, 5 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `아이 눈높이 1인칭 POV. 카메라가 천천히 앞으로 이동하며 밝고 따뜻한 한국 소아과 병원 입구로 다가가는 장면. 유리 자동문이 열리며 화사한 실내가 보임. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 접수대 너머에서 따뜻하게 웃으며 카메라를 정면으로 바라보고 손을 흔들어 환영함. 실사 영화 화질, 따뜻한 조명, 5초`

* **선택지 (PECS 그림 카드):**
  * **[모드 A (경증)]**: `[👋 인사하기]` / `[😶 가만히]` / `[🙈 숨기]`
  * **[모드 B (무언어)]**: `[👋 인사하기]` / `[🤝 손잡기]` (2개로 제한)

* **분기 클립:**
  * `C1_HiPath` (3초): 간호사 엄지척 ("어서 와~!") | Static Shot
    * **[영문]:** `First-person POV static shot, friendly Korean female pediatric nurse giving big warm smile and thumbs up directly at camera lens, photorealistic, 3s`
    * **[한글]:** `1인칭 시점 고정 샷. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 카메라 렌즈를 정면으로 바라보며 환하게 웃고 엄지척을 선명하게 보여주는 장면. 실사 화질, 3초`
  * `C1_HidePath` (3초): 간호사가 곰돌이 인형을 보여줌 ("괜찮아~") | Static Shot
    * **[영문]:** `First-person POV static shot, kind Korean female nurse pulling out soft teddy bear plush toy from below frame presenting it toward camera lens with patient warm smile, photorealistic, 3s`
    * **[한글]:** `1인칭 시점 고정 샷. 파스텔 핑크 스크럽의 친절한 한국인 여성 간호사가 화면 아래에서 부드러운 곰돌이 인형을 꺼내 카메라 렌즈 방향으로 내밀며 인내심 있고 따뜻한 미소로 안심시키는 장면. 실사 화질, 3초`

---

### 📍 챕터 2: 접수 & 대기실

* **[일정표 상태]:** `[ 📋 2. 접수 ]` 하이라이트

#### 🎬 C2_Reception — 접수 창구 (5초)
* **참조 이미지:** 📋 [`real_reception_waiting.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_reception_waiting.png), 👩‍⚕️ [`real_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_nurse_turnaround.png)
* **카메라 워크:** Static Eye-Level
* **콘티:** 간호사 선생님이 클립보드를 들고 "이름이 뭐예요?" 물어보며 진료 카드를 건넴.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV at child's eye level, static camera shot, a friendly Korean female nurse behind a bright reception counter leans slightly forward directly toward the camera with a warm smile asking "What's your name?", holding clipboard, handing over a small clinic card toward the camera lens. Eye contact with camera, cozy warm pediatric reception area background, photorealistic cinematic, 5 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `아이 눈높이 1인칭 시점. 고정 카메라 샷. 밝은 접수 창구 너머의 친근한 한국인 여성 간호사가 카메라 쪽으로 직접 몸을 기울이며 따뜻하게 웃으며 "이름이 뭐예요?" 하고 묻고 진료 카드를 카메라 렌즈 쪽으로 건네주는 장면. 카메라와 눈맞춤. 따뜻하고 아늑한 소아과 접수실 배경. 실사 영화 화질, 5초`
* **인터랙션 (PECS):** `[🗣️ 이름 말하기]` 또는 `[🤐 고개 끄덕이기]` 그림 카드 탭

#### 🎬 C2_WaitingRoom — 대기실 탐색 (6초)
* **참조 이미지:** 📋 [`real_reception_waiting.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_reception_waiting.png)
* **카메라 워크:** Slow Pan Left-to-Right
* **콘티:** 알록달록 대기실 둘러보기.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV seated eye level, slow pan left to right exploring a cozy colorful Korean pediatric waiting room. Camera slowly pans revealing: fish tank with swimming fish on left, small bookshelf with picture books center, colorful children's chairs in foreground. Natural warm lighting, calm welcoming atmosphere, photorealistic cinematic, 6 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점. 앉은 눈높이. 카메라가 왼쪽에서 오른쪽으로 느리게 패닝하며 아늑하고 알록달록한 한국 소아과 대기실을 탐색. 어항, 그림책 책장, 색깔 의자 순서대로 보임. 따뜻한 자연 채광, 실사 영화 화질, 6초`
* **탐색 미션 (터치):** 🐟 어항 물고기 / 📚 그림책 / ⏰ 시계 중 1개 이상 터치 ➔ "조금만 기다리면 돼!"

---

### 📍 챕터 3: 이름 호명 & 복도 이동

#### 🎬 C3_NameCall — 이름 호명 & 복도 걷기 (5초)
* **참조 이미지:** 🚪 [`real_clinic_hallway.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_clinic_hallway.png), 👩‍⚕️ [`real_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_nurse_turnaround.png)
* **카메라 워크:** Hold ➔ Dolly-In Walk
* **콘티:** 간호사 선생님이 진료실 문 앞에서 이름을 부름. 복도를 타고 진료실로 다가가는 POV 이동.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV at child's eye level. Camera holds still as a friendly Korean female nurse in pink scrubs stands at an open clinic room door smiling and beckoning gently toward the camera. Then camera begins a slow steady dolly-in walking forward down a bright clean corridor toward the open room door, warm pediatric clinic interior, photorealistic, 5 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `아이 눈높이 1인칭 시점. 파스텔 핑크 스크럽의 친근한 한국인 간호사가 열린 진료실 문 앞에서 카메라를 향해 따뜻하게 웃으며 손짓으로 안내. 이어서 카메라가 밝고 깨끗한 복도를 따라 진료실 문 쪽으로 천천히 안정적으로 달리인 POV 이동. 따뜻한 소아과 실내, 실사 화질, 5초`

---

### 📍 챕터 4: 진료실 입장 & 의사 인사

* **[일정표 상태]:** `[ 🩺 3. 진료 ]` 하이라이트

#### 🎬 C4_DoctorGreet — 의사 인사 & 자리 안내 (5초)
* **참조 이미지:** 🩺 [`real_doctor_room.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_room.png), 👨‍⚕️ [`real_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_turnaround.png)
* **카메라 워크:** Dolly-In Reveal ➔ Static
* **콘티:** 진료실 문이 열리고 둥근 안경과 흰 가운의 의사 선생님이 정면 카메라를 보고 환하게 인사. "어서 와~ 의자에 앉아볼까?"
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV, camera slowly pushes forward as a clinic room door opens revealing a warm bright Korean pediatric exam room interior. A friendly Korean male pediatrician in his late 30s with round glasses and white lab coat looks directly into the camera lens with a warm smile and waves hello at the camera. Camera settles to static shot as he gently points to a child's seat. Eye contact with camera, photorealistic cinematic video, 5 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점. 진료실 문이 열리면서 카메라가 앞으로 밀고 들어가 따뜻한 소아과 진료실 내부가 드러남. 둥근 안경과 흰 가운의 친근한 한국인 남성 소아과 의사가 카메라 렌즈를 정면으로 바라보며 환하게 웃고 손을 흔들어 인사. 카메라가 고정되며 의사가 아동 의자를 손으로 가리킴. 카메라와 눈맞춤. 실사 영화 화질, 5초`

---

### 📍 챕터 5: 진료 과정 (선택 검사 및 주사)

#### 5-A: 신뢰 루트 (기구 검사)
* **참조 이미지:** 🩺 [`real_doctor_room.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_room.png), 👨‍⚕️ [`real_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_turnaround.png)
* **감각 사전 예고 팝업:** 🩺 청진기 ➔ ❄️ `차갑다!` / 🔦 손전등 ➔ 💡 `반짝!`
* `C5A_Stethoscope` (6초): 청진기 손목 시연 ➔ 카메라 가슴에 대기 (Static + Object Approach)
  * **[영문]:** `First-person POV static shot. Friendly Korean male pediatrician demonstrates toy dinosaur stethoscope on his own wrist showing 'Not cold!', then slowly moves stethoscope toward camera lens with gentle smile. Eye contact throughout, photorealistic, 6s`
  * **[한글]:** `1인칭 시점 고정 카메라. 친근한 한국인 남성 소아과 의사가 공룡 청진기를 자신의 손목에 대며 "차갑지 않아~" 시연 후, 청진기를 카메라 렌즈 쪽으로 천천히 가져오는 장면. 내내 카메라와 눈맞춤, 실사 화질, 6초`
* `C5A_Throat` (5초): 손전등 들어 보이며 "아~ 해볼까?" (QTE '아~' 버튼)
  * **[영문]:** `First-person POV static shot. Friendly Korean male pediatrician holds small penlight, shows it to camera lens with encouraging smile, then slowly brings light closer to center camera perspective. Eye contact, photorealistic, 5s`
  * **[한글]:** `1인칭 시점 고정 샷. 친근한 한국인 남성 소아과 의사가 작은 손전등을 카메라 렌즈에 보여주고 격려하는 미소 후, 손전등을 카메라 중앙으로 천천히 다가오게 하는 연출. 카메라와 눈맞춤, 실사 화질, 5초`
* `C5A_Ear` (4초): 이경으로 귀 비추기 (QTE 3초 가만히)
  * **[영문]:** `First-person POV static shot. Friendly Korean male pediatrician holds otoscope in center frame with gentle smile and eye contact, then slowly moves it toward right side of frame (approaching ear position). Photorealistic, 4s`
  * **[한글]:** `1인칭 시점 고정 샷. 친근한 한국인 남성 소아과 의사가 이경을 중앙에 들고 카메라와 눈맞춤 후, 이경을 화면 오른쪽 측면(아이 귀 위치)으로 천천히 이동시키는 연출. 실사 화질, 4초`

#### 5-B: 달래기 루트 (곰돌이 매개 ➔ 복식 호흡)
* **참조 이미지:** 🩺 [`real_doctor_room.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_room.png), 👨‍⚕️ [`real_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_turnaround.png)
* `C5B_BearFirst` (6초): 곰돌이에 청진기 먼저 시연 ➔ "네 차례야~"
  * **[영문]:** `First-person POV static medium shot. Kind Korean male pediatrician listens to teddy bear's chest with stethoscope, then holds bear out toward camera lens saying 'Now it's your turn~'. Eye contact at end, photorealistic, 6s`
  * **[한글]:** `1인칭 시점 고정 미디엄 샷. 친절한 한국인 남성 소아과 의사가 곰돌이 가슴에 청진기를 대고 진료한 후, 곰돌이를 카메라 렌즈 쪽으로 내밀며 "이번엔 네 차례야~"라고 유도. 마지막에 카메라와 눈맞춤, 실사 화질, 6초`
* `C5B_Breathing` (5초): 풍선 부풀리기 QTE (3초 누르고 있기)
  * **[영문]:** `First-person POV static medium shot. Friendly Korean male pediatrician looks directly into camera lens, cheerfully demonstrates deep breathing with puffed cheeks, exhaling with 'whoosh'. Encouraging eye contact, photorealistic, 5s`
  * **[한글]:** `1인칭 시점 고정 미디엄 샷. 친근한 한국인 남성 소아과 의사가 카메라 렌즈를 정면으로 바라보며 코로 들이마셔 볼을 부풀린 후 입으로 "후~" 내쉬는 심호흡을 시연. 카메라와 눈맞춤 유지, 실사 화질, 5초`

#### 5-C: 주사 맞기 (7단계 공포 완화)
* **참조 이미지:** 🩺 [`real_doctor_room.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_room.png), 👩‍⚕️ [`real_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_nurse_turnaround.png)
* **[일정표 상태]:** `[ 💉 4. 주사 ]` 하이라이트
* **감각 사전 예고 팝업:** 💉 주사기 ➔ 🌵 `따끔! (3초면 끝나요)`
* `C5C_Notice` (5초): "오늘 건강 주사 맞아야 해" 사전 예고
  * **[영문]:** `First-person POV static medium shot. Kind Korean male pediatrician speaks directly to camera lens with gentle serious but warm expression saying 'Today you need a small shot'. Patient trustworthy tone, photorealistic, 5s`
  * **[한글]:** `1인칭 시점 고정 미디엄 샷. 친절한 한국인 남성 소아과 의사가 카메라 렌즈를 정면으로 바라보며 부드럽지만 진지하고 따뜻한 표정으로 "오늘 주사를 맞아야 해"라고 알림. 차분하고 신뢰감 있는 톤, 실사 화질, 5초`
* `C5C_ShowTools` (6초): 알코올 솜 ➔ 반창고 ➔ 주사기 하나씩 보여주기 (탐색 탭)
  * **[영문]:** `First-person POV static shot. Friendly Korean female nurse in pink scrubs sequentially shows medical tray items toward camera lens: alcohol swab pad, colorful bandage, small syringe. Eye contact between reveals, photorealistic, 6s`
  * **[한글]:** `1인칭 시점 고정 샷. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 의료 쟁반의 알코올 솜, 반창고, 주사기를 순서대로 카메라 렌즈 쪽으로 들어 보임. 아이템 제시 사이 간호사와 눈맞춤, 실사 화질, 6초`
* `C5C_BreathPre` (6초): 풍선 호흡 QTE
  * **[영문]:** `First-person POV static medium shot. Kind Korean female nurse cheerfully demonstrates balloon breathing looking directly into camera lens - inhaling with puffed cheeks, exhaling with 'whoosh'. Direct eye contact, photorealistic, 6s`
  * **[한글]:** `1인칭 시점 고정 미디엄 샷. 파스텔 핑크 스크럽의 친절한 한국인 여성 간호사가 카메라 렌즈를 바라보며 볼을 부풀려 들이마시고 내쉬는 풍선 호흡 시연. 지속적인 카메라 눈맞춤, 실사 화질, 6초`
* `C5C_ArmChoice` (4초): 🦾 오른팔 / 💪 왼팔 선택 (자율 통제감)
  * **[영문]:** `First-person POV static medium shot. Friendly Korean female nurse looks directly into camera, alternately extends left and right hands toward camera from sides saying 'Which arm do you want?'. Eye contact throughout, photorealistic, 4s`
  * **[한글]:** `1인칭 시점 고정 미디엄 샷. 친근한 한국인 여성 간호사가 카메라를 정면으로 바라보며 왼손과 오른손을 번갈아 카메라 쪽으로 내밀어 선택권을 줌. 카메라 눈맞춤 유지, 실사 화질, 4초`
* `C5C_AlcWipe` (5초): "차가울 거야~" 알코올 솜 닦기
  * **[영문]:** `First-person POV close-up of child's arm, static camera. Korean female nurse shows alcohol swab pad from above then slowly lowers swab down toward camera (arm surface). Object descending approach, photorealistic, 5s`
  * **[한글]:** `아이 팔 클로즈업 1인칭 시점. 고정 카메라. 간호사가 알코올 솜을 위에서 보인 후 카메라(팔 표면) 쪽으로 위에서 아래로 천천히 내리는 하강 연출. 실사 화질, 5초`
* `C5C_Injection` (7초): 💪 버티기 QTE (주사기는 화면 가장자리 작게 연출 ➔ 간호사 얼굴 필프레임 환한 미소)
  * **[영문]:** `First-person POV static close-up of child's arm. Nurse looks warmly at camera saying 'Breathe in and out~'. Subtle motion at far edge of frame. Cut to: nurse's face filling frame with huge joyful smile saying 'All done!!'. Photorealistic, 7s`
  * **[한글]:** `1인칭 시점 아이 팔 고정 클로즈업. 간호사가 카메라를 따뜻하게 보며 호흡 유도. 화면 가장자리에 미묘한 동작 후 컷: 간호사 얼굴이 화면을 가득 채우며 "끝났어!!" 환하게 웃음. 실사 화질, 7초`
* `C5C_Bandage` (5초): 반창고 선택 (공룡/별/하트) + 감정 체크 (`😭아팠어요` / `😊괜찮았어요`)
  * **[영문]:** `First-person POV static medium shot. Cheerful Korean female nurse looks directly into camera with big smile, holds up 3 cute bandage options toward camera center. Direct eye contact throughout, photorealistic, 5s`
  * **[한글]:** `1인칭 시점 고정 미디엄 샷. 쾌활한 한국인 여성 간호사가 카메라를 직접 바라보며 큰 미소로 반창고 3종을 카메라 중앙으로 들어 보임. 내내 카메라 눈맞춤, 실사 화질, 5초`

---

### 📍 챕터 6: 보상 & 귀가

* **참조 이미지:** 🩺 [`real_doctor_room.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_room.png), 👨‍⚕️ [`real_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Graphic/hospital/real/real_doctor_turnaround.png)
* **[일정표 상태]:** `[ 🎁 5. 보상 ]` 하이라이트

#### 🎬 C6_Reward — 스티커 보상 선택 (5초)
* **카메라 워크:** Static Medium + Object Offer
* **콘티:** 의사 선생님이 환하게 웃으며 엄지척! 반짝이는 스티커 3종을 카메라 렌즈 앞으로 내묾.
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV static medium shot, joyful Korean male pediatrician looks directly into camera lens with big warm smile and thumbs up, holding out 3 shiny reward stickers toward camera center frame. Celebration atmosphere, photorealistic, 5 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점 고정 미디엄 샷. 기쁜 표정의 한국인 남성 소아과 의사가 카메라 렌즈를 직접 바라보며 환한 미소와 엄지척을 취하고, 빛나는 보상 스티커 3종을 카메라 중앙 앞으로 내묾. 축하 분위기, 실사 화질, 5초`

#### 🎬 C6_Farewell — 작별 인사 (4초) & 엔딩
* **콘티:** 의사 선생님이 "다음에 또 와! 선생님이 기다릴게~" 손 흔듦 ➔ 🎉 진료 성공 배지 획득 엔딩 화면!
* **AI 비디오 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV static medium shot, warm friendly Korean male pediatrician looks directly into camera lens with big genuine smile, waving goodbye enthusiastically directly at camera. Cozy clinic background, photorealistic, 4 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점 고정 미디엄 샷. 따뜻하고 친근한 한국인 남성 소아과 의사가 카메라 렌즈를 내내 정면으로 바라보며 진심 어린 미소로 카메라를 향해 손을 흔들어 작별 인사. 실사 화질, 4초`

---

## 📋 전체 클립 및 파이프라인 요약표

| 단계 | 클립 ID | 형식 | 영문/한글 프롬프트 완비 여부 |
| :--- | :--- | :--- | :---: |
| **Step 1** | `PreStory_1~3` | 3인칭 3D 애니메이션 (30초) | ✅ 완비 |
| **Step 2** | `Visual_Schedule` | 상단 HUD UI | ✅ 완비 |
| **Step 3** | `Model_First_1~3` | 3인칭 관찰 비디오 (45초) | ✅ 완비 |
| **Step 4 (C1)** | `C1_Arrive / HiPath / HidePath` | 1인칭 실사 비디오 | ✅ 완비 |
| **Step 4 (C2)** | `C2_Reception / WaitingRoom` | 1인칭 실사 비디오 | ✅ 완비 |
| **Step 4 (C3)** | `C3_NameCall` | 1인칭 실사 비디오 | ✅ 완비 |
| **Step 4 (C4)** | `C4_DoctorGreet` | 1인칭 실사 비디오 | ✅ 완비 |
| **Step 4 (C5)** | `C5A (3클립) / C5B (2클립) / C5C (7클립)` | 1인칭 실사 비디오 | ✅ 완비 |
| **Step 4 (C6)** | `C6_Reward / Farewell` | 1인칭 실사 비디오 | ✅ 완비 |
