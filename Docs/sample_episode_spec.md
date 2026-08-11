# [기획서] 코코링크(CocoLink) 샘플 에피소드
## : AI 기반 인터랙티브 소아과 병원 경험 훈련 (MVP)

---

## 1. 개요 및 기획 배경

* **프로젝트명:** 코코링크 (CocoLink)
* **목표:** 말이 느리거나 병원 공포감이 높은 아동(자폐스펙트럼, 발달지연, 유아)을 위한 시각적·행동적 사전 적응(Desensitization) 인터랙티브 비디오 훈련 앱.
* **핵심 메커니즘:** 《디트로이트: 비컴 휴먼》 스타일의 분기형 인터랙티브 비디오 시스템 + 누적 관계도(친밀도/불안도)에 따른 동적 반응 연출.
* **샘플 목표:** 1인 개발/제작 리소스를 최소화(AI 비디오 클립 5개)하면서 핵심 시스템(선택-상태 변화-조건 분기-QTE 미션)을 구현 및 검증.

---

## 2. 캐릭터 및 핵심 상태 변수 (State Machine)

### 2.1 주요 캐릭터
* **의사 선생님:** 온화하고 친절한 소아과 전문의 (POV 1인칭 시점 연출).
  * 둥근 안경, 깔끔한 흰색 가운, 파스텔 톤의 파란 셔츠, 귀여운 청진기 착용.
  * 30대 후반 실사 한국인 의사 모습.
* **간호사 선생님:** 따뜻하고 상냥한 소아과 간호사.
  * 단정한 머리, 파스텔 핑크/연보라 톤의 소아과 스크럽 유니폼 착용.
  * 20대 후반~30대 초반 실사 한국인 간호사 모습.
* **아이 (사용자):** 1인칭 관찰자 및 당사자.

#### 🎨 캐릭터 일관성 유지용 턴어라운드 시트 (Model Sheet)

##### 1) 의사 선생님 턴어라운드 시트
![의사 선생님 캐릭터 턴어라운드](file:///d:/Github/Unity/cocolink/Docs/pediatrician_turnaround.png)

##### 2) 간호사 선생님 턴어라운드 시트
![간호사 선생님 캐릭터 턴어라운드](file:///d:/Github/Unity/cocolink/Docs/nurse_turnaround.png)

##### 3) 소아과 진료실 배경 턴어라운드/레퍼런스 시트 (Clinic Background)
![소아과 진료실 배경](file:///d:/Github/Unity/cocolink/Docs/clinic_background.png)

> **💡 [핵심] 캐릭터 + 배경 완벽한 공간 일관성(Spatial Consistency) 작업 파이프라인:**
> 1. **배경 레퍼런스 고정 (`clinic_background.png`):** 모든 비디오 클립 생성 시 소아과 진료실 배경 이미지를 고정값으로 사용합니다.
> 2. **캐릭터+배경 1장 베이스 컷 (Base Composite Image) 합성:**
>    * Midjourney / Photoshop에서 `clinic_background.png` 배경 위에 `pediatrician_turnaround.png`(의사)와 `nurse_turnaround.png`(간호사)를 자연스럽게배치하여 **첫 장면에셋 정지 이미지(Start Frame)**를 1장 합성합니다.
> 3. **Image-to-Video 툴 입력 (Runway / Kling AI / Luma):**
>    * 그렇게 완성된 **'캐릭터+배경 통합 베이스 이미지'**를 비디오 AI의 **First Frame Image**로 넣고 동작 프롬프트만 주면 배경과 인물 모두 100% 동일하게 일관성이 유지됩니다!





### 2.2 누적 상태 변수 (State)
```json
{
  "doctor_trust": 30,   // 의사 선생님과의 친밀도/신뢰도 (범위: 0 ~ 100, 초기값: 30)
  "anxiety_level": 50   // 아동의 심리적 불안도 (범위: 0 ~ 100, 초기값: 50)
}
```

---

## 3. 전체 에피소드 분기 시나리오 (Flowchart)

```
                                [Video_A: 진료실 입장 & 의사 인사]
                                       │
                ┌──────────────────────┼──────────────────────┐
                ▼                      ▼                      ▼
         [선택 1: 안녕 인사]    [선택 2: 멍하니 대기]   [선택 3: 부모 뒤로 숨기]
         (Trust +20 / Anx -10) (Trust +0 / Anx +0)   (Trust -10 / Anx +20)
                │                      │                      │
                └──────────────────────┼──────────────────────┘
                                       │
                   [조건 체크: doctor_trust 수치 확인]
                                       │
               ┌───────────────────────┴───────────────────────┐
               ▼                                               ▼
     [doctor_trust >= 50]                            [doctor_trust < 50]
  (친밀도 높음 / 불안도 낮음)                       (친밀도 낮음 / 불안도 높음)
               │                                               │
   [Video_B: 청진기 보여주기]                      [Video_C: 곰돌이 인형으로 달래기]
               │                                               │
    [QTE 미션: 청진기 터치]                         [QTE 미션: 곰돌이 코 터치]
               │                                               │
               └───────────────────────┬───────────────────────┘
                                       │
                        [Video_D: 진료 성공 & 스티커 보상]
```

---

## 4. 비디오 클립별 스토리보드 & AI 프롬프트 명세 (5개 클립)

모든 클립은 실사 영화/드라마 느낌의 **'따뜻하고 친근한 3D/실사(Photorealistic Real-Person)'** 스타일로 통일합니다.

* **🎯 추천 화면 비율 (Aspect Ratio):**
  * **태블릿 / PC / 가로형 타겟 (추천):** **`16:9`** (Midjourney: `--ar 16:9`, Runway/Kling: `16:9` 설정) - *아이들이 시각적 몰입감을 갖기에 가장 적합*
  * **스마트폰 세로형 타겟:** **`9:16`** (Midjourney: `--ar 9:16`, Runway/Kling: `9:16` 설정)

---


### 🎬 Video_A: 진료실 입장 & 의사 선생님 인사
* **상황:** 아동(사용자)이 진료실 문을 열고 들어서자 의사 선생님이 반갑게 인사를 건네는 첫 장면.
* **권장 클립 길이:** **4초** (후반 2초는 UI 선택지 등장 구간)
* **시각 연출 (콘티):**
  * `0.0s - 1.5s`: 문이 열리며 1인칭 POV 시점으로 따뜻하고 밝은 소아과 진료실 내부가 보임. 의사 선생님이 카메라를 정면으로 바라봄.
  * `1.5s - 4.0s`: 의사 선생님이 따뜻한 미소를 지으며 손을 흔들어 반갑게 인사함 ("안녕! 어서 오렴~").
* **카메라 워크:** Eye-level 1인칭 POV, 렌즈 천천히 의사 쪽으로 Dolly In.
* **AI 생성 프롬프트 (Runway / Kling / Luma):**
  * **[영문 입력용]:**
    > `First-person POV photo, opening a pediatric clinic room door. A real friendly Korean male pediatrician in his late 30s with round glasses and white lab coat smiling warmly and waving hand gently directly at camera. Bright soft realistic medical clinic background, cozy natural sunlight, photorealistic cinematic video, 8k resolution, warm cozy atmosphere`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점 사진, 소아과 진료실 문을 여는 장면. 둥근 안경과 흰색 의사 가운을 입은 30대 후반의 친근한 한국인 남성 소아과 의사가 카메라를 정면으로 바라보며 따뜻하게 미소 지으며 부드럽게 손을 흔든다. 밝고 부드러운 실사 소아과 병원 배경, 포근한 자연 햇살, 실사 영화 영상 스타일, 8k 화질, 따뜻하고 포근한 분위기`

---

### 🎬 Video_Idle: (공용) 선택 대기용 루프
* **상황:** 선택지 선택을 기다리거나 QTE 입력을 기다리는 동안 자연스럽게 재생되는 대기 비디오.
* **권장 클립 길이:** **4초 (AI 최소 클립 길이 4초 준수 / Seamless Ping-Pong Loop 권장)**
  * *팁: 대부분의 AI 비디오 생성 툴(Kling, Runway, Luma)은 최소 생성 길이가 4초/5초입니다. 따라서 AI로는 4초 클립을 생성한 뒤 유니티(Unity)에서 그대로 무한 반복(Looping)하거나, 4초 비디오를 정방향->역방향(Ping-Pong Loop)으로 이어 붙여 끊김 없이 연출합니다.*
* **시각 연출 (콘티):**
  * `0.0s - 4.0s`: 의사 선생님이 다정한 미소를 유지한 채 가볍게 숨을 쉬고 Eye blinking(눈 껌뻑임)을 1~2회 수행. 큰 몸짓 없이 잔잔하게 움직여 루프 시 자연스러움 유지.
* **카메라 워크:** 삼각대 고정 샷 (Static POV Shot).
* **AI 생성 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV photorealistic video, a friendly Korean male pediatrician waiting with a gentle warm smile, subtle natural eye blinking and slow breathing, static tripod shot, realistic warm pediatric clinic background, photorealistic cinema quality, seamless 4-second video`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점 실사 비디오, 다정하고 따뜻한 미소를 지으며 기다리는 친근한 한국인 남성 소아과 의사, 자연스럽고 미세한 눈 껌뻑임과 천천히 숨쉬는 움직임, 삼각대 고정 카메라 샷, 실감나고 따뜻한 소아과 진료실 배경, 실사 영화 화질, 자연스러운 4초 영상`


---

### 🎬 Video_B: [친밀함] 청진기 보여주기 (Trust >= 50 분기)
* **상황:** 아이의 신뢰도가 높아 의사 선생님이 귀여운 청진기를 꺼내 보이며 친근하게 다가옴.
* **권장 클립 길이:** **5초**
* **시각 연출 (콘티):**
  * `0.0s - 2.0s`: 의사 선생님이 책상 위에서 공룡 모양 장식이 달린 알록달록한 청진기를 들어 올림.
  * `2.0s - 5.0s`: 청진기를 카메라(아이) 쪽으로 가까이 내밀며 "이것 봐, 귀여운 공룡 청진기야! 한번 만져볼래?" 하고 친근하게 유도. (마지막 프레임에서 QTE 터치 영역 활성화)
* **카메라 워크:** Medium Shot에서 청진기 중심으로 클로즈업.
* **AI 생성 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV photo, a real friendly male Korean pediatrician holding up a cute toy dinosaur stethoscope towards the camera. Gentle smiling realistic face, inviting and reassuring gesture, photorealistic lighting, cinematic depth of field, 5 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점 사진, 귀여운 공룡 장난감 청진기를 카메라 쪽으로 들어 올려 보여주는 친근한 실제 한국인 남성 소아과 의사. 부드럽게 미소 짓는 실사 얼굴, 다정하고 안심시키는 제스처, 실사 조명, 영화 같은 심도 표현, 5초`

---

### 🎬 Video_C: [불안함] 곰돌이 인형으로 달래기 (Trust < 50 분기)
* **상황:** 아이의 불안도가 높아 의사 선생님이 곰돌이 손인형을 꺼내 아이의 긴장을 풀어주려고 함.
* **권장 클립 길이:** **5초**
* **시각 연출 (콘티):**
  * `0.0s - 2.5s`: 의사 선생님이 푹신한 곰돌이 손인형을 손에 끼우고 천천히 인사를 시킴.
  * `2.5s - 5.0s`: 곰돌이 인형을 카메라 쪽으로 살짝 내밀며 곰돌이가 고개를 까딱거림 ("곰돌이가 인사하네~ 코 한번 쿡 찍어볼까?"). (마지막 프레임에서 QTE 터치 영역 활성화)
* **카메라 워크:** Eye-level 1인칭 POV, 느리고 부드러운 움직임.
* **AI 생성 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV realistic shot, a kind male Korean pediatrician holding a soft fluffy teddy bear hand puppet, gently moving the bear to wave hello at camera to calm a child. Soft patient expression, bright warm clinic background, photorealistic cinematic quality, 5 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점 실사 샷, 푹신하고 귀여운 곰돌이 손인형을 들고 있는 친절한 한국인 남성 소아과 의사, 불안해하는 아이를 달래기 위해 곰돌이를 부드럽게 움직여 카메라에 인사시키는 모습. 부드럽고 인내심 있는 표정, 밝고 따뜻한 진료실 배경, 실사 영화 화질, 5초`

---

### 🎬 Video_D: 진료 성공 & 스티커 보상 (최종 엔딩)
* **상황:** QTE 미션을 마치고 진료를 무사히 마친 후 의사 선생님이 칭찬하며 반짝이는 스티커를 선물로 내묾.
* **권장 클립 길이:** **4초**
* **시각 연출 (콘티):**
  * `0.0s - 2.0s`: 의사 선생님이 아주 밝게 웃으며 엄지척(Thumbs up) 포즈를 취함.
  * `2.0s - 4.0s`: 귀여운 동물 캐릭터 모양의 빛나는 칭찬 스티커를 화면(카메라) 바로 앞까지 손으로 내밀며 보상 전달.
* **카메라 워크:** 카메라 쪽으로 스티커가 다가오는 Close-Up 연출, 주변에 축하 이펙트/밝은 조명.
* **AI 생성 프롬프트:**
  * **[영문 입력용]:**
    > `First-person POV, a joyful real male Korean pediatrician giving a big warm smile and a clear thumbs up, holding out a cute shiny star reward sticker directly towards the camera lens. Celebration feeling, warm sunlight, photorealistic 8k, cinematic camera, 4 seconds`
  * **[한글 해석 및 전달 의미]:**
    > `1인칭 시점, 밝고 환한 미소와 명확한 엄지척 제스처를 취하는 기쁜 표정의 실제 한국인 남성 소아과 의사, 귀엽고 반짝이는 별 모양 보상 스티커를 카메라 렌즈 바로 앞까지 손으로 내밀어 주는 모습. 축하하는 분위기, 따뜻한 햇살, 실사 8k 화질, 영화 같은 카메라 연출, 4초`

---

## 5. 블렌더(Blender) 프리비즈(Previz) 제작 가이드

기획서의 씬 연출(카메라 구도, 캐릭터 위치, 애니메이션 타임라인, QTE 터치 시점)을 **블렌더(Blender)**에서 3D 프리비즈(Pre-visualization)로 빠르게 시뮬레이션하여 검증할 수 있습니다.

### 5.1 블렌더 프리비즈의 핵심 역할
1. **POV 카메라 구도 검증:** 1인칭 시점(아이 눈높이)에서 의사/간호사/소품이 카메라 렌즈(35mm~50mm)에 어떻게 잡히는지 사전 체크.
2. **QTE 터치 영역 시점 계산:** 비디오 마지막 프레임에서 청진기나 인형이 정확히 어느 좌표(Screen Space)로 들어오는지 타임라인 키프레임 설계.
3. **AI 비디오 생성용 First Frame 합성 재료:** 블렌더 3D 연출 씬을 단순 렌더링한 뒤 AI 툴(Kling/Runway)의 컨트롤넷(ControlNet/Pose Depth) 입력을 위한 뼈대 컷으로 활용.

---

### 5.2 블렌더 씬 자동 구성 파이썬 스크립트 (Python Automation)

블렌더 실행 후 **`Text Editor`** 탭에서 아래 파이썬 스크립트를 붙여넣고 `Run Script (Alt+P)`를 누르면 **코코링크 소아과 진료실 1인칭 POV 씬, 의사 더미, 청진기/곰돌이 소품더미, 카메라 및 조명**이 자동으로 생성됩니다.

```python
import bpy

def setup_cocolink_previz():
    # 1. 기존 기본 메쉬 초기화
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.name = "CocoLink_Previz"
    scene.render.fps = 30
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080

    # 2. 1인칭 POV 카메라 (아이 시점 높이 1.2m)
    cam_data = bpy.data.cameras.new(name="POV_Camera")
    cam_obj = bpy.data.objects.new("POV_Camera", cam_data)
    scene.collection.objects.link(cam_obj)
    scene.camera = cam_obj
    cam_obj.location = (0, -2.2, 1.2)
    cam_obj.rotation_euler = (1.5708, 0, 0)
    cam_data.lens = 35 # 35mm 자연스러운 1인칭 렌즈

    # 3. 소아과 진료실 배경 더미 (진료 책상 & 뒤 벽)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.75))
    desk = bpy.context.active_object
    desk.name = "Doctor_Desk"
    desk.scale = (1.6, 0.8, 0.75)

    bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 2.0, 2.5))
    wall = bpy.context.active_object
    wall.name = "Clinic_Wall"
    wall.rotation_euler = (1.5708, 0, 0)

    # 4. 의사 선생님 더미 (Doctor Blockout)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=1.4, location=(0, 0.6, 1.3))
    doctor_body = bpy.context.active_object
    doctor_body.name = "Doctor_Body"

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.25, location=(0, 0.6, 2.1))
    doctor_head = bpy.context.active_object
    doctor_head.name = "Doctor_Head"

    # 5. 소품 더미 (청진기 & 곰돌이 인형)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.15, minor_radius=0.03, location=(-0.4, 0.2, 0.8))
    stetho = bpy.context.active_object
    stetho.name = "Prop_Stethoscope"

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(0.4, 0.2, 0.8))
    bear = bpy.context.active_object
    bear.name = "Prop_TeddyBear"

    # 6. 조명 (소아과 포근한 세팅)
    bpy.ops.object.light_add(type='SUN', location=(2, -2, 4))
    sun = bpy.context.active_object
    sun.data.energy = 3.0

    print("CocoLink Previz Scene Ready!")

if __name__ == "__main__":
    setup_cocolink_previz()
```

---

### 5.3 비디오 노드별 블렌더 프리비즈 샷 연출법

| 노드 ID | 클립 타임라인 | 블렌더 키프레임 애니메이션 연출 가이드 |
| :--- | :--- | :--- |
| **Video_A** | 0.0s ~ 4.0s (120f) | POV 카메라는 `(0, -2.5, 1.2)`에서 `(0, -2.2, 1.2)`로 천천히 줌인. 의사 더미 손(`Doctor_Body` 상단)을 `Z축`으로 45도 회전시켜 인사 동작 애니메이션 키 삽입. |
| **Video_Idle** | 0.0s ~ 4.0s (120f) | POV 카메라 고정. 의사 더미 머리(`Doctor_Head`)를 Z축으로 `0.02m`씩 천천히 위아래로 호흡 애니메이션 적용 (Looping). |
| **Video_B** | 0.0s ~ 5.0s (150f) | `0~60f`: 청진기 더미(`Prop_Stethoscope`)가 책상에서 일어남. <br>`60~150f`: 청진기 더미가 카메라 시점 바로 앞 `(0, -1.0, 1.1)` 위치까지 커지며 다가옴 (QTE 좌표 확보). |
| **Video_C** | 0.0s ~ 5.0s (150f) | `0~75f`: 곰돌이 인형 더미(`Prop_TeddyBear`)가 등장하여 고개 좌우 흔듦. <br>`75~150f`: 곰돌이 코가 화면 중앙 `(0, -1.2, 1.1)`으로 다가옴 (QTE 코 터치 좌표 확보). |
| **Video_D** | 0.0s ~ 4.0s (120f) | 의사 더미 상체를 카메라 앞으로 살짝 기울이고, 스티커 판 더미를 화면 전체로 클로즈업. |



