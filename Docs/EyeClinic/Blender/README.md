# Blender 5.2 기반 CocoLink 소아 안과 3D 프리비즈(Previs) 제작 가이드

본 문서는 **Step 3 (3D 모델링 시연: 곰돌이 턱받침 & 열기구 보기)** 및 **Step 4 (1인칭 실사 촬영용 카메라 앵글)** 프리비즈를 블렌더에서 쉽고 빠르게 구성하는 가이드입니다.

---

## 📂 폴더 구조

```
d:\Github\Unity\cocolink\Docs\EyeClinic\Blender\
├── scripts/
│   └── setup_eyeclinic_previs.py   # 1초 만에 기본 씬(방, 검사기, 코코, 카메라)을 완성하는 자동화 스크립트
├── assets/                         # .blend 파일 및 3D 모델 (.obj / .fbx)
└── renders/                        # 프리비즈 렌더 이미지 및 프리뷰 영상 (.mp4)
```

---

## 🚀 1분 퀵스타트 (원클릭 씬 생성)

1. **블렌더(Blender 5.2)** 실행
2. 상단 메뉴 탭에서 **`Scripting`** 선택
3. **`Open`** 버튼을 누르고 아래 스크립트 선택:
   * 파일 경로: [`d:\Github\Unity\cocolink\Docs\EyeClinic\Blender\scripts\setup_eyeclinic_previs.py`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/scripts/setup_eyeclinic_previs.py)
4. 상단의 **`Run Script` (단축키: `Alt + P`)** 클릭!
5. **결과:**
   * 🏥 **안과 예비검사실 방 & 바닥 & 조명** 자동 배치
   * 🎈 **소아용 자동굴절검사기(턱받침대, 렌즈, 책상)** 생성
   * 🐻 **노란 스카프를 맨 3D 곰돌이 코코(블록아웃)** 착석
   * 🎥 **프리비즈 전용 카메라(16:9, 1080p, 24fps)** 자동 조준 완료!

---

## 🎬 프리비즈 핵심 카메라 앵글 3종 (Lens Setup)

블렌더에서 `Numpad 0`을 누르면 카메라 뷰로 전환됩니다. 씬 내에서 카메라를 복제(`Shift + D`)하여 3가지 핵심 앵글을 잡을 수 있습니다:

1. **카메라 1 [Step 3용 - 3인칭 쿼터 뷰]:**
   * 위치: `X: 2.2m, Y: -1.2m, Z: 2.0m` (Focal Length: 50mm)
   * 용도: 곰돌이 코코가 턱을 올리고 씩씩하게 열기구를 바라보는 전체 시연 샷
2. **카메라 2 [Step 4용 - 1인칭 아이 눈높이 POV]:**
   * 위치: `X: 0m, Y: 0.8m, Z: 1.62m` (Focal Length: 28mm~35mm 광각)
   * 용도: 아이의 눈앞에 턱받침이 다가오고 기계 렌즈를 마주하는 1인칭 샷
3. **카메라 3 [렌즈 내부 POV - 열기구 화면]:**
   * 기계 렌즈 안쪽에서 빨간 열기구가 선명해지는 시각 연출

---

## 💾 파일 저장 및 렌더링

* **프로젝트 저장:** `File` ➔ `Save As` ➔ [`d:\Github\Unity\cocolink\Docs\EyeClinic\Blender\assets\eyeclinic_previs_v01.blend`](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/Blender/assets/eyeclinic_previs_v01.blend) 로 저장
* **빠른 프리뷰 렌더:** `Render` ➔ `Render Image` (`F12`) / 뷰포트에서 `Viewport Shading (Z -> Material Preview)` 켜기
