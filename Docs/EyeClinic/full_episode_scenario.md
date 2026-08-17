# [시나리오 마스터 명세] CocoLink: 소아 안과 적응 4단계 풀 시나리오

## : 마스터 기획서(cocolink_eyeclinic_master_spec.md) 기반 4-Step 점진적 실사화 시나리오

> **대상:** 자폐스펙트럼(ASD), 발달지연, 무언어/언어지연, 낯선 기계 및 시각 감각 불안이 높은 유아·아동 (3~9세)  
> **핵심 원칙:** `2D 보노보노풍 동화(마음 안정 & 직관적 표정)` ➔ `2D UI(단순 일정 안내)` ➔ `3D 시연(입체 기계 완충)` ➔ `1인칭 실사(현실 체험)`

---

## 🎨 참조 에셋 라이브러리 (Graphic Reference Assets)

> **💡 단계별 목적에 맞춘 3단 그래픽 파이프라인 (2D 보노보노풍 동화 ➔ 3D 시연 ➔ 1인칭 실사):**

```
[ Step 1: 2D 보노보노풍 동화 ] ───▶ [ Step 3: 3D 캐주얼 시연 ] ───▶ [ Step 4: 1인칭 실사 POV ]
Graphic/2d_storybook/               Graphic/3d_animation/              Graphic/real/
```

### 1. 📖 Step 1 전용 (2D 미니멀 보노보노 스타일: `Graphic/eyeclinic/2d_storybook/`)

- 🐻 **2D 아기 곰돌이 '코코' (보노보노 감성 점 눈 + 노란 스카프):** [`Graphic/eyeclinic/2d_storybook/coco_bear_bonobono_style.jpg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/coco_bear_bonobono_style.jpg)
- 🐻 **2D 엄마 곰돌이 '엄마 코코' (온화한 보노보노풍 미니멀 라인):** [`Graphic/eyeclinic/2d_storybook/mother_bear_bonobono_style.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/mother_bear_bonobono_style.jpeg)
- 🦉 **2D 의사 부엉이 '눈빛 선생님' (동그란 안경 + 흰 가운):** [`Graphic/eyeclinic/2d_storybook/doctor_owl_bonobono_style.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/doctor_owl_bonobono_style.jpeg)
- 🐰 **2D 간호사 토끼 '보미' (민트색 유니폼 + 소아 시력판):** [`Graphic/eyeclinic/2d_storybook/nurse_rabbit_bonobono_style.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/nurse_rabbit_bonobono_style.jpeg)
- 🏥 **2D 안과 건물 외관 (플랫 파스텔 무지개와 눈 간판):** [`Graphic/eyeclinic/2d_storybook/eyeclinic_2d_bonobono_exterior.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/eyeclinic_2d_bonobono_exterior.jpeg)
- 👁️ **2D 안과 진료실 풍경 (따뜻한 시력표와 진료실 책상):** [`Graphic/eyeclinic/2d_storybook/eyeclinic_2d_bonobono_interior.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/eyeclinic_2d_bonobono_interior.jpeg)

### 2. 🧸 Step 3 전용 (3D 캐주얼/토이 모델링 스타일: `Graphic/eyeclinic/3d_animation/`)

- 🐻 **3D 아기 곰돌이 '코코' (소아과 에피소드 오리지널 3D 코코 곰돌이):** [`Graphic/eyeclinic/3d_animation/coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/coco_bear_character_turnaround.png)
- 🐻 **3D 엄마 곰돌이 '엄마 코코':** [`Graphic/eyeclinic/3d_animation/mother_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/mother_bear_character_turnaround.png)
- 🐰 **3D 간호사 토끼 '보미':** [`Graphic/eyeclinic/3d_animation/nurse_rabbit_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/nurse_rabbit_character_turnaround.png)
- 🦉 **3D 의사 부엉이 '눈빛 선생님':** [`Graphic/eyeclinic/3d_animation/doctor_owl_3d_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/doctor_owl_3d_turnaround.png)
- 🎈 **3D 자동굴절검사기 & 예비검사실:** [`Graphic/eyeclinic/3d_animation/eyeclinic_3d_autorefrac_room.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/eyeclinic_3d_autorefrac_room.png)
- 👁️ **3D 안과 진료실:** [`Graphic/eyeclinic/3d_animation/eyeclinic_3d_doctor_room.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/eyeclinic_3d_doctor_room.png)
- 🎬 **[프리비즈] 3-1 턱받침 착석 영상:** [`Docs/EyeClinic/Blender/renders/3-1_chinrest.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-1_chinrest.mp4)
- 🎬 **[프리비즈] 3-2 열기구 관찰 영상:** [`Docs/EyeClinic/Blender/renders/3-2_balloon.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-2_balloon.mp4)
- 🎬 **[프리비즈] 3-3 별 선글라스 축하 영상:** [`Docs/EyeClinic/Blender/renders/3-3_sunglasses.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-3_sunglasses.mp4)

### 3. 📸 Step 4 전용 (1인칭 실사 스타일: `Graphic/real/`)

- 👨‍⚕️ **실사 안과 의사 선생님:** [`Graphic/real/real_eye_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eye_doctor_turnaround.png)
- 👩‍⚕️ **실사 검안사/간호사 선생님:** [`Graphic/real/real_optometrist_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_nurse_turnaround.png)
- 🏥 **[입구] 실사 안과 입구/외관:** [`Graphic/real/real_eyeclinic_exterior.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_exterior.jpeg)
- 📋 **[접수처] 실사 안과 접수대:** [`Graphic/real/real_eyeclinic_reception.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_reception.jpeg)
- 🧸 **[대기실] 실사 안과 대기실/복도:** [`Graphic/real/real_eyeclinic_waiting_room.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_waiting_room.jpeg)
- 🎈 **[예비검사실] 실사 자동굴절검사기/안압계실:** [`Graphic/real/real_eyeclinic_exam_room.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_exam_room.png)
- 👁️ **[진료실] 실사 세극등 현미경 진료실:** [`Graphic/real/real_eyeclinic_doctor_room.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_doctor_room.png)

---

## 🎬 STEP 1: Pre-Story (2D 보노보노풍 동화: 안과는 눈을 반짝이게 해줘요)

> **목적:** 복잡한 시각 자극 없이 극도의 시각적 편안함과 직관적 감정 표현으로 안과에 대한 긍정적 개념 형성.  
> **형식:** 30초 3인칭 2D 미니멀 카툰 모션 애니메이션 (보노보노 감성: 단순한 선, 플랫 파스텔 단색 톤, 느긋한 템포)

### 1-1. 눈이 침침해요 (2D 보노보노풍)

- **참조 에셋:** 🐻 [`coco_bear_bonobono_style.jpg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/coco_bear_bonobono_style.jpg), 🐻 [`mother_bear_bonobono_style.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/mother_bear_bonobono_style.jpeg)
- **길이:** 8초 | **구도:** 3인칭 고정 미디엄 샷
- **콘티:** 푸른 하늘과 잔디 언덕 위, 노란 스카프를 맨 둥글둥글한 곰돌이 코코가 동그란 점 눈을 깜빡거리며 작은 땀방울(💦)과 함께 눈을 살살 비빔. 엄마 곰돌이가 다가와 따뜻하게 토닥이며 "눈이 침침하네? 안과에 가보자~" 나직하고 다정하게 말함.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `2D minimalist Japanese cartoon animation, Bonobono anime aesthetic. A cute round brown baby bear Coco with simple black dot eyes and yellow neck scarf sitting peacefully, blinking slowly and gently rubbing its eyes with a tiny sweatdrop icon (sweatdrop of mild confusion). Kind round mother bear pats its back warmly. Ultra-simple outlines, flat pastel sky blue background, calm relaxing slow pace, 8 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `2D 미니멀 일본 카툰 애니메이션 스타일, 보노보노 애니메이션 감성. 단순한 검은 점 눈과 노란 목 스카프를 맨 귀엽고 둥글둥글한 갈색 아기 곰돌이 코코가 평화롭게 앉아 눈을 천천히 깜빡이고 작은 땀방울 아이콘과 함께 눈을 비빔. 다정한 엄마 곰돌이가 등을 따뜻하게 토닥여 줌. 매우 단순한 선, 플랫 파스텔 하늘색 배경, 차분하고 느긋한 템포, 8초`

### 1-2. 안과 건물의 모습 (2D 보노보노풍)

- **참조 에셋:** 🏥 [`eyeclinic_2d_bonobono_exterior.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/eyeclinic_2d_bonobono_exterior.jpeg), 🐰 [`nurse_rabbit_bonobono_style.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/nurse_rabbit_bonobono_style.jpeg)
- **길이:** 8초 | **구도:** 3인칭 와이드 샷
- **콘티:** 심플하고 깔끔한 파스텔 톤의 안과 건물. 커다란 눈 모양 심볼이 둥실 떠 있고, 문이 부드럽게 열리며 의사 선생님과 간호사 캐릭터가 느긋하게 손을 흔들며 환영함.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `2D minimalist anime aesthetic, Bonobono style. A simple cute pediatric eye clinic building with a friendly big eye sign. Doors slide open smoothly. Friendly cartoon doctor owl and nurse rabbit wave hands slowly and cheerfully. Clean flat pastel colors, peaceful and reassuring vibe, 8 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `2D 미니멀 애니메이션 스타일, 보노보노 풍. 친근하고 커다란 눈 간판이 있는 단순하고 귀여운 소아 안과 건물. 문이 부드럽게 열리고 의사 부엉이와 간호사 토끼가 천천히 여유롭게 손을 흔들며 맞이함. 깔끔한 플랫 파스텔 색감, 평화롭고 안심되는 분위기, 8초`

### 1-3. 눈이 반짝반짝 (2D 보노보노풍)

- **참조 에셋:** 👁️ [`eyeclinic_2d_bonobono_interior.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/eyeclinic_2d_bonobono_interior.jpeg), 🦉 [`doctor_owl_bonobono_style.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/2d_storybook/doctor_owl_bonobono_style.jpeg)
- **길이:** 14초 | **구도:** 3인칭 미디엄 샷
- **콘티:** 의사 선생님이 반짝이는 작은 별 막대를 보여주자 코코의 점 눈이 반짝(✨) 빛남. 의사가 귀여운 노란 별 안경을 코코에게 씌워주자 코코가 입을 'ㅅ' 모양으로 앙다물고 방긋 웃음. "안과는 우리 눈을 시원하고 맑게 도와주는 곳이에요!"
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `2D minimalist Bonobono animation style, kind cartoon doctor gently shines a soft glowing star stick, making teddy bear Coco's simple dot eyes sparkle with tiny yellow stars. Doctor places cute star glasses on Coco, who smiles with an adorable cat-like mouth 'ㅅ'. Calming, cute, stress-free ending, 14 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `2D 미니멀 보노보노 애니메이션 스타일. 친절한 의사가 부드럽게 빛나는 별 막대를 비추자 곰돌이 코코의 단순한 점 눈에 작은 노란 별이 반짝임. 의사가 귀여운 별 안경을 씌워주자 코코가 귀여운 'ㅅ' 입 모양으로 방긋 웃음. 편안하고 귀여운 안심 엔딩, 14초`

---

## 🎨 STEP 2: Visual Schedule (2D UI 단순 시각 일정표)

> **목적:** 인지 부하 없이 "언제 집에 가는지" 전체 진행 과정을 상시 아이콘으로 명확히 보여주어 불안 차단.

### 2-1. 상단 일정표 UI 구성 (HUD)

```
[ 🏥 1. 안과 입구 ] ➔ [ 📋 2. 접수 ] ➔ [ 🎈 3. 눈 검사 ] ➔ [ 👁️ 4. 진료실 ] ➔ [ 🕶️ 5. 보상 ]
```

- **동작 규칙:**
    - 진행 중인 단계: 반짝이는 하이라이트 + 통통 튀는 바운스 효과
    - 완료된 단계: 초록색 체크 표시(✅)로 전환
    - 2D 단순 픽토그램/이모지 카드로 시각적 피로도 최소화

---

## 🎬 STEP 3: Model-First (3D 캐주얼 시연: 곰돌이의 입체 안과 기계 체험)

> **목적:** 2D 동화에서 ➔ 1인칭 실사로 넘어가기 전, **입체 기계(자동검사기, 턱받침, 열기구)의 공간감과 부피감을 3D 장난감 그래픽으로 사전 체험(완충 브릿지).**  
> **형식:** 3인칭 3D 캐주얼 애니메이션 (Mario 3D World / Toy-like Vinyl Texture)  
> **💡 3D 프리비즈 영상 지원:** 본 단계의 카메라 앵글, 타이밍, 모션은 [`Docs/EyeClinic/Blender/renders/`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/)의 프리비즈 영상(.mp4)을 기반으로 제작되었습니다.  
> **전환 나레이션:** _"보노보노 친구 코코가 이제 안과 의자에 앉았어요! 코코가 어떻게 하는지 같이 볼까요?"_

### 3-1. 곰돌이 턱받침에 턱 대기 (3D 시연)

- **참조 에셋:**
    - 🐻 **3D 코코:** [`coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/coco_bear_character_turnaround.png)
    - 🐰 **3D 간호사 토끼:** [`nurse_rabbit_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/nurse_rabbit_character_turnaround.png)
    - 🎈 **3D 검사실 배경:** [`eyeclinic_3d_autorefrac_room.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/eyeclinic_3d_autorefrac_room.png)
- **🎬 3D 프리비즈 영상 (Blender):**
    - 🎥 **[프리뷰 렌더]:** [`Docs/EyeClinic/Blender/renders/3-1_chinrest.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-1_chinrest.mp4) (카메라 앵글 및 모션)
    - 🎭 **[3D Semantic Color ID 마스크]:** [`Docs/EyeClinic/Blender/renders/3-1_chinrest_id_mask.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-1_chinrest_id_mask.mp4) (AI 캐릭터/오브젝트 분별 마스크)
- **💡 3D Semantic Color ID 지정 규칙 (AI Object Masking):**
    - 🔴 **Pure Red (#FF0000) ➔ 🐻 3D 코코 곰돌이 (`coco_bear_character_turnaround.png`)**
        - 3D 씬에서 빨간색 단색으로 렌더링된 영역 전체를 코코 곰돌이 캐릭터로 자동 치환 및 생성.
    - 🟢 **Pure Green (#00FF00) ➔ 🐰 3D 간호사 토끼 (`nurse_rabbit_character_turnaround.png`)**
        - 3D 씬에서 초록색 단색으로 렌더링된 영역(몸통, 귀, 머리를 토닥이는 팔)을 간호사 토끼로 치환 및 생성.
    - 🔵 **Pure Blue (#0000FF) ➔ 🎈 3D 자동굴절검사기 (`eyeclinic_3d_autorefrac_room.png`)**
        - 3D 씬에서 파란색 단색으로 렌더링된 영역을 안과 검사기 본체 및 턱받침 바로 치환 및 생성.
    - 🟡 **Pure Yellow (#FFFF00) ➔ 🪑 검사 의자 & 책상 (가구/인터랙션 환경)**
    - ⚫ **Pure Black (#000000) ➔ 🏥 검사실 배경 (바닥 및 벽면)**
- **길이:** 10초 | **콘티:** 친숙한 귀여운 3D 아기 곰돌이 코코가 자동검사기 턱받침에 턱을 편안하게 착 올리고 이마를 댐. 곁에서 지켜보던 간호사 토끼 보미가 칭찬하며 다정하게 머리를 쓰다듬어 줌.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `3D casual animated style, Mario 3D World aesthetic, smooth vinyl toy texture. A cute friendly brown teddy bear Coco (original 3D model) sits comfortably in front of a friendly 3D eye examination machine, resting chin gently on soft chinrest and forehead against band. Cute friendly female nurse rabbit Bomi in mint scrubs stands beside smiling and gently pats Coco's head with praise. Warm inviting lighting, 10 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `3D 캐주얼 애니메이션 스타일 (마리오 3D 월드 감성, 매끄러운 비닐 장난감 질감). 친숙한 갈색 아기 곰돌이 코코가 3D 안과 검사기 턱받침에 턱을 편안하게 올리고 이마를 댐. 옆에 선 민트색 유니폼의 귀여운 간호사 토끼 보미가 미소 지으며 코코의 머리를 다정하게 쓰다듬어 칭찬함. 따뜻하고 안정적인 조명, 10초`

### 3-2. 곰돌이 열기구 보기 (3D 시연)

- **참조 에셋:** 🎈 [`eyeclinic_3d_balloon_viewfinder.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/eyeclinic_3d_balloon_viewfinder.png) (양쪽 눈 양안 Dual-Lens 뷰파인더 화면)
- **🎬 3D 프리비즈 영상 (Blender):**
    - 🎥 **[프리뷰 렌더]:** [`Docs/EyeClinic/Blender/renders/3-2_balloon.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-2_balloon.mp4) (양안 렌즈 뷰파인더 + 열기구 포커싱 프리뷰)
    - 🎭 **[3D Semantic Color ID 마스크]:** [`Docs/EyeClinic/Blender/renders/3-2_balloon_id_mask.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-2_balloon_id_mask.mp4) (AI 양안 렌즈/열기구/십자선 분별 마스크)
- **💡 3D Semantic Color ID 지정 규칙 (3-2 양안 열기구 보기):**
    - 🔵 **Pure Blue (#0000FF) ➔ 🔍 좌/우 양안 원형 뷰파인더 렌즈 링 프레임 (2개)**
    - 🔴 **Pure Red (#FF0000) ➔ 🎈 양쪽 렌즈 정중앙의 빨간 열기구 (2개)** (둥실 떠오르며 초점이 맞음)
    - 🟡 **Pure Yellow (#FFFF00) ➔ 🎯 양쪽 렌즈 초점 십자선 UI 크로스헤어**
    - ⚪ **Light Gray (#D9D9D9) ➔ ⚙️ 검사기 전면 하우징 바디**
    - ⚫ **Pure Black (#000000) ➔ 🏞️ 렌즈 배경 (맑은 하늘과 푸른 초원)**
- **길이:** 15초 | **콘티 (코코의 1인칭 POV 렌즈 시점):** 양안 검사기 렌즈 속 십자선 중앙으로 흐릿하던 빨간 열기구가 둥실 떠오르며 점점 선명하고 또렷해짐. (보이스오버: "우와! 빨간 열기구 찾았다!")
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `3D casual animated style, eye clinic vision test POV. First-person POV view looking through dual circular binocular eyepieces of a pediatric auto-refractor. In each lens viewfinder with yellow crosshairs, a cute red hot air balloon floats upwards against a bright blue sky and green hills, gradually focusing from blurry to sharp and crystal clear. Cheerful, colorful, stress-free medical examination scene, 15 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `3D 캐주얼 애니메이션 스타일, 안과 시력검사 1인칭 시점(POV). 소아용 자동굴절검사기 양안(쌍안경) 렌즈를 통해 바라본 1인칭 화면. 노란 십자선 가이드 안에서 파란 하늘과 초원을 배경으로 둥실 떠오르는 귀여운 빨간 열기구가 흐린 상태에서 점차 선명하고 또렷하게 초점이 맞춰짐. 밝고 경쾌한 무자극 검사 영상, 10초`

### 3-3. 곰돌이 멋진 별 선글라스 획득 (3D 시연)

- **참조 에셋:** 🦉 [`doctor_owl_3d_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/doctor_owl_3d_turnaround.png), 🐻 [`coco_bear_character_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/3d_animation/coco_bear_character_turnaround.png)
- **🎬 3D 프리비즈 영상 (Blender):** 🎥 [`Docs/EyeClinic/Blender/renders/3-3_sunglasses.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/3-3_sunglasses.mp4) (선글라스 착용 및 축하 바운스 모션 프리뷰)
- **길이:** 20초 | **콘티:** 의사 부엉이 선생님이 "코코 정말 최고야!" 하며 반짝이는 금빛 별 선글라스를 씌워주고 하이파이브! 코코가 기뻐하며 브이(V) 포즈.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `3D casual animated style. Joyful doctor owl in white coat puts shiny gold star sunglasses on teddy bear Coco and gives a high-five. Coco does a cute victory V-sign. Bright confetti and sparkles celebrating success, 20 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `3D 캐주얼 애니메이션 스타일. 흰 가운의 의사 부엉이 선생님이 곰돌이 코코에게 반짝이는 금빛 별 선글라스를 씌워주고 하이파이브를 침. 코코가 기뻐하며 브이 포즈를 취함. 축하 파티클 효과, 20초`
- **전환 나레이션:** _"코코도 열기구를 신나게 찾았어요! 이제 우리 차례예요! 출발해볼까요?"_ ➔ **Step 4(1인칭 실사)로 전환!**

---

## 🎬 STEP 4: Interactive Simulation (1인칭 실사 6개 챕터 체험)

> **목적:** 2D 동화와 3D 시연으로 완벽히 적응한 후, 실제 소아 안과 1인칭 POV 실사 비디오로 직접 검사를 수행하며 현실 안과 공포 제로화.  
> **인터랙션 피처:** PECS 그림 카드 선택지 + 사전 감각 예고 (🎈열기구! / 💡반짝 불빛! / 💧시원한 물방울!)

---

### 📍 챕터 1: 안과 도착 & 입구

- **[일정표 상태]:** `[ 🏥 1. 안과 입구 ]` 하이라이트
- **참조 에셋:** 🏥 [`real_eyeclinic_exterior.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_exterior.jpeg), 👩‍⚕️ [`real_optometrist_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_nurse_turnaround.png)

#### 🎬 C1_Arrive — 안과 입구 도착 (5초)

- **카메라 워크:** Slow Dolly-In (1인칭 아이 눈높이 전진)
- **콘티:** 안과 유리 자동문이 열리고 민트색 스크럽을 입은 친절한 간호사 선생님이 접수대 너머에서 카메라를 향해 반갑게 손을 흔듦.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV child's eye level, slow dolly-in approaching a bright welcoming Korean pediatric eye clinic entrance. Automatic glass doors slide open revealing modern cheerful interior with eye chart art. Friendly Korean female optometrist in mint green scrubs behind reception desk smiles warmly and waves hand directly at camera. Photorealistic cinematic quality, warm soft lighting, 16:9, 5 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `아이 눈높이 1인칭 POV. 카메라가 천천히 전진하며 밝고 환영하는 한국 소아 안과 입구로 다가가는 장면. 유리 자동문이 열리며 시력표 그림이 있는 화사한 내부가 드러남. 민트 그린 스크럽의 친근한 한국인 여성 검안사가 접수대 너머에서 카메라를 보며 따뜻하게 손을 흔듦. 실사 영화 화질, 5초`

- **선택지 (PECS 그림 카드):**
    - **[모드 A (경증)]**: `[👋 인사하기]` / `[😶 가만히]` / `[🙈 숨기]`
    - **[모드 B (무언어)]**: `[👋 인사하기]` / `[🤝 손잡기]`

- **분기 클립:**
    - `C1_HiPath` (3초): 검안사 선생님이 환하게 웃으며 엄지척 ("안녕! 어서 와~") | Static Shot
        - **[영문]:** `First-person POV static shot, friendly Korean female optometrist nurse giving bright smile and thumbs up directly at camera lens, photorealistic, 3s`
        - **[한글]:** `1인칭 시점 고정 샷. 친절한 한국인 여성 검안사/간호사가 카메라를 정면으로 보며 환하게 웃고 엄지척을 해주는 장면. 실사 화질, 3초`
    - `C1_HidePath` (3초): 검안사 선생님이 귀여운 곰돌이 인형을 보여주며 안심시킴 ("괜찮아, 천천히 들어오자") | Static Shot
        - **[영문]:** `First-person POV static shot, kind Korean female nurse pulling out cute soft teddy bear plush toy with yellow scarf gently showing it toward camera lens with patient warm smile, photorealistic, 3s`
        - **[한글]:** `1인칭 시점 고정 샷. 친절한 간호사가 노란 스카프를 맨 곰돌이 인형을 부드럽게 내밀며 따뜻한 미소로 안심시키는 장면. 실사 화질, 3초`

---

### 📍 챕터 2: 접수 & 대기실 탐색

- **[일정표 상태]:** `[ 📋 2. 접수 ]` 하이라이트
- **참조 에셋:** 📋 [`real_eyeclinic_reception.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_reception.jpeg), 🧸 [`real_eyeclinic_waiting_room.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_waiting_room.jpeg), 👩‍⚕️ [`real_optometrist_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_nurse_turnaround.png)

#### 🎬 C2_Reception — 접수 창구 (5초)

- **카메라 워크:** Static Eye-Level
- **참조 에셋:** 📋 [`real_eyeclinic_reception.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_reception.jpeg)
- **콘티:** 간호사 선생님이 "오늘 눈 검사하러 왔구나! 이름이 뭐예요?" 물어보며 귀여운 눈 모양 진료 카드를 건넴.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV child's eye level, static shot. Friendly Korean female nurse behind bright eye clinic counter smiles warmly, holding cute clipboard, offering a colorful eye-shaped appointment card toward camera lens. Direct eye contact, warm pediatric eye clinic reception, photorealistic, 5 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `아이 눈높이 1인칭 시점. 고정 샷. 밝은 안과 카운터 너머의 친근한 한국인 간호사가 따뜻하게 웃으며 클립보드를 들고 귀여운 눈 모양 카드를 카메라 렌즈 쪽으로 건네줌. 카메라와 눈맞춤. 실사 화질, 5초`
- **인터랙션 (PECS):** `[🗣️ 이름 말하기]` 또는 `[🤐 고개 끄덕이기]` 카드 탭

#### 🎬 C2_WaitingRoom — 대기실 탐색 & 그림 찾기 (6초)

- **카메라 워크:** Slow Pan Left-to-Right
- **참조 에셋:** 🧸 [`real_eyeclinic_waiting_room.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_waiting_room.jpeg)
- **콘티:** 대기실 벽면의 알록달록 눈 나무 벽화(Green Dream)와 안경/선글라스 거치대, 벤치에 앉은 큰 곰돌이 인형을 둘러봄.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV seated eye level, slow pan left to right exploring a cozy colorful Korean pediatric eye clinic waiting room corridor. Light wooden walls, comfortable pastel sofa bench with a cute large plush teddy bear sitting, wall decorated with a colorful eye tree mural 'Green Dream', and a colorful display of children's eye glasses. Natural warm lighting, photorealistic, 6 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `1인칭 시점. 앉은 눈높이. 카메라가 왼쪽에서 오른쪽으로 천천히 회전하며 아늑한 소아 안과 대기실과 복도를 탐색. 파스텔 벤치 소파 위의 큰 곰돌이 인형, 벽면의 알록달록한 눈 나무 벽화(Green Dream), 어린이용 안경 거치대 등이 보임. 따뜻한 자연광, 실사 화질, 6초`
- **탐색 미션 (터치):** 🧸 곰돌이 인형 / 🌳 눈 나무 벽화 / 👓 어린이 안경 중 1개 터치 ➔ "잘 찾았어! 시력 검사 준비 완료!"

---

### 📍 챕터 3: 예비 검사실 (기계 검사 & 열기구/안압)

- **[일정표 상태]:** `[ 🎈 3. 눈 검사 ]` 하이라이트
- **참조 에셋:** 🎈 [`real_eyeclinic_exam_room.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_exam_room.png), 👩‍⚕️ [`real_optometrist_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_nurse_turnaround.png)

#### 🎬 C3_PreExamRoom — 검사실 이동 (4초)

- **카메라 워크:** Dolly-In Walk
- **콘티:** 검안사 선생님이 검사실 문을 열고 "이쪽으로 와서 곰돌이 코코가 봤던 신기한 기계 속 열기구를 볼까요?" 손짓하며 안내.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV, slow steady dolly-in walking through open door into a clean bright eye examination room. Friendly female optometrist standing beside modern pediatric autorefractor machine gestures warmly toward the comfortable chair. Direct eye contact, photorealistic, 4 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `1인칭 시점. 카메라가 천천히 걸어가며 깨끗한 안과 예비검사실로 들어감. 최신 소아용 자동굴절검사기 옆에 선 친절한 여성 검안사가 의자를 가리키며 다정하게 손짓함. 카메라와 눈맞춤, 실사 화질, 4초`

#### 🎬 C3_ChinRest — 턱받침에 턱 대기 (5초)

- **카메라 워크:** Approaching Dolly-In & Close-Up on Chinrest (1인칭 POV)
- **참조 에셋:** 🎈 [`real_eyeclinic_exam_room.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_exam_room.jpeg), 👩‍⚕️ [`real_optometrist_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_nurse_turnaround.png), 👁️ [`C3_chinrest_concept.jpg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/real/C3_chinrest_concept.jpg)
- **🎬 3D 실사 프리비즈 영상 (Blender):**
    - 🎥 **[1인칭 POV 3D 프리뷰]:** [`Docs/EyeClinic/Blender/renders/real/C3_chinrest.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/real/C3_chinrest.mp4) (카메라 눈높이 전진 및 안착 모션)
    - 🎭 **[Semantic Color ID 마스크]:** [`Docs/EyeClinic/Blender/renders/real/C3_chinrest_id_mask.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/real/C3_chinrest_id_mask.mp4) (AI 비디오 생성용 마스킹)
- **💡 3D Semantic Color ID 규칙:**
    - 🔴 **Pure Red (#FF0000):** 턱받침 및 이마받침 패드 (Chinrest / Forehead Band)
    - 🔵 **Pure Blue (#0000FF):** 자동굴절검사기 본체 하우징 (Autorefractor Housing)
    - 🟢 **Pure Green (#00FF00):** 곁에서 안내하는 검안사 선생님 손길/팔 (Optometrist Nurse Guiding Hand)
    - 🟡 **Pure Yellow (#FFFF00):** 검사 테이블/책상 (Desk)
    - 🩵 **Cyan (#00FFFF):** 양안 뷰파인더 렌즈 (Optical Lenses)
- **콘티:** 의자에 앉아 검사기 턱받침이 시야에 다가옴. 검안사 선생님이 부드러운 손길로 "턱을 콕! 이마를 착! 대볼까?" 안내.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV, approaching smooth white chinrest of autorefractor machine. Friendly female optometrist gently guides with clean hands near the sides smiling reassuringly, saying 'Rest your chin here gently~'. Direct eye contact, photorealistic, 5 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `1인칭 시점. 자동굴절검사기의 매끄러운 흰색 턱받침에 다가가는 시야. 친절한 여성 검안사가 부드럽게 손짓하며 안심시키는 미소로 턱을 대도록 안내함. 실사 화질, 5초`
- **인터랙션 QTE:** 화면의 턱받침 가이드에 맞춰 `[턱 대기 3초 Hold]` 탭 유지!

#### 🎬 C3_BalloonView — 열기구 보기 자동굴절검사 (6초)

- **감각 사전 예고 팝업:** 🎈 `열기구 찾기!`
- **카메라 워크:** Machine Lens POV (양안 렌즈 속 시야 & 크로스헤어 타깃)
- **참조 에셋:** 🎈 [`real_c3_balloon_view.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c3_balloon_view.jpeg), 👍 [`real_optometrist_thumbs_up.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_thumbs_up.jpeg)
- **🎬 3D 실사 프리비즈 영상 (Blender):**
    - 🎥 **[렌즈 POV 3D 프리뷰]:** [`Docs/EyeClinic/Blender/renders/real/C3_balloon_view.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/real/C3_balloon_view.mp4) (양안 렌즈 십자선 & 열기구 부유 모션)
    - 🎭 **[Semantic Color ID 마스크]:** [`Docs/EyeClinic/Blender/renders/real/C3_balloon_view_id_mask.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/real/C3_balloon_view_id_mask.mp4) (AI 비디오 생성용 마스킹)
- **💡 3D Semantic Color ID 규칙:**
    - 🔵 **Pure Blue (#0000FF):** 좌/우 2개 원형 렌즈 아이피스 링 (Dual Lens Eyepieces)
    - 🟡 **Pure Yellow (#FFFF00):** 좌/우 렌즈 초점 십자선 및 가이드 링 (Crosshair Reticle)
    - 🔴 **Pure Red (#FF0000):** 중앙 타깃 열기구 및 바구니 (Hot Air Balloon)
    - ⚪ **Light Gray (#D9D9D9):** 검사기 본체 전면 하우징 (Autorefractor Housing)
    - ⚫ **Pure Black (#000000):** 배경 하늘과 초원 풍경 (Background Meadow / Sky)
- **콘티:** 렌즈 안으로 붉은 열기구와 푸른 초원이 보임. 초점이 흐려졌다 선명해지는 연출. "열기구가 둥실둥실~ 가만히 3초만 바라보자!" ➔ 검안사 선생님이 "열기구 정말 잘 봤어요! 백 점!" 환하게 칭찬.
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV looking through an autorefractor lens view. A colorful red hot air balloon floats over a green grassy country road landscape. The image slightly blurs and comes back into crisp sharp focus smoothly. Cut to: female optometrist giving enthusiastic thumbs up saying 'Awesome job!'. Calm visual, photorealistic, 6 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `자동굴절검사기 렌즈 속을 들여다보는 1인칭 시점. 초원 도로 위로 떠 있는 알록달록한 빨간 열기구. 이미지가 살짝 흐려졌다가 부드럽게 또렷해짐. 컷: 여성 검안사가 크게 웃으며 엄지척을 해줌. 차분하고 흥미로운 시각 연출, 실사 화질, 6초`
- **인터랙션:** 화면 속 🎈 열기구 터치 ➔ 초점 맞추기 성공!

---

### 📍 챕터 4: 그림 시력 검사

- **참조 에셋:** 🎈 [`real_eyeclinic_exam_room.jpeg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_exam_room.jpeg), 👩‍⚕️ [`real_optometrist_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_nurse_turnaround.png), 👁️ [`B5276385504_41125294488.jpg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/B5276385504_41125294488.jpg) (한식표준 3M용 시력표 실물), 🖼️ [`real_c4_chart_match.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c4_chart_match.png)

#### 🎬 C4_ChartMatch — PECS 한식표준 시력표 맞추기 (6초)

- **참조 실물 시력표:** [`Docs/EyeClinic/Graphic/real/B5276385504_41125294488.jpg`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/B5276385504_41125294488.jpg) (대한안과학회 제정 한식표준 3M용 시력표)
- **카메라 워크:** Eye-Level toward Korean Standard Eye Chart (한식표준 3M용 시력표)
- **🎬 3D 실사 프리비즈 영상 (Blender):**
    - 🎥 **[1인칭 POV 3D 프리뷰]:** [`Docs/EyeClinic/Blender/renders/real/C4_chart_match.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/real/C4_chart_match.mp4) (지시봉 포인팅 & 아이 맞춤 시선 모션)
    - 🎭 **[Semantic Color ID 마스크]:** [`Docs/EyeClinic/Blender/renders/real/C4_chart_match_id_mask.mp4`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/renders/real/C4_chart_match_id_mask.mp4) (AI 비디오 생성용 마스킹)
- **💡 3D Semantic Color ID 규칙:**
    - 🔵 **Pure Blue (#0000FF):** 한식표준 조명 시력표 판 (Korean Standard Light Box Eye Chart)
    - 🟡 **Pure Yellow (#FFFF00):** 타깃 그림 기호 (Target Symbol: ✈️ 비행기)
    - 🔴 **Pure Red (#FF0000):** 기타 그림 기호 (Other Symbols: 🦋 나비, 🐦 새, 🚗 자동차)
    - 🟢 **Pure Green (#00FF00):** 검안사 선생님 (Optometrist Nurse)
    - 🟣 **Magenta (#FF00FF):** 지시봉 (Pointer Stick)
    - ⚫ **Pure Black (#000000):** 검사실 배경 및 벽면 (Background Room / Wall)
- **콘티:** 검안사 선생님이 지시봉으로 벽에 걸린 실제 **한식표준 시력표** 속 그림(✈️ 비행기, 🦋 나비, 🐦 새, 🚗 자동차)을 가리킴. "선생님이 가리키는 그림이 무엇일까요? 손으로 콕 찔러볼까요?"
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV child's eye level in Korean pediatric eye clinic. Friendly Korean female optometrist nurse holding a cute character pointer stick points to a Korean standard illuminated wall-mounted eye chart (한식표준시력표) displaying picture symbols on the right column (an airplane, a butterfly, a bird, a car). She smiles warmly at camera waiting for answer. Bright reassuring clinic lighting, photorealistic, 6 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `한국 소아 안과 검사실 아이 눈높이 1인칭 시점. 친근한 여성 검안사가 귀여운 캐릭터 지시봉으로 벽에 걸린 한식표준 조명 시력표의 우측 그림 기호(비행기, 나비, 새, 자동차)를 가리키며 카메라를 보고 따뜻하게 미소 지음. 밝고 따뜻한 클리닉 조명, 실사 화질, 6초`
- **PECS 터치 인터랙션:** 화면 하단 `[✈️ 비행기]` / `[🦋 나비]` / `[🐦 새]` / `[🚗 자동차]` 그림 카드 중 일치하는 카드 탭 ➔ 딩동댕 칭찬 사운드!

---

### 📍 챕터 5: 안과 진료실 & 맞춤 안경 검사 (시험 안경 착용)

- **[일정표 상태]:** `[ 👁️ 4. 진료실 ]` 하이라이트
- **참조 에셋:** 👨‍⚕️ [`real_c5_doctor_greet.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c5_doctor_greet.png) (진료실 문열림 & 의사 인사 키프레임), 👓 [`real_c5_trial_frame.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c5_trial_frame.png) (소아용 동그란 시험 안경 착용), ✨ [`real_c5_lens_change.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c5_lens_change.png) (시험 안경 렌즈 너머 선명해지는 시야), 👁️ [`real_eyeclinic_doctor_room.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eyeclinic_doctor_room.png), 👨‍⚕️ [`real_eye_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eye_doctor_turnaround.png)

#### 🎬 C5_DoctorGreet — 의사 선생님 인사 & 시험 안경 안내 (5초)

- **참조 키프레임:** 👨‍⚕️ [`Docs/EyeClinic/Graphic/real/real_c5_doctor_greet.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c5_doctor_greet.png)
- **카메라 워크:** Dolly-In ➔ Static
- **콘티:** 진료실 문이 열리고 둥근 안경을 쓴 친절한 안과 전문의 선생님이 맞이함. "어서 오세요! 오늘 우리 친구 눈에 딱 맞는 안경을 찾아볼 거예요!"
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV entering warm Korean pediatric ophthalmology exam room. Friendly male eye doctor in 30s with round glasses and white lab coat looks into camera with reassuring smile, gently welcoming child into the exam chair. Bright cozy pediatric clinic lighting, photorealistic, 5 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `1인칭 시점. 아늑한 한국 소아 안과 진료실 입장. 둥근 안경과 흰 가운의 30대 남성 안과 의사가 안심시키는 미소로 카메라를 보며 진료 의자로 반갑게 맞이함. 밝고 아늑한 소아 진료실 조명, 실사 화질, 5초`

#### 🎬 C5A_TrialFrame — 소아용 동그란 시험 안경 써보기 (5초)

- **참조 키프레임:** 👓 [`Docs/EyeClinic/Graphic/real/real_c5_trial_frame.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c5_trial_frame.png)
- **감각 사전 예고 팝업:** 👓 `동글동글 시험 안경 써보기!`
- **카메라 워크:** Eye-Level Static POV
- **콘티:** 의사 선생님이 알록달록한 동그란 시험 안경(Trial Frame)을 보여주며 카메라에 부드럽게 씌워줌. "짜잔! 동글동글 멋진 안경 써볼까? 귀 뒤에 쏙 걸쳐줄게~"
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV static shot. Friendly Korean male eye doctor gently brings a colorful pediatric round trial frame (test glasses) toward camera lens with warm reassuring smile, fitting it comfortably on the child's perspective. Photorealistic, 5 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `1인칭 시점 고정 샷. 친절한 한국인 남성 안과 의사가 알록달록한 소아용 동그란 시험 안경을 카메라 렌즈 앞으로 부드럽게 가져와 편안하게 씌워주는 연출. 실사 화질, 5초`

#### 🎬 C5A_LensChange — 렌즈 쏙쏙 맞춤 교체 & 시야 선명화 (6초)

- **참조 키프레임:** ✨ [`Docs/EyeClinic/Graphic/real/real_c5_lens_change.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c5_lens_change.png)
- **카메라 워크:** POV through Trial Frame (안경 렌즈 너머 시야)
- **콘티:** 의사 선생님이 동그란 도수 렌즈를 시험 안경에 쏙 끼워 넣음 ➔ 살짝 흐릿했던 시야가 반짝하고 선명하고 또렷해짐! "와, 세상이 훨씬 선명하고 또렷하게 보이지? 최고야!"
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV through trial frame eyeglasses. Friendly eye doctor smiles as he clicks a round optical test lens into the frame. Instant shift from slight soft blur to crisp crystal-clear vision with bright twinkle effect. Doctor gives a cheerful thumbs up. Photorealistic, 6 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `시험 안경을 쓴 1인칭 시점. 의사가 동그란 광학 테스트 렌즈를 안경테에 쏙 끼움. 살짝 흐릿했던 시야가 반짝하는 효과와 함께 선명하고 또렷하게 맑아짐. 의사가 밝게 엄지척을 해줌. 실사 화질, 6초`

---

### 📍 챕터 6: 안경 처방전 발급 & 귀가

- **[일정표 상태]:** `[ 📄 5. 완료 ]` 하이라이트
- **참조 에셋:** 📄 [`real_c6_reward.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c6_reward.png) (접수처 안경 처방전 발급 키프레임), 👨‍⚕️ [`real_eye_doctor_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_eye_doctor_turnaround.png), 👩‍⚕️ [`real_optometrist_nurse_turnaround.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_optometrist_nurse_turnaround.png)

#### 🎬 C6_Reward — 안경 처방전 전달 (5초)

- **참조 키프레임:** 📄 [`Docs/EyeClinic/Graphic/real/real_c6_reward.png`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Graphic/real/real_c6_reward.png)
- **콘티:** 검안사 간호사 선생님이 대기실/접수처에서 오늘 완성된 **진짜 안경 처방전**을 양손으로 공손히 내밈. "오늘 검사 정말 씩씩하게 잘 받았어요! 이 처방전으로 안경원에 가서 멋진 안경 맞추세요!"
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV static shot in warm Korean pediatric eye clinic waiting room. Friendly Korean female optometrist nurse in mint scrubs (matching turnaround reference) warmly holds out an official eyeglasses prescription folder (안경 처방전) with both hands toward camera lens with a proud cheerful smile. Photorealistic, 5 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `따뜻한 소아 안과 대기실/접수처 1인칭 시점 고정 샷. 민트 스크럽의 친절한 한국인 검안사 간호사(턴어라운드 일치)가 안경 처방전을 양손으로 정중히 카메라 렌즈 쪽으로 내밀며 대견하고 밝은 미소를 지음. 실사 화질, 5초`
- **보상 터치 인터랙션:** 화면 중앙 `[📄 안경 처방전 받기]` 카드 탭 ➔ 딩동댕 칭찬 사운드!

#### 🎬 C6_Farewell — 의료진 작별 인사 (5초)

- **콘티:** 안과 의사 선생님과 간호사 선생님이 나란히 서서 카메라를 보며 환하게 웃고 손을 흔듦. "눈이 반짝반짝 건강해졌어요! 다음에 또 만나요, 안녕~!" ➔ 🎉 안과 박사 수료 배지 획득 엔딩!
- **AI 비디오 프롬프트:**
    - **[영문 입력용]:**
        > `First-person POV static medium two-shot. Kind Korean male eye doctor and female optometrist nurse standing side by side, looking directly into camera lens with warm proud smiles. Both giving high-fives and waving goodbye happily. Bright pediatric clinic background, photorealistic cinematic quality, 5 seconds`
    - **[한글 해석 및 전달 의미]:**
        > `1인칭 시점 고정 미디엄 투샷. 친절한 한국인 남성 안과 의사와 여성 검안사 간호사가 나란히 서서 카메라 렌즈를 정면으로 바라보며 자랑스러운 미소를 지음. 두 사람 모두 카메라를 향해 하이파이브와 손을 흔들어 작별 인사. 실사 영화 화질, 5초`

---

## 📋 전체 클립 및 파이프라인 요약표

| 단계            | 클립 ID                                        |          시각 스타일          | 인터랙션 / 주요 연출                          |
| :-------------- | :--------------------------------------------- | :---------------------------: | :-------------------------------------------- |
| **Step 1**      | `PreStory_1~3`                                 | **2D 보노보노풍 동화** (30초) | 눈 비비기 ➔ 안과 소개 ➔ 별 안경               |
| **Step 2**      | `Visual_Schedule`                              |   **2D UI 픽토그램** (HUD)    | 입구 ➔ 접수 ➔ 기계 ➔ 진료 ➔ 보상              |
| **Step 3**      | `Model_First_1~3`                              |   **3D 캐주얼 시연** (45초)   | 턱받침 ➔ 열기구 찾기 ➔ 별 선글라스            |
| **Step 4 (C1)** | `C1_Arrive / HiPath / HidePath`                |      **1인칭 실사 POV**       | [인사] / [숨기] PECS 그림 카드                |
| **Step 4 (C2)** | `C2_Reception / WaitingRoom`                   |      **1인칭 실사 POV**       | [이름 말하기] PECS + 그림 찾기 터치           |
| **Step 4 (C3)** | `C3_PreExamRoom / ChinRest / BalloonView`      |   **1인칭 실사 POV** + QTE    | 턱 대기 3초 + 🎈 열기구 찾기                  |
| **Step 4 (C4)** | `C4_ChartMatch`                                |   **1인칭 실사 POV** + 터치   | ✈️ 비행기 / 🦋 나비 / 🐦 새 / 🚗 차 PECS 매칭 |
| **Step 4 (C5)** | `C5_DoctorGreet / C5A_TrialFrame / C5A_LensChange` |   **1인칭 실사 POV** + 터치   | 👓 동그란 시험 안경 착용 & 도수 렌즈 맞춤    |
| **Step 4 (C6)** | `C6_Reward / Farewell`                         |      **1인칭 실사 POV**       | [안경 처방전 받기] 탭 + 작별 인사             |
