# [기획서] 코코링크(CocoLink) 소아 안과 샘플 에피소드
## : AI 기반 인터랙티브 안과 경험 훈련 (Eye Clinic MVP)

---

## 1. 개요 및 기획 배경

* **프로젝트명:** 코코링크 (CocoLink) - 안과 에피소드
* **목표:** 낯선 검사 기계(자동굴절기, 안압계), 어두운 진료실, 안압 바람, 안약에 대한 공포감이 높은 아동(자폐스펙트럼, 발달지연, 유아)을 위한 시각적·행동적 사전 적응(Desensitization) 인터랙티브 비디오 훈련.
* **핵심 점진적 실사화 파이프라인:**
  1. **Step 1:** `2D 파스텔 수채화 동화` (병원은 눈을 시원하게 해주는 안전한 곳이라는 개념 형성)
  2. **Step 2:** `2D 단순 UI 일정표` (언제 집에 가는지 직관적 시각 안내)
  3. **Step 3:** `3D 캐주얼 모델링 시연` (입체 기계에 턱을 대고 열기구를 체험하는 완충 브릿지)
  4. **Step 4:** `1인칭 실사 비디오` (PECS 카드 선택 + 감각 사전 예고 + QTE)

---

## 2. 캐릭터 및 핵심 상태 변수 (State Machine)

### 2.1 주요 캐릭터
* **아기 곰돌이 '코코':** 노란 스카프를 착용한 귀여운 갈색 곰돌이 (Step 1의 2D와 Step 3의 3D에서 동일한 외형/아이템 유지).
* **안과 의사 선생님:** 온화하고 친절한 소아 안과 전문의 (Step 4 실사 1인칭 연출).
* **검안사/간호사 선생님:** 상냥하고 유쾌한 소아 안과 검안사.
* **아이 (사용자):** 1인칭 관찰자 및 당사자.

#### 🎨 캐릭터 일관성 유지용 턴어라운드 시트 (Model Sheet)
* 2D 동화 코코: `Graphic/eyeclinic/2d_storybook/coco_bear_bonobono_style.jpg`
* 3D 캐주얼 코코: `Graphic/eyeclinic/3d_animation/coco_bear_3d_turnaround.png`
* 실사 안과 의사: `Graphic/eyeclinic/real/real_eye_doctor_turnaround.png`
* 실사 검안사: `Graphic/eyeclinic/real/real_optometrist_nurse_turnaround.png`

### 2.2 누적 상태 변수 (State)
```json
{
  "eye_doctor_trust": 30,   // 의사/검안사 선생님과의 친밀도 (범위: 0 ~ 100, 초기값: 30)
  "anxiety_level": 50       // 아동의 심리적 불안도 (범위: 0 ~ 100, 초기값: 50)
}
```

---

## 3. 핵심 안과 에피소드 비디오 클립 흐름

1. `Step 1 (2D 동화)`: 눈이 침침해요 ➔ 안과 소개 ➔ 별 안경 선물
2. `Step 2 (2D 일정표)`: 5단계 UI 상시 노출 (`입구 ➔ 접수 ➔ 기계 ➔ 진료 ➔ 보상`)
3. `Step 3 (3D 시연)`: 턱받침 대기 ➔ 🎈 열기구 보기 ➔ 별 선글라스 획득
4. `Step 4 (1인칭 실사)`:
   * `C1_Arrive`: 안과 입장 & 검안사 손인사 (선택: 인사 vs 숨기)
   * `C2_Reception & WaitingRoom`: 접수 & 그림 시력표 동물 찾기 탐색
   * `C3_ChinRest & BalloonView`: 턱 대기 3초 유지 QTE & 🎈 열기구 보기
   * `C4_ChartMatch`: PECS 그림 시력표 맞추기 (🦆 오리 / 🦋 나비 / 🚗 차)
   * `C5_DoctorGreet & SlitLamp`: 진료실 입장 & 💡 불빛/세극등 검사
   * `C6_Reward & Farewell`: 멋진 별 선글라스 스티커 획득 & 작별 인사

상세 프롬프트 및 비디오 대본은 [full_episode_scenario.md](file:///d:/Github/Unity/cocolink/Docs/EyeClinic/full_episode_scenario.md) 참조.
