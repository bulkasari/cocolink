# [시나리오 기획서] CocoLink 풀 에피소드: 소아과 병원 방문 전체 여정
## : 사회성 발달 지원 아동을 위한 단계별 병원 적응 시나리오

> **대상:** 자폐스펙트럼(ASD), 발달지연, 사회불안이 높은 유아·아동 (3~9세)
> **핵심 목표:** 병원 방문의 전 과정을 순서대로, 천천히, 예측 가능하게 경험시켜 실제 병원에 대한 공포를 낮추고 사회적 행동 패턴(인사, 대기, 검사 협조)을 학습하게 한다.

---

## 1. 전체 에피소드 구조 (Journey Map)

> 실제 소아과 방문 흐름을 6개 챕터로 나누어 촘촘하게 구성합니다.

```
[챕터 1] 병원 도착 & 입구 → [챕터 2] 접수 & 대기실 → [챕터 3] 이름 호명 & 입장
     → [챕터 4] 진료실 의사 인사 → [챕터 5] 진료 과정 (검사) → [챕터 6] 스티커 보상 & 귀가
```

---

## 2. 캐릭터 목록

| 캐릭터 | 역할 | 외형 | 참조 이미지 |
| :--- | :--- | :--- | :--- |
| **의사 선생님** | 30대 후반 남성 소아과의사 | 흰 가운, 둥근 안경, 따뜻한 미소 | `Docs/pediatrician_turnaround.png` |
| **간호사 선생님** | 20대 후반 여성 소아과간호사 | 파스텔 핑크 스크럽, 단정한 머리 | `Docs/nurse_turnaround.png` |
| **엄마/보호자** | 아이 동행 보호자 (화면 밖 목소리 or 손 등장) | 따뜻한 손, 목소리 | (텍스트/목소리 연출) |

---

## 3. 누적 상태 변수 (State Machine)

```json
{
  "doctor_trust":  30,   // 의사 신뢰도     (0~100, 초기 30)
  "nurse_trust":   20,   // 간호사 신뢰도   (0~100, 초기 20)
  "anxiety_level": 60,   // 불안도          (0~100, 초기 60)
  "cooperation":   10,   // 검사 협조도     (0~100, 초기 10)
  "badge_count":    0    // 획득한 스티커 수 (0~5)
}
```

---

## 4. 챕터별 상세 시나리오

---

### 📍 챕터 1: 병원 도착 & 입구

**씬 설명:** 아이(1인칭 POV)가 엄마 손을 잡고 소아과 건물 입구 앞에 서있음. 자동문이 열린다.

**클립 ID:** `C1_Arrive`
**클립 길이:** 5초
**콘티:**
- `0s~2s`: 소아과 건물 외벽, 귀여운 동물 벽화가 그려진 입구. 자동문이 열리며 따뜻한 실내 공기가 느껴짐.
- `2s~5s`: 화면이 실내로 전환되며 간호사 선생님이 입구 데스크 너머로 손을 흔들어 환영함.

**선택지 등장:**

| 번호 | 선택지 | 상태 변화 | 분기 |
| :--: | :--- | :--- | :--- |
| 1 | 🙌 손 흔들어 인사하기 | nurse_trust +15 / anxiety -10 | → C1_HiPath |
| 2 | 😶 가만히 서있기 | 변화 없음 | → C1_WaitPath |
| 3 | 🙈 엄마 뒤로 숨기 | anxiety +15 | → C1_HidePath |

**분기 클립:**
- `C1_HiPath`: 간호사 선생님이 밝게 웃으며 "어서 와~ 잘 왔어!" 엄지척
- `C1_WaitPath`: 간호사 선생님이 다정하게 "와줘서 고마워~ 안으로 들어와도 돼!"
- `C1_HidePath`: 간호사 선생님이 곰돌이 인형을 꺼내며 "괜찮아, 곰돌이도 같이 왔어~"

**스몰 배지 조건:** 선택 1 선택 시 ⭐ 미니 배지 획득 ("용감한 인사왕!")
**다음 챕터로:** 모든 분기 → 챕터 2

---

### 📍 챕터 2: 접수 & 대기실

**씬 설명:** 접수 창구 앞. 간호사 선생님이 이름을 물어본다. 이후 대기실에서 기다리는 장면.

#### 2-A: 접수 창구

**클립 ID:** `C2_Reception`
**클립 길이:** 5초
**콘티:**
- `0s~2.5s`: 간호사 선생님이 창구 너머에서 "이름이 뭐예요?" 하고 친절하게 물어봄.
- `2.5s~5s`: 진료 카드를 받아들이며 "자, 이거 들고 저쪽에서 기다려 줄 수 있어?"라고 안내.

**선택지 (목소리 반응):**

| 번호 | 선택지 | 상태 변화 |
| :--: | :--- | :--- |
| 1 | 🗣️ 내 이름 말하기 | nurse_trust +15 / cooperation +10 |
| 2 | 😐 엄마가 대신 말하게 하기 | anxiety -5 (편안함) |
| 3 | 🤐 고개 끄덕이기 | nurse_trust +5 |

**피드백 클립:** 어떤 선택이든 간호사는 "잘했어! 대기실에서 기다려줘~" → 긍정 강화 일관 유지

#### 2-B: 대기실 기다리기

**클립 ID:** `C2_WaitingRoom`
**클립 길이:** 6초
**씬 설명:** 알록달록한 소아과 대기실. 어항, 장난감 바구니, 그림책이 보임.

**콘티:**
- `0s~2s`: 1인칭으로 대기실 의자에 앉는 시점. 옆에 엄마가 앉아 있음(손만 보임).
- `2s~6s`: 대기실을 천천히 둘러봄. 다른 아이가 그림책 보는 모습, 어항 물고기 움직임.

**인터랙션 (탐색 미션):**
- 화면에 3개의 탐색 포인트가 순차적으로 표시됨
  - 🐟 어항 물고기 터치 → "어, 물고기가 반갑다고 헤엄쳤어!"
  - 📚 그림책 터치 → "병원 그림책이네~ 나중에 읽어볼까?"
  - ⏰ 시계 터치 → "조금만 기다리면 선생님이 불러줄 거야!"

**다음 챕터 조건:** 탐색 1개 이상 완료 시 → 챕터 3

---

### 📍 챕터 3: 이름 호명 & 진료실 입장

**씬 설명:** 간호사 선생님이 이름을 부른다. 아이가 일어나서 진료실로 걸어가는 장면.

**클립 ID:** `C3_NameCall`
**클립 길이:** 5초
**콘티:**
- `0s~2s`: 간호사 선생님이 문 앞에서 아이 이름을 부르며 손짓("이쪽으로 와도 돼~").
- `2s~5s`: 1인칭으로 복도를 걸어 진료실 문 앞까지 다가가는 POV 워크.

**선택지 (이동 방식):**

| 번호 | 선택지 | 상태 변화 |
| :--: | :--- | :--- |
| 1 | 🚶 혼자 먼저 걸어가기 | cooperation +15 / anxiety -10 |
| 2 | 🤝 엄마 손 잡고 걸어가기 | anxiety -5 |
| 3 | 🐢 천천히 따라가기 | 변화 없음 |

**중요 포인트:** 어떤 선택이든 "도착했어! 잘 왔어!" 긍정 강화 → 모든 선택이 정답임을 학습

---

### 📍 챕터 4: 진료실 입장 & 의사 선생님 인사

> 기존 MVP 시나리오 Video_A와 동일 구조, 더 세분화

**씬 설명:** 진료실 문이 열리고 의사 선생님이 맞이한다.

**클립 ID:** `C4_DoctorGreet`
**클립 길이:** 5초
**콘티:**
- `0s~2s`: 진료실 문이 열리며 밝고 포근한 진료실 내부 등장. 의사 선생님이 카메라 방향으로 환하게 웃으며 손을 흔듦.
- `2s~5s`: "어서 와~ 이 의자에 앉아볼까?" 의자를 손으로 가리키며 안내.

**선택지 (반응):**

| 번호 | 선택지 | 상태 변화 |
| :--: | :--- | :--- |
| 1 | 👋 "안녕하세요!" 인사하기 | doctor_trust +20 / anxiety -15 |
| 2 | 😶 가만히 앉기 | anxiety -5 |
| 3 | 🙈 문 앞에서 잠깐 멈추기 | anxiety +5 → 간호사 등장해서 도움 |

**분기 (선택 3 특별 분기):**
- 간호사 선생님이 뒤에서 다가와 "괜찮아~ 선생님이 정말 친절해! 같이 들어갈까?" → cooperation +5

**상태 조건 분기:**
- `doctor_trust ≥ 50` & `anxiety ≤ 50` → 챕터 5-A (쉬운 진료 루트)
- `doctor_trust < 50` or `anxiety > 50` → 챕터 5-B (달래기 진료 루트)

---

### 📍 챕터 5-A: 진료 과정 (신뢰 루트 — 청진기·구강 검사)

**씬 설명:** 아이가 비교적 편안한 상태. 의사 선생님이 순서대로 진료를 진행.

#### 5-A-1: 청진기 검사

**클립 ID:** `C5A_Stethoscope`
**클립 길이:** 6초
**콘티:**
- `0s~2s`: 의사 선생님이 공룡 장식 청진기를 먼저 자신의 손목에 대서 "차갑지 않아~ 따뜻해져서 대볼게" 시연.
- `2s~6s`: 청진기를 화면(아이 시점)쪽으로 천천히 가져옴 "조금만 가만히 있어줄 수 있어?"

**QTE 미션:** 청진기 터치 → "참 잘했어! 심장 소리가 들려~ 두근두근!" → cooperation +20

**단계 설명 클립(선택적):**
- 의사 선생님: "청진기로 심장 소리를 들어보는 거야. 아프지 않아~" (검사 의미 설명 → 예측 가능성 제공)

#### 5-A-2: 구강 검사 (목 들여다보기)

**클립 ID:** `C5A_Throat`
**클립 길이:** 5초
**콘티:**
- `0s~2s`: 의사 선생님이 손에 작은 손전등을 들고 "입 안 조금만 볼게~ 아~ 해줄 수 있어?"
- `2s~5s`: 화면 아래 "아~" 버튼이 등장. 누르면 의사 선생님이 "잘했어! 목이 건강해~" 반응.

**QTE 미션 (타이밍):** '아~' 버튼 → cooperation +15

#### 5-A-3: 귀 검사

**클립 ID:** `C5A_Ear`
**클립 길이:** 4초
**콘티:**
- `0s~1.5s`: 의사 선생님이 이경(귀 검사 기구)을 보여주며 "이걸로 귀 안을 비춰볼게, 간지럽진 않아~"
- `1.5s~4s`: 귀 쪽으로 천천히 다가오는 장면.

**QTE 미션:** 화면 유지(가만히 있기) 3초 → cooperation +15

---

### 📍 챕터 5-B: 진료 과정 (달래기 루트 — 인형 매개 진료)

**씬 설명:** 아이가 불안한 상태. 간호사 선생님이 함께 들어와 곰돌이 인형을 매개로 진료를 진행.

#### 5-B-1: 곰돌이 인형 먼저 진료하기

**클립 ID:** `C5B_BearFirst`
**클립 길이:** 6초
**콘티:**
- `0s~3s`: 의사 선생님이 곰돌이 인형을 간호사에게서 받아 "곰돌이 먼저 검사해줄게~" 하며 곰돌이 가슴에 청진기 대어줌.
- `3s~6s`: "곰돌이 심장 소리 들렸어! 이번엔 네 차례야~ 할 수 있어?"

**선택지:**

| 번호 | 선택지 | 상태 변화 |
| :--: | :--- | :--- |
| 1 | ✅ 네! 해볼게요 | cooperation +20 / anxiety -20 → 5-A 루트로 합류 |
| 2 | 🤔 조금 더 보기 | 의사 한 번 더 시연 후 재시도 |

#### 5-B-2: 호흡 연습 게임

**클립 ID:** `C5B_Breathing`
**클립 길이:** 5초
**씬 설명:** 불안 완화를 위한 복식호흡 미니 미션.

**콘티:**
- `0s~5s`: 의사 선생님이 "우리 같이 풍선 부는 연습 해볼까? 코로 들이마시고~ 입으로 후~!"

**QTE 미션 (호흡 게임):**
- 화면 중앙에 풍선 아이콘 등장
- 누르고 있으면 풍선이 부풀어 오름 → 3초 유지
- 성공 시: anxiety -25 / cooperation +10

---

### 📍 챕터 6: 보상 & 귀가 준비

#### 6-A: 스티커 보상

**클립 ID:** `C6_Reward`
**클립 길이:** 5초
**콘티:**
- `0s~2s`: 의사 선생님이 환하게 웃으며 엄지척 "정말 잘했어! 용감한 어린이야!"
- `2s~5s`: 반짝이는 별 / 공룡 / 하트 모양 스티커 3가지를 화면에 내밀며 "어떤 거 좋아?"

**선택 인터랙션:** 스티커 3종 중 하나 터치 → badge_count +1 → 선택한 스티커가 화면에 붙는 애니메이션

#### 6-B: 의사 선생님 작별 인사

**클립 ID:** `C6_Farewell`
**클립 길이:** 4초
**콘티:**
- `0s~4s`: 의사 선생님이 "다음에 또 와! 선생님이 기다릴게~" 하며 손 흔들어 작별 인사.

**선택지:**

| 번호 | 선택지 | 상태 변화 |
| :--: | :--- | :--- |
| 1 | 👋 손 흔들어 작별인사 | doctor_trust +10 (최종 기록) |
| 2 | 😄 웃으며 고개 숙이기 | doctor_trust +5 |
| 3 | 😶 그냥 문 나가기 | 변화 없음 |

#### 6-C: 엔딩 결과 화면 (Episode Result Screen)

에피소드 종료 후 최종 상태값을 기반으로 맞춤 피드백 표시.

| 조건 | 메시지 | 배지 |
| :--- | :--- | :--- |
| doctor_trust ≥ 70 | "의사 선생님이랑 아주 친해졌어요! 다음엔 더 즐겁게 갈 수 있어요!" | 🏆 병원 친구 배지 |
| cooperation ≥ 60 | "검사를 아주 잘 협조했어요! 용감한 어린이예요!" | ⭐ 용감한 환자 배지 |
| anxiety ≤ 30 | "병원이 무섭지 않았죠? 정말 씩씩했어요!" | 💪 씩씩이 배지 |
| badge_count ≥ 3 | "스티커 수집왕! 다음 에피소드도 도전해보세요!" | 🎖 수집왕 배지 |

---

### 📍 챕터 5-C: 주사 맞기 (선택 에피소드 — 가장 촘촘한 공포 완화 설계)

> **⚠️ 주의:** 주사는 아동이 가장 강렬하게 공포를 느끼는 경험입니다.  
> 이 챕터는 **5단계 공포 완화 + 통증 예측 + 성공 경험**의 순서로 설계합니다.  
> **절대 속이거나 "안 아프다"고 하지 않습니다.** ("조금 따끔할 수 있어" 솔직한 설명이 신뢰를 높입니다.)

---

#### 5-C-0: 주사 필요 사전 예고 (안내 화면)

**클립 ID:** `C5C_Notice`
**클립 길이:** 5초
**씬 설명:** 의사 선생님이 부드럽게 예방접종이 필요하다고 미리 알려주는 장면.

**콘티:**
- `0s~2s`: 의사 선생님이 진지하지만 다정하게 "오늘 건강해지는 데 도움이 되는 주사를 맞아야 해. 미리 알려줄게~"
- `2s~5s`: 화면에 주사기 일러스트(귀엽게 캐릭터화된) + "준비가 되면 알려줘!" 문구 표시.

**선택지 (마음 준비 확인):**

| 번호 | 선택지 | 상태 변화 |
| :--: | :--- | :--- |
| 1 | 💪 준비됐어요! | anxiety -5 / cooperation +10 |
| 2 | 😰 조금 무서워요 | → 5-C-1 달래기 루트 진입 |
| 3 | 😭 싫어요! 무서워요! | → 5-C-1 달래기 루트 + 특별 간호사 지원 등장 |

---

#### 5-C-1: 주사 도구 먼저 보여주기 (탈감작화 — Desensitization)

**클립 ID:** `C5C_ShowTools`
**클립 길이:** 6초
**씬 설명:** 간호사 선생님이 주사와 관련된 도구들을 하나씩 먼저 보여주며 익숙하게 만들어 줌.

**콘티:**
- `0s~2s`: 간호사 선생님이 쟁반에 담긴 도구를 가리키며 "이게 뭔지 알아?" 하고 궁금하게 소개.
  - 알코올 솜: "이건 피부를 깨끗하게 닦아주는 솜이야. 차갑고 시원해~"
  - 반창고: "이건 다 끝나고 붙여주는 거야. 어떤 그림 붙여줄까?"
  - 주사기: "이게 주사야. 빠르게 들어갔다가 금방 끝나~"

**인터랙션:** 도구 3개 순서대로 터치해서 설명 듣기 (탐색 미션)
- 각 도구 터치 → 짧은 애니메이션 + 친절한 설명 → anxiety -5씩

---

#### 5-C-2: 호흡 준비 미션 (주사 전 진정 호흡)

**클립 ID:** `C5C_BreathPre`
**클립 길이:** 6초
**씬 설명:** 간호사 선생님이 주사 맞기 전 호흡법을 함께 연습.

**콘티:**
- `0s~6s`: 간호사 선생님이 "주사 맞을 때 이렇게 하면 덜 무서워~ 나랑 같이 해보자!"
  - 코로 천천히 들이마시기 3초 → 입으로 후~ 내쉬기 3초

**QTE 미션 (호흡 게임):**
- 화면에 풍선 아이콘 등장
- 화면 아무 곳이나 길게 누르면 풍선이 부풀어오름 (3초 유지)
- 손 떼면 풍선이 줄어듦
- 성공 시: anxiety -20 / "잘했어! 이렇게 숨을 쉬면 훨씬 나아~"

---

#### 5-C-3: 팔 선택 & 위치 자율권 부여 (자율 통제감)

**클립 ID:** `C5C_ArmChoice`
**클립 길이:** 4초
**씬 설명:** 간호사 선생님이 어느 팔에 맞을지 아이가 선택하게 해줌 → 상황 통제감 제공.

**콘티:**
- `0s~4s`: 간호사 선생님이 "어떤 팔에 맞을래? 이쪽 팔? 저쪽 팔?" 하며 양손을 번갈아 가리킴.

**선택지:**

| 번호 | 선택지 | 상태 변화 |
| :--: | :--- | :--- |
| 1 | 🦾 오른팔 선택 | cooperation +10 / anxiety -10 |
| 2 | 💪 왼팔 선택 | cooperation +10 / anxiety -10 |

> **설계 의도:** 실제 의료적으로 어느 팔이든 상관없을 때 아이에게 선택권을 주면 통제감이 생겨 협조율이 크게 높아집니다. (실제 ASD 아동 의료 지침 기반)

---

#### 5-C-4: 알코올 솜 닦기 (사전 감각 예고)

**클립 ID:** `C5C_AlcWipe`
**클립 길이:** 5초
**씬 설명:** 간호사 선생님이 알코올 솜으로 팔을 닦아주기 전에 먼저 "차가울 거야"라고 예고.

**콘티:**
- `0s~2s`: 간호사 선생님이 "자, 지금 솜으로 닦을게~ 차갑고 시원할 거야!" 하고 솜을 보여줌.
- `2s~5s`: 솜이 화면(팔 시점)으로 천천히 다가오는 연출.

**QTE 미션:** 화면 고정 (3초 가만히) → "잘 참았어! 다음은 주사야~"
- 성공: cooperation +10

---

#### 5-C-5: 주사 맞기 (핵심 장면 — 가장 세밀하게 설계)

**클립 ID:** `C5C_Injection`
**클립 길이:** 7초

> **⚠️ 연출 원칙:**
> - "안 아파" 절대 금지. "조금 따끔할 수 있어" 솔직하게 예고.
> - 주사기가 화면에 직접 크게 나타나지 않도록 연출 (공포 자극 최소화).
> - 의사/간호사 얼굴이 함께 보이도록 → 안심 표정 제공.
> - 주사 후 "끝났어!" 즉각 알려주기.

**콘티:**
- `0s~1.5s`: 간호사 선생님이 "자~ 지금 할게. 숨 한번 크게 들이마셔!" 하며 준비 신호.
- `1.5s~2s`: 간호사 선생님이 "후~ 내쉬어~" 하며 같이 호흡 유도.
- `2s~4s`: **[카메라 팔 시점 클로즈업]** 간호사 손이 팔에 닿는 느낌 (주사기는 화면 가장자리 작게) → **딱! 소리 효과**
- `4s~7s`: 간호사 선생님 얼굴이 화면 전체를 채우며 "끝났어!! 정말 잘했어!! 🌟" → 환한 웃음.

**QTE 미션 (버티기 미션):**
- 주사 순간 화면 중앙에 **💪 버튼** 등장
- 누르고 있으면 "참는 중..." 게이지가 차오름 (3초)
- 성공 시: cooperation +25 / anxiety -20 / badge_count +1

**실패 처리 (손 뗄 경우):**
- 간호사 선생님이 "괜찮아~ 움직일 수 있어. 다시 해보자~" 재도전 지원.
- 실패 패널티 없음 (언제든 재시도 가능)

---

#### 5-C-6: 반창고 붙이기 & 즉각 보상

**클립 ID:** `C5C_Bandage`
**클립 길이:** 5초
**씬 설명:** 주사가 끝나고 반창고를 붙이는 의식 → 완료 신호 역할.

**콘티:**
- `0s~2s`: 간호사 선생님이 반창고 여러 종류를 보여주며 "어떤 그림 붙여줄까? 공룡? 별? 하트?"
- `2s~5s`: 선택한 반창고가 팔에 붙여지는 장면 + "이제 다 끝났어! 용감한 어린이야!" 칭찬.

**선택 인터랙션:**
- 🦕 공룡 반창고 | ⭐ 별 반창고 | 💜 하트 반창고 중 터치 선택
- 선택 시 badge_count +1 (특별 반창고 배지)

**주사 후 감정 체크 (감정 표현 학습):**

| 번호 | 지금 기분은? | 처리 |
| :--: | :--- | :--- |
| 😭 많이 아팠어요 | "아팠구나. 잘 참았어! 많이 용감했어~" | 공감 → 위로 |
| 😕 조금 아팠어요 | "맞아, 조금 따끔했지? 정말 씩씩했어!" | 공감 → 칭찬 |
| 😊 괜찮았어요 | "우와! 전혀 안 무서웠어? 최고야!" | 강한 칭찬 |

> **설계 의도:** 감정 표현 선택지는 아이가 자신의 감정을 인식하고 언어화하는 연습이자,  
> "아팠어도 잘한 거야"라는 메시지로 성공 경험을 강화합니다.

---

#### 5-C 클립 목록 요약

| 클립 ID | 장면 | 길이 | 핵심 미션 |
| :--- | :--- | :--- | :--- |
| `C5C_Notice` | 주사 예고 | 5s | 선택지 (준비됐어요/무서워요) |
| `C5C_ShowTools` | 도구 탐색 | 6s | 탐색 3회 터치 |
| `C5C_BreathPre` | 호흡 준비 | 6s | 풍선 QTE (3초 유지) |
| `C5C_ArmChoice` | 팔 선택 | 4s | 왼팔/오른팔 선택 |
| `C5C_AlcWipe` | 알코올 닦기 | 5s | 3초 가만히 QTE |
| `C5C_Injection` | 주사 맞기 | 7s | 💪 버티기 QTE (3초) |
| `C5C_Bandage` | 반창고 선택 | 5s | 반창고 터치 선택 + 감정 표현 |

**챕터 5-C 총 클립 수:** 7개 / **총 시간:** 약 38초 (인터랙션 포함 약 2~3분)

---



```
[C1: 병원 입구 도착]
       │
  ┌────┼────┐
  ▼    ▼    ▼
인사  대기  숨기
  └────┼────┘
       │
[C2-A: 접수 창구]
  이름말하기 / 엄마대신 / 고개끄덕
       │
[C2-B: 대기실]
  어항·책·시계 탐색 미션 (1개 이상)
       │
[C3: 이름 호명 & 입장]
  혼자/엄마손/천천히
       │
[C4: 의사 선생님 인사]
       │
    ┌──┴──┐
    ▼      ▼
Trust≥50  Trust<50
Anx≤50   Anx>50
    │      │
  [C5-A] [C5-B]
청진기    곰돌이 매개
구강 검사 호흡 게임
귀 검사   └→ C5-A 합류
    └──┬──┘
       │
  [C6-A: 스티커 선택]
  [C6-B: 작별인사]
  [C6-C: 결과 화면]
```

---

## 6. 제작 클립 목록 (AI 비디오 생성용)

| 클립 ID | 챕터 | 길이 | 장면 요약 | 화면비율 |
| :--- | :--- | :--- | :--- | :--- |
| C1_Arrive | 1 | 5s | 입구 자동문, 간호사 환영 | 16:9 |
| C1_HiPath | 1-분기 | 3s | 간호사 엄지척 반응 | 16:9 |
| C1_HidePath | 1-분기 | 3s | 간호사 곰돌이 꺼내기 | 16:9 |
| C2_Reception | 2 | 5s | 접수 창구 대화 | 16:9 |
| C2_WaitingRoom | 2 | 6s | 대기실 탐색 | 16:9 |
| C3_NameCall | 3 | 5s | 이름 호명 & 복도 걷기 | 16:9 |
| C4_DoctorGreet | 4 | 5s | 의사 인사 & 자리 안내 | 16:9 |
| C5A_Stethoscope | 5-A | 6s | 청진기 시연 & 검사 | 16:9 |
| C5A_Throat | 5-A | 5s | 구강 검사 (아~ 하기) | 16:9 |
| C5A_Ear | 5-A | 4s | 귀 검사 | 16:9 |
| C5B_BearFirst | 5-B | 6s | 곰돌이 먼저 진료 | 16:9 |
| C5B_Breathing | 5-B | 5s | 호흡 연습 게임 | 16:9 |
| C6_Reward | 6 | 5s | 스티커 보상 선택 | 16:9 |
| C6_Farewell | 6 | 4s | 작별 인사 | 16:9 |
| Idle_Nurse | 공용 | 4s (loop) | 간호사 대기 루프 | 16:9 |
| Idle_Doctor | 공용 | 4s (loop) | 의사 대기 루프 | 16:9 |

**총 클립 수: 16개** (분기 클립 포함)

---

## 7. 아동 발달 심리 기반 시나리오 설계 원칙

1. **예측 가능성 (Predictability):** 모든 씬 시작 전 짧은 자막으로 다음에 무슨 일이 일어날지 미리 알려줌 (e.g., "이제 선생님이 귀를 볼 거예요").
2. **긍정 강화 일관성 (Positive Reinforcement):** 어떤 선택을 해도 부정적 피드백 없이 격려하는 반응만 제공.
3. **자율 통제감 (Sense of Control):** 선택지를 통해 아이가 상황을 통제한다는 느낌을 줌.
4. **점진적 노출 (Gradual Exposure):** 가장 덜 무서운 것(입구·인사)부터 가장 무서운 것(검사)까지 단계적으로 경험.
5. **사회적 모델링 (Social Modeling):** 곰돌이 인형이 먼저 검사를 받는 장면 → 간접 경험으로 공포 완화.
6. **반복 가능한 루프 (Repeatable Loop):** 에피소드를 여러 번 반복할수록 초기값(anxiety)이 점차 낮아지도록 누적 기록.

---

## 8. 전체 클립 AI 비디오 생성 프롬프트 명세

> **공통 설정 (모든 클립 적용):**
> - 화면 비율: `16:9` (Runway/Kling: `16:9`, Midjourney: `--ar 16:9`)
> - 스타일: 실사(Photorealistic), 따뜻하고 친근한 소아과 의원 분위기
> - 참조 이미지: `pediatrician_turnaround.png` (의사), `nurse_turnaround.png` (간호사), `clinic_background.png` (배경)
> - **Image-to-Video 방식**: 각 클립 생성 전 배경+캐릭터 합성 이미지를 First Frame으로 입력
> - **카메라 워크 AI 키워드:** `static shot` (고정), `slow dolly in` (천천히 줌인), `handheld slight wobble` (핸드헬드), `slow pan` (패닝), `close-up` (클로즈업)

---

### 챕터 1 — 병원 도착 & 입구

---

#### 🎬 C1_Arrive — 병원 입구 도착 & 간호사 환영 (5초)
* **카메라 워크:** 천천히 전진하는 Dolly-In (슬로우 달리인) → 입구 자동문이 열리면서 시작되는 POV 이동
* **[영문 입력용]:**
  > `First-person POV, child's height eye-level, slow dolly-in movement approaching a bright warm Korean pediatric clinic entrance. Automatic glass doors slide open revealing a cheerful colorful interior. A friendly female Korean pediatric nurse in pastel pink scrubs stands behind the reception desk, smiling warmly and waving hand gently directly at the camera. Slow steady forward camera movement, photorealistic cinematic quality, warm soft lighting, 16:9, 5 seconds`
* **[한글 해석]:**
  > `아이 눈높이 1인칭 POV. 카메라가 천천히 앞으로 이동(달리인)하며 밝고 따뜻한 한국 소아과 병원 입구로 다가가는 장면. 유리 자동문이 열리며 알록달록한 실내가 보임. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 접수대 너머에서 따뜻하게 웃으며 카메라를 정면으로 바라보고 손을 흔들어 환영함. 느리고 안정적인 전진 카메라 이동. 실사 영화 화질, 따뜻한 조명, 5초`

---

#### 🎬 C1_HiPath — 인사 반응: 간호사 엄지척 (3초)
* **카메라 워크:** 고정 샷 (Static Shot) — 흔들림 없이 인물 정면 고정
* **[영문 입력용]:**
  > `First-person POV, static camera shot, a friendly Korean female pediatric nurse in pastel pink scrubs looking directly into the camera lens with a big warm smile, giving a clear enthusiastic thumbs up gesture toward the camera, bright cheerful pediatric clinic background, photorealistic, eye contact with camera, 3 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 카메라 샷. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 카메라 렌즈를 정면으로 바라보며 환하게 웃고 카메라를 향해 선명하게 엄지척을 보여주는 장면. 밝고 화사한 소아과 병원 배경. 카메라와 눈맞춤. 실사 화질, 3초`

---

#### 🎬 C1_HidePath — 숨기 반응: 간호사 곰돌이 꺼내기 (3초)
* **카메라 워크:** 고정 샷 (Static Shot) — 인형이 카메라 쪽으로 다가오는 연출
* **[영문 입력용]:**
  > `First-person POV, static camera shot, a kind Korean female pediatric nurse in pastel pink scrubs gently pulling out a soft fluffy teddy bear plush toy from below frame and presenting it toward the camera lens with a patient warm reassuring smile. Teddy bear moves toward the camera. Soothing calm gesture, photorealistic clinic background, eye contact with camera, 3 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 카메라 샷. 파스텔 핑크 스크럽의 친절한 한국인 여성 간호사가 화면 아래에서 부드러운 곰돌이 인형을 꺼내 카메라 렌즈 방향으로 내밀며 인내심 있고 따뜻한 미소로 안심시키는 장면. 곰돌이가 카메라 쪽으로 다가오는 연출. 카메라와 눈맞춤. 실사 소아과 배경, 3초`

---

### 챕터 2 — 접수 & 대기실

---

#### 🎬 C2_Reception — 접수 창구 대화 (5초)
* **카메라 워크:** 고정 샷 (Static Shot) — 창구 너머 인물과 아이-레벨 고정
* **[영문 입력용]:**
  > `First-person POV at child's eye level, static camera shot, a friendly Korean female nurse behind a bright reception counter leans slightly forward directly toward the camera with a warm smile asking "What's your name?", holding clipboard, handing over a small clinic card toward the camera lens. Eye contact with camera, cozy warm pediatric reception area background, photorealistic cinematic, 5 seconds`
* **[한글 해석]:**
  > `아이 눈높이 1인칭 시점. 고정 카메라 샷. 밝은 접수 창구 너머의 친근한 한국인 여성 간호사가 카메라 쪽으로 직접 몸을 기울이며 따뜻하게 웃으며 "이름이 뭐예요?" 하고 묻고 진료 카드를 카메라 렌즈 쪽으로 건네주는 장면. 카메라와 눈맞춤. 따뜻하고 아늑한 소아과 접수실 배경. 실사 영화 화질, 5초`

---

#### 🎬 C2_WaitingRoom — 대기실 탐색 (6초)
* **카메라 워크:** 느린 좌→우 팬 (Slow Pan Left-to-Right) — 앉은 눈높이에서 대기실 천천히 탐색
* **[영문 입력용]:**
  > `First-person POV seated eye level, slow pan left to right exploring a cozy colorful Korean pediatric waiting room. Camera slowly pans revealing: fish tank with swimming fish on left, small bookshelf with picture books center, colorful children's chairs in foreground, animal wall decals on soft pastel walls. Natural warm lighting, calm welcoming atmosphere, photorealistic cinematic, 6 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 앉은 눈높이. 카메라가 왼쪽에서 오른쪽으로 느리게 패닝하며 아늑하고 알록달록한 한국 소아과 대기실을 탐색. 순서대로 보이는 요소: 왼쪽 벽 어항(물고기 헤엄), 중앙 그림책 책장, 앞쪽 색깔 아동용 의자, 파스텔 벽의 동물 벽화 스티커. 따뜻한 자연 채광, 편안하고 친근한 분위기. 실사 영화 화질, 6초`

---

### 챕터 3 — 이름 호명 & 진료실 입장

---

#### 🎬 C3_NameCall — 이름 호명 & 복도 걷기 (5초)
* **카메라 워크:** 정지 → 달리인 (Hold → Dolly-In Walk) — 간호사 확인 후 POV가 복도를 타고 달리는 연출
* **[영문 입력용]:**
  > `First-person POV at child's eye level. Camera holds still as a friendly Korean female nurse in pink scrubs stands at an open clinic room door smiling and beckoning gently toward the camera. Then camera begins a slow steady dolly-in walking forward down a bright clean corridor toward the open room door, slight natural handheld walking movement, warm pediatric clinic interior, photorealistic, 5 seconds`
* **[한글 해석]:**
  > `아이 눈높이 1인칭 시점. 카메라가 잠시 멈춰 있는 동안 파스텔 핑크 스크럽의 친근한 한국인 간호사가 열린 진료실 문 앞에서 카메라를 향해 따뜻하게 웃으며 손짓으로 안내. 이어서 카메라가 밝고 깨끗한 복도를 따라 진료실 문 쪽으로 천천히 안정적으로 달리인 POV 이동 시작. 자연스러운 양측 이동 흔들림 느낌. 따뜻한 소아과 실내. 실사 화질, 5초`

---

### 챕터 4 — 진료실 의사 선생님 인사

---

#### 🎬 C4_DoctorGreet — 의사 인사 & 자리 안내 (5초)
* **카메라 워크:** 달리인 → 고정 (Dolly-In Reveal → Static) — 문 열리며 들어가다가 의사 앞에서 정지
* **[영문 입력용]:**
  > `First-person POV, camera slowly pushes forward as a clinic room door opens revealing a warm bright Korean pediatric exam room interior. A friendly Korean male pediatrician in his late 30s with round glasses and white lab coat looks directly into the camera lens with a warm smile and waves hello at the camera. Camera settles to static shot as he gently points to a child's seat saying 'Come sit here!'. Dolly-in to static transition, eye contact with camera, photorealistic cinematic video, warm natural lighting, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 진료실 문이 열리면서 카메라가 천천히 앞으로 밀고 들어가(달리인) 따뜻하고 밝은 한국 소아과 진료실 내부가 드러나는 연출. 둥근 안경과 흰 가운의 친근한 한국인 남성 소아과 의사가 카메라 렌즈를 정면으로 바라보며 환하게 웃고 손을 흔들어 인사함. 카메라가 고정되며 의사가 아동 의자를 손으로 가리키며 "이 의자에 앉아볼까?"라고 안내. 달리인→고정 전환. 카메라와 눈맞춤. 실사 영화 화질, 따뜻한 조명, 5초`

---

### 챕터 5-A — 신뢰 루트 진료

---

#### 🎬 C5A_Stethoscope — 청진기 시연 & 검사 (6초)
* **카메라 워크:** 고정 + 오브젝트 접근 (Static + Object Approach) — 청진기가 화면 바깥에서 카메라 쪽으로 천천히 접근
* **[영문 입력용]:**
  > `First-person POV at child's eye level, static camera shot. A friendly Korean male pediatrician looks directly into the camera lens, places a colorful dinosaur-decorated stethoscope on his own wrist demonstrating 'See? Not cold!'. Then slowly and gently moves the stethoscope toward the camera (toward the viewer's chest). Eye contact with camera maintained throughout. Object approach to camera, gentle reassuring expression, photorealistic warm clinic lighting, 6 seconds`
* **[한글 해석]:**
  > `아이 눈높이 1인칭 시점. 고정 카메라. 친근한 한국인 남성 소아과 의사가 카메라 렌즈를 정면으로 바라보며 공룡 장식 청진기를 자신의 손목에 먼저 대보이며 "차갑지 않아~" 시연. 이어서 청진기를 카메라(아이 가슴) 쪽으로 천천히 부드럽게 접근시키는 오브젝트 어프로치 연출. 내내 카메라와 눈맞춤 유지. 실사 따뜻한 진료실 조명, 6초`

---

#### 🎬 C5A_Throat — 구강 검사 (5초)
* **카메라 워크:** 고정 샷 (Static Shot) — 손전등이 화면 중앙에서 카메라 쪽으로 천천히 접근
* **[영문 입력용]:**
  > `First-person POV, static camera shot. A friendly Korean male pediatrician looks directly into the camera with an encouraging smile, holds up a small medical penlight toward the camera saying 'Can you say Ahh?'. He slowly brings the penlight closer toward the camera (child's mouth). Eye contact with camera, object approach centered in frame, warm photorealistic clinic setting, soft gentle lighting, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 카메라 샷. 친근한 한국인 남성 소아과 의사가 카메라를 격려하는 미소로 정면 바라보며 작은 손전등을 카메라 쪽으로 들어 보이고 "아~ 해줄 수 있어?"라고 말함. 손전등을 카메라(아이 입) 쪽으로 천천히 가까이 접근시키는 연출. 카메라와 눈맞춤. 화면 중앙 오브젝트 어프로치. 따뜻한 실사 진료실, 부드러운 조명, 5초`

---

#### 🎬 C5A_Ear — 귀 검사 (4초)
* **카메라 워크:** 고정 후 측면 접근 (Static + Side Approach) — 이경이 화면 오른쪽 측면으로 천천히 이동
* **[영문 입력용]:**
  > `First-person POV, static camera shot. A friendly Korean male pediatrician holds an otoscope in center frame, shows it directly at the camera with gentle reassuring smile and eye contact saying 'I'll just shine a light in your ear, it won't tickle!'. Then slowly moves the otoscope to the right side of frame approaching the ear position. Camera stays completely static, side approach of object, photorealistic warm pediatric clinic, 4 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 완전 고정 카메라 샷. 친근한 한국인 남성 소아과 의사가 이경을 화면 중앙에 들고 카메라와 눈맞춤하며 다정한 미소로 "귀 안을 비춰볼게, 간지럽진 않아~"라고 말함. 이어서 이경을 화면 오른쪽 측면(아이 귀 위치)으로 천천히 이동시키는 사이드 어프로치 연출. 카메라는 완전 고정. 실사 따뜻한 소아과 진료실, 4초`

---

### 챕터 5-B — 달래기 루트 진료

---

#### 🎬 C5B_BearFirst — 곰돌이 먼저 진료받기 (6초)
* **카메라 워크:** 고정 미디엄 샷 (Static Medium Shot) — 화면 오른쪽에서 인형이 등장 후 카메라 쪽으로 내밀어지는 연출
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A kind Korean male pediatrician receives a soft teddy bear puppet from the right side of frame. He places the stethoscope on the bear's chest, looks at the bear with a playful smile saying 'I heard the bear's heartbeat!'. Then turns to look directly into the camera and slowly extends the teddy bear toward the camera lens saying 'Now it's your turn~'. Eye contact with camera at end, bear extends toward camera, warm photorealistic clinic, 6 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 친절한 한국인 남성 소아과 의사가 화면 오른쪽에서 곰돌이 손인형을 받음. 곰돌이 가슴에 청진기를 대고 장난스럽게 "곰돌이 심장 소리 들렸어!"라고 말함. 이어서 카메라 렌즈를 정면으로 바라보며 곰돌이를 카메라 쪽으로 천천히 내미는 연출. 마지막에 카메라와 눈맞춤. 인형이 카메라 방향으로 확장되는 연출. 따뜻한 실사 진료실, 6초`

---

#### 🎬 C5B_Breathing — 호흡 연습 게임 (5초)
* **카메라 워크:** 고정 미디엄 샷 (Static Medium Shot) — 의사가 카메라를 정면으로 바라보며 호흡 시연
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A friendly Korean male pediatrician looks directly and steadily into the camera lens throughout, cheerfully demonstrates deep breathing - slowly inhales through nose for 3 counts with visibly puffed cheeks, then slowly exhales through mouth with exaggerated 'whoosh' expression. Maintains warm encouraging eye contact with camera, inviting the viewer to breathe along. Photorealistic soft clinic lighting, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 친근한 한국인 남성 소아과 의사가 내내 카메라 렌즈를 정면으로 바라보며 심호흡을 쾌활하게 시연. 코로 천천히 3박자 들이마시며 볼이 선명하게 부풀어 오름, 이어서 입으로 과장된 "후~" 표정으로 천천히 내쉬기. 카메라와 따뜻하게 격려하는 눈맞춤 유지하며 같이 호흡하자고 유도. 실사 부드러운 진료실 조명, 5초`

---

### 챕터 5-C — 주사 맞기

---

#### 🎬 C5C_Notice — 주사 사전 예고 (5초)
* **카메라 워크:** 고정 미디엄 샷 (Static Medium Shot) — 의사가 카메라를 정면으로 바라보며 직접 대화
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A kind Korean male pediatrician looks directly and steadily into the camera lens with a gentle serious but warm expression. Speaks directly to the camera: 'Today you need a small shot to stay healthy. I'll tell you everything before we start, okay?'. Sustained direct eye contact with camera throughout, patient and trustworthy tone, photorealistic warm clinic, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 친절한 한국인 남성 소아과 의사가 카메라 렌즈를 내내 정면으로 바라보며 부드럽지만 진지하고 따뜻한 표정으로 카메라에 직접 말을 건넴. "오늘 건강해지는 데 도움이 되는 주사를 맞아야 해. 시작하기 전에 다 알려줄게, 괜찮아?" 지속적인 카메라 직시. 신뢰감 있는 차분한 톤. 실사 따뜻한 진료실, 5초`

---

#### 🎬 C5C_ShowTools — 주사 도구 탐색 (6초)
* **카메라 워크:** 고정 + 아이템 순차 제시 (Static + Sequential Object Reveal) — 도구들이 하나씩 카메라 쪽으로 올라와 제시됨
* **[영문 입력용]:**
  > `First-person POV, static camera shot. A friendly Korean female nurse in pink scrubs sequentially presents medical tray items one at a time toward the camera lens. First: alcohol swab pad rising into frame from below ('This cools and cleans your skin~'). Then: colorful bandage lifted toward camera ('Which design do you like?'). Finally: small syringe briefly shown ('This is quick and done right away~'). Each object revealed toward camera one at a time. Eye contact with camera between reveals. Warm reassuring smile, photorealistic clinic, 6 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 카메라 샷. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 의료 쟁반의 도구를 하나씩 순차적으로 카메라 렌즈 쪽으로 올려 제시. 첫째: 알코올 솜이 화면 아래에서 올라오며 등장("피부 닦아주는 거야, 차갑고 시원해~"). 둘째: 알록달록 반창고를 카메라 쪽으로 들어올림("어떤 그림 좋아?"). 셋째: 작은 주사기를 잠깐 보여줌("빠르게 들어갔다가 금방 끝나~"). 각 오브젝트가 순서대로 카메라를 향해 제시됨. 제시 사이에 카메라와 눈맞춤. 따뜻하고 안심시키는 미소. 실사 소아과 배경, 6초`

---

#### 🎬 C5C_BreathPre — 주사 전 호흡 준비 (6초)
* **카메라 워크:** 고정 미디엄 샷 (Static Medium Shot) — 간호사가 카메라를 직시하며 호흡 시연
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A kind Korean female nurse in pink scrubs looks directly into the camera lens and cheerfully demonstrates balloon breathing together with the viewer - slowly inhales through the nose with clearly puffed cheeks for 3 seconds, then slowly exhales through the mouth with a big 'whoosh'. Direct sustained eye contact with camera. Encouraging gesture saying 'When you breathe like this during the shot, it feels much better!'. Photorealistic warm clinic, 6 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 파스텔 핑크 스크럽의 친절한 한국인 여성 간호사가 카메라 렌즈를 직접 바라보며 시청자와 함께 풍선 호흡을 쾌활하게 시연. 코로 3초 동안 천천히 들이마시며 볼이 선명하게 부풀어 오름, 이어서 입으로 크게 "후~" 내쉬기. 카메라와 지속적인 직시 눈맞춤. "주사 맞을 때 이렇게 하면 훨씬 나아~"라고 격려. 실사 따뜻한 진료실, 6초`

---

#### 🎬 C5C_ArmChoice — 팔 선택 장면 (4초)
* **카메라 워크:** 고정 미디엄 샷 (Static Medium Shot) — 양손이 번갈아 화면 좌/우로 등장
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A friendly Korean female nurse in pink scrubs looks directly into the camera and alternately extends her left hand then right hand toward the camera from left and right sides of frame saying 'Which arm do you want? This arm? Or that arm?'. Hands alternate left-right in frame. Warm encouraging smile with direct eye contact at camera throughout. Photorealistic clinic lighting, 4 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 카메라를 직접 바라보며 왼손과 오른손을 화면 왼쪽과 오른쪽에서 번갈아 카메라 쪽으로 내밀며 "어떤 팔에 맞을래? 이쪽 팔? 저쪽 팔?"이라고 말함. 손이 화면 좌우로 번갈아 등장. 내내 카메라와 직시 눈맞춤. 따뜻한 격려 미소. 실사 진료실 조명, 4초`

---

#### 🎬 C5C_AlcWipe — 알코올 솜 닦기 (5초)
* **카메라 워크:** 고정 클로즈업 (Static Close-Up) — 아이 팔 시점, 솜이 화면 위에서 아래로 접근
* **[영문 입력용]:**
  > `First-person POV close-up of child's arm, static camera shot. A Korean female nurse in pink scrubs briefly shows an alcohol swab pad toward the camera from above saying 'I'll wipe your arm now, it'll feel cool and fresh!'. Then slowly lowers the swab down toward the camera (child's arm surface). Camera remains completely static close-up of arm. Object descending approach from top of frame, photorealistic warm clinic, 5 seconds`
* **[한글 해석]:**
  > `아이 팔 클로즈업 1인칭 시점. 완전 고정 카메라 샷. 파스텔 핑크 스크럽의 한국인 여성 간호사가 알코올 솜을 화면 위에서 잠깐 보여주며 "지금 솜으로 닦을게~ 차갑고 시원할 거야!"라고 말함. 이어서 솜을 카메라(아이 팔 표면) 쪽으로 위에서 아래로 천천히 내리는 하강 어프로치 연출. 카메라는 아이 팔 클로즈업 완전 고정. 실사 따뜻한 진료실, 5초`

---

#### 🎬 C5C_Injection — 주사 맞기 핵심 장면 (7초)
* **카메라 워크:** 고정 클로즈업 → 얼굴 클로즈업 컷 (Static Close-Up Arm → Face Fill-Frame Cut) — 팔 고정 후 간호사 얼굴로 화면 전환
* **[영문 입력용]:**
  > `First-person POV, static close-up of child's arm. A Korean female nurse in pink scrubs looks warmly at camera saying 'Take a big breath in... and breathe out~'. A very brief subtle motion at the far edge of frame (syringe kept peripheral and small, never center frame). Cut to: nurse's face filling the entire frame from close distance with a huge joyful smile saying 'All done!! You did amazing!!'. Two-shot sequence: arm close-up static then face fill-frame static, photorealistic, 7 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 아이 팔 고정 클로즈업. 파스텔 핑크 스크럽의 한국인 여성 간호사가 카메라를 따뜻하게 바라보며 "자~ 숨 한번 크게 들이마셔... 후~ 내쉬어~"라고 유도. 화면 가장 가장자리에 아주 잠깐 미묘한 동작(주사기는 항상 주변부에 작게, 절대 화면 중앙에 오지 않음). 이어서 컷: 간호사 얼굴이 가까이서 화면 전체를 채우며 "끝났어!! 정말 잘했어!!"라고 환하게 웃음. 2샷 시퀀스: 팔 클로즈업 고정 → 얼굴 필프레임 고정. 실사 화질, 7초`

> **⚠️ 연출 주의:** 주사기를 화면 중앙 크게 연출하지 않도록 Reference Image로 구도를 제어할 것. 공포 자극 최소화.

---

#### 🎬 C5C_Bandage — 반창고 선택 & 감정 체크 (5초)
* **카메라 워크:** 고정 미디엄 샷 (Static Medium Shot) — 반창고가 화면 중앙으로 제시됨
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A cheerful Korean female nurse in pink scrubs looks directly into the camera with a big celebratory smile, holds up 3 cute colorful bandage options toward the camera center frame (dinosaur, star, heart designs) asking 'Which one do you want?'. Then applies the chosen bandage with care while maintaining eye contact saying 'All done! You were so brave today!'. Direct eye contact with camera throughout, joyful warm celebration, photorealistic, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 쾌활한 파스텔 핑크 스크럽의 한국인 여성 간호사가 카메라를 직접 바라보며 큰 축하의 미소로 귀여운 반창고 3종(공룡, 별, 하트)을 화면 중앙으로 카메라 쪽에 들어 보이며 "어떤 거 붙여줄까?"라고 묻는 장면. 이어서 카메라와 눈맞춤을 유지하며 선택된 반창고를 정성껏 붙여주며 "다 끝났어! 오늘 정말 용감했어!"라고 칭찬. 내내 카메라와 직시 눈맞춤. 기쁜 축하 분위기. 실사 화질, 5초`

---

### 챕터 6 — 보상 & 귀가

---

#### 🎬 C6_Reward — 스티커 보상 선택 (5초)
* **카메라 워크:** 고정 미디엄 + 스티커 접근 (Static Medium + Object Offer) — 스티커 3종이 카메라 쪽으로 제시됨
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A joyful Korean male pediatrician looks directly into the camera lens with a huge warm smile and enthusiastic thumbs up saying 'You were incredible today!'. Then holds out 3 shiny reward stickers simultaneously toward the camera center frame (star, dinosaur, heart shapes) asking 'Which one do you want?'. Direct eye contact with camera, stickers extended toward camera, celebration atmosphere, warm bright lighting, photorealistic, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 기쁜 표정의 한국인 남성 소아과 의사가 카메라 렌즈를 직접 바라보며 환한 큰 미소와 열정적인 엄지척으로 "오늘 정말 대단했어!"라고 말함. 이어서 빛나는 보상 스티커 3종(별, 공룡, 하트 모양)을 화면 중앙 카메라 쪽으로 동시에 내밀며 "어떤 거 갖고 싶어?"라고 묻는 장면. 카메라와 직시 눈맞춤. 스티커가 카메라 방향으로 제시됨. 축하 분위기, 따뜻하고 밝은 조명. 실사 화질, 5초`

---

#### 🎬 C6_Farewell — 의사 작별 인사 (4초)
* **카메라 워크:** 고정 미디엄 샷 (Static Medium Shot) — 카메라 정면 직시하며 손 흔들기
* **[영문 입력용]:**
  > `First-person POV, static medium shot. A warm friendly Korean male pediatrician looks directly and steadily into the camera lens with a big genuine warm smile, waves goodbye enthusiastically directly at the camera saying 'Come back again! The doctor will be waiting for you~'. Direct sustained eye contact with camera, warm cozy clinic background, soft natural lighting, photorealistic, 4 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 고정 미디엄 샷. 따뜻하고 친근한 한국인 남성 소아과 의사가 카메라 렌즈를 내내 정면으로 바라보며 진심 어린 큰 따뜻한 미소로 카메라를 향해 활발하게 손을 흔들며 "다음에 또 와! 선생님이 기다릴게~"라고 작별 인사. 카메라와 지속적인 직시 눈맞춤. 따뜻하고 아늑한 진료실 배경, 부드러운 자연 채광. 실사 화질, 4초`

---

### 공용 대기 루프 클립

---

#### 🎬 Idle_Doctor — 의사 선생님 대기 루프 (4초 loop)
* **카메라 워크:** 삼각대 완전 고정 (Tripod Static Lock) — 절대 흔들림 없이 완전 고정, 루프 이음새 없음
* **[영문 입력용]:**
  > `First-person POV, locked-off tripod static shot with absolutely zero camera movement. A friendly Korean male pediatrician with round glasses and white lab coat waits with a gentle warm patient smile looking directly at the camera lens, subtle natural eye blinking every 2-3 seconds and barely perceptible slow chest breathing. Completely static camera, no movement whatsoever, realistic warm pediatric clinic background, photorealistic cinema quality, seamless 4-second looping video`
* **[한글 해석]:**
  > `1인칭 시점. 삼각대 완전 잠금 고정 샷 — 카메라 움직임 절대 없음. 둥근 안경과 흰 가운의 친근한 한국인 남성 소아과 의사가 카메라 렌즈를 직접 바라보며 다정하고 따뜻한 미소를 유지. 2~3초마다 자연스러운 눈 껌뻑임과 거의 느껴지지 않는 천천히 숨쉬는 가슴 움직임. 카메라 완전 고정, 어떤 움직임도 없음. 실사 따뜻한 소아과 진료실 배경. 실사 영화 화질. 자연스럽게 이어지는 4초 루프`

---

#### 🎬 Idle_Nurse — 간호사 선생님 대기 루프 (4초 loop)
* **카메라 워크:** 삼각대 완전 고정 (Tripod Static Lock) — 절대 흔들림 없이 완전 고정, 루프 이음새 없음
* **[영문 입력용]:**
  > `First-person POV, locked-off tripod static shot with absolutely zero camera movement. A friendly Korean female pediatric nurse in pastel pink scrubs waits with a gentle warm patient smile looking directly at the camera lens, subtle natural eye blinking every 2-3 seconds and barely perceptible slow breathing. Completely static camera, no movement whatsoever, bright warm pediatric clinic background, photorealistic cinema quality, seamless 4-second looping video`
* **[한글 해석]:**
  > `1인칭 시점. 삼각대 완전 잠금 고정 샷 — 카메라 움직임 절대 없음. 파스텔 핑크 스크럽의 친근한 한국인 여성 소아과 간호사가 카메라 렌즈를 직접 바라보며 다정하고 따뜻한 미소를 유지. 2~3초마다 자연스러운 눈 껌뻑임과 거의 느껴지지 않는 천천히 숨쉬는 움직임. 카메라 완전 고정, 어떤 움직임도 없음. 밝고 따뜻한 소아과 진료실 배경. 실사 영화 화질. 자연스럽게 이어지는 4초 루프`



---

#### 🎬 C5A_Throat — 구강 검사 (5초)
* **[영문 입력용]:**
  > `First-person POV. A friendly Korean male pediatrician holds a small medical penlight and says 'Can you say Ahh?' with an encouraging smile. He slowly brings the light toward the camera (child's mouth perspective). Warm photorealistic clinic setting, soft gentle lighting, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 친근한 한국인 남성 소아과 의사가 작은 손전등을 들고 격려하는 미소로 "아~ 해줄 수 있어?"라고 말하며 카메라(아이 입) 쪽으로 천천히 다가오는 장면. 따뜻한 실사 진료실 배경, 부드러운 조명, 5초`

---

#### 🎬 C5A_Ear — 귀 검사 (4초)
* **[영문 입력용]:**
  > `First-person POV. A friendly Korean male pediatrician holds an otoscope (ear examination device), shows it to the camera saying 'I'll just shine a light in your ear, it won't tickle!', then slowly brings it closer toward the side of the camera frame. Gentle reassuring smile, photorealistic warm pediatric clinic, 4 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 친근한 한국인 남성 소아과 의사가 이경(귀 검사 기구)을 카메라에 보여주며 "귀 안을 비춰볼게, 간지럽진 않아~"라고 말한 후 카메라 측면 쪽으로 천천히 가져오는 장면. 다정하고 안심시키는 미소. 실사 따뜻한 소아과 진료실, 4초`

---

### 챕터 5-B — 달래기 루트 진료

---

#### 🎬 C5B_BearFirst — 곰돌이 먼저 진료받기 (6초)
* **[영문 입력용]:**
  > `First-person POV. A kind Korean male pediatrician receives a soft teddy bear puppet from a nurse, places the stethoscope on the bear's chest and pretends to listen with a playful smile saying 'I heard the bear's heartbeat!'. Then holds the bear out toward the camera saying 'Now it's your turn~'. Warm photorealistic clinic, 6 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 친절한 한국인 남성 소아과 의사가 간호사에게서 곰돌이 손인형을 받아 곰돌이 가슴에 청진기를 대고 장난스럽게 "곰돌이 심장 소리 들렸어!"라고 말함. 이어서 곰돌이를 카메라 방향으로 내밀며 "이번엔 네 차례야~"라고 유도. 따뜻한 실사 진료실, 6초`

---

#### 🎬 C5B_Breathing — 호흡 연습 게임 (5초)
* **[영문 입력용]:**
  > `First-person POV. A friendly Korean male pediatrician demonstrates deep breathing with an exaggerated friendly gesture - slowly inhaling through the nose with puffed cheeks, then slowly exhaling through the mouth with a 'whoosh' expression. Encouraging warm smile, inviting the camera (child) to follow along. Photorealistic soft clinic lighting, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 친근한 한국인 남성 소아과 의사가 과장되게 친근한 제스처로 심호흡을 시연. 코로 천천히 들이마시며 볼을 부풀리다가 입으로 "후~" 천천히 내쉬는 표정. 격려하는 따뜻한 미소로 카메라(아이)에게 같이 해보자고 유도. 실사 부드러운 진료실 조명, 5초`

---

### 챕터 5-C — 주사 맞기

---

#### 🎬 C5C_Notice — 주사 사전 예고 (5초)
* **[영문 입력용]:**
  > `First-person POV. A kind Korean male pediatrician speaks directly to the camera with a gentle serious but warm expression, saying 'Today you need a small shot to stay healthy. I'll tell you everything before we start, okay?'. Patient and trustworthy tone, photorealistic warm clinic, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 친절한 한국인 남성 소아과 의사가 카메라를 향해 부드럽지만 진지하고 따뜻한 표정으로 "오늘 건강해지는 데 도움이 되는 주사를 맞아야 해. 시작하기 전에 다 알려줄게, 괜찮아?"라고 말하는 장면. 신뢰감 있는 차분한 톤. 실사 따뜻한 진료실, 5초`

---

#### 🎬 C5C_ShowTools — 주사 도구 탐색 (6초)
* **[영문 입력용]:**
  > `First-person POV. A friendly Korean female nurse in pink scrubs shows a small medical tray with tools one by one to the camera: first an alcohol swab pad ('This cools and cleans your skin~'), then a colorful bandage ('This goes on after, which design do you like?'), then a small syringe ('This is quick and done right away~'). Warm reassuring smile, photorealistic clinic setting, 6 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 작은 의료 쟁반을 카메라 앞에 보여주며 도구를 하나씩 소개. 알코올 솜("피부 닦아주는 거야, 차갑고 시원해~"), 알록달록 반창고("다 끝나면 붙여주는 거야, 어떤 그림 좋아?"), 작은 주사기("빠르게 들어갔다가 금방 끝나~") 순서. 따뜻하고 안심시키는 미소. 실사 소아과 배경, 6초`

---

#### 🎬 C5C_BreathPre — 주사 전 호흡 준비 (6초)
* **[영문 입력용]:**
  > `First-person POV. A kind Korean female nurse in pink scrubs cheerfully demonstrates balloon breathing with the camera - slowly inhales through the nose with puffed cheeks (3 seconds), then slowly exhales through the mouth with a 'whoosh'. Encouraging gesture saying 'When you breathe like this during the shot, it feels much better!'. Photorealistic warm clinic, 6 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 파스텔 핑크 스크럽의 친절한 한국인 여성 간호사가 카메라와 함께 풍선 호흡을 쾌활하게 시연. 코로 천천히 들이마시며 볼을 부풀리는 동작(3초) 후 입으로 "후~" 천천히 내쉬기. "주사 맞을 때 이렇게 하면 훨씬 나아~"라고 격려하는 제스처. 실사 따뜻한 진료실, 6초`

---

#### 🎬 C5C_ArmChoice — 팔 선택 장면 (4초)
* **[영문 입력용]:**
  > `First-person POV. A friendly Korean female nurse in pink scrubs holds out both hands alternately toward the camera saying 'Which arm do you want? This arm or that arm?', with a warm encouraging smile giving the child the choice. Photorealistic clinic lighting, 4 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 파스텔 핑크 스크럽의 친근한 한국인 여성 간호사가 양손을 번갈아 카메라 쪽으로 내밀며 "어떤 팔에 맞을래? 이쪽 팔? 저쪽 팔?"이라고 따뜻한 미소로 선택권을 줌. 실사 진료실 조명, 4초`

---

#### 🎬 C5C_AlcWipe — 알코올 솜 닦기 (5초)
* **[영문 입력용]:**
  > `First-person POV at child's arm perspective. A Korean female nurse in pink scrubs holds up an alcohol swab pad and says 'I'll wipe your arm now, it'll feel cool and fresh!', then slowly brings the swab toward the camera (child's arm). The camera stays steady as the swab approaches. Photorealistic warm clinic, 5 seconds`
* **[한글 해석]:**
  > `아이 팔 시점 1인칭 POV. 파스텔 핑크 스크럽의 한국인 여성 간호사가 알코올 솜을 들어 보이며 "지금 솜으로 닦을게~ 차갑고 시원할 거야!"라고 말한 후 카메라(아이 팔) 쪽으로 솜을 천천히 가져오는 장면. 카메라는 고정 유지. 실사 따뜻한 진료실, 5초`

---

#### 🎬 C5C_Injection — 주사 맞기 핵심 장면 (7초)
* **[영문 입력용]:**
  > `First-person POV, child's arm close-up perspective. A Korean female nurse in pink scrubs gives a warm encouraging look saying 'Take a big breath in...and breathe out~'. A quick subtle motion near the edge of frame (syringe minimized, not close-up). Then the nurse's face fills the frame with a huge joyful smile saying 'All done!! You did amazing!!'. Quick completion, warm celebration, photorealistic, 7 seconds`
* **[한글 해석]:**
  > `아이 팔 클로즈업 1인칭 시점. 파스텔 핑크 스크럽의 한국인 여성 간호사가 따뜻하게 격려하며 "자~ 숨 한번 크게 들이마셔... 후~ 내쉬어~"라고 유도. 화면 가장자리에 아주 작게 잠깐 스쳐가는 동작(주사기 클로즈업 최소화). 이어서 간호사 얼굴이 화면을 가득 채우며 "끝났어!! 정말 잘했어!!"라고 환하게 웃는 장면. 실사 화질, 7초`

> **⚠️ 연출 주의:** 주사기를 화면 중앙 크게 연출하지 않도록 Reference Image로 구도를 제어할 것. 공포 자극 최소화.

---

#### 🎬 C5C_Bandage — 반창고 선택 & 감정 체크 (5초)
* **[영문 입력용]:**
  > `First-person POV. A cheerful Korean female nurse in pink scrubs holds up 3 cute colorful bandage options toward the camera (dinosaur, star, heart designs) asking 'Which one do you want?'. Then applies the chosen bandage while saying 'All done! You were so brave today!'. Joyful warm celebration atmosphere, photorealistic, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 쾌활한 파스텔 핑크 스크럽의 한국인 여성 간호사가 귀여운 반창고 3종(공룡, 별, 하트 디자인)을 카메라 쪽으로 들어 보이며 "어떤 거 붙여줄까?"라고 묻는 장면. 이어서 선택된 반창고를 붙여주며 "다 끝났어! 오늘 정말 용감했어!"라고 칭찬. 기쁜 축하 분위기. 실사 화질, 5초`

---

### 챕터 6 — 보상 & 귀가

---

#### 🎬 C6_Reward — 스티커 보상 선택 (5초)
* **[영문 입력용]:**
  > `First-person POV. A joyful Korean male pediatrician gives a big warm smile and clear thumbs up saying 'You were incredible today!', then holds out 3 shiny reward stickers toward the camera (star shape, dinosaur shape, heart shape) asking 'Which one do you want?'. Celebration atmosphere, warm bright lighting, photorealistic, 5 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 기쁜 표정의 한국인 남성 소아과 의사가 환한 미소와 함께 엄지척을 선명하게 보여주며 "오늘 정말 대단했어!"라고 말함. 이어서 빛나는 보상 스티커 3종(별, 공룡, 하트 모양)을 카메라 쪽으로 내밀며 "어떤 거 갖고 싶어?"라고 묻는 장면. 축하 분위기, 따뜻하고 밝은 조명. 실사 화질, 5초`

---

#### 🎬 C6_Farewell — 의사 작별 인사 (4초)
* **[영문 입력용]:**
  > `First-person POV. A warm friendly Korean male pediatrician waves goodbye enthusiastically at the camera with a big genuine smile, saying 'Come back again! The doctor will be waiting for you~'. Warm cozy clinic background, soft natural lighting, photorealistic, 4 seconds`
* **[한글 해석]:**
  > `1인칭 시점. 따뜻하고 친근한 한국인 남성 소아과 의사가 환한 진심 어린 미소로 카메라를 향해 활발하게 손을 흔들며 "다음에 또 와! 선생님이 기다릴게~"라고 작별 인사를 하는 장면. 따뜻하고 아늑한 진료실 배경, 부드러운 자연 채광. 실사 화질, 4초`

---

### 공용 대기 루프 클립

---

#### 🎬 Idle_Doctor — 의사 선생님 대기 루프 (4초 loop)
* **[영문 입력용]:**
  > `First-person POV, a friendly Korean male pediatrician with round glasses and white lab coat waiting with a gentle warm patient smile, subtle natural eye blinking and slow breathing motion, static tripod shot, realistic warm pediatric clinic background, photorealistic cinema quality, seamless 4-second looping video`
* **[한글 해석]:**
  > `1인칭 시점. 둥근 안경과 흰 가운의 친근한 한국인 남성 소아과 의사가 다정하고 따뜻한 미소를 유지한 채 기다리는 장면. 자연스러운 눈 껌뻑임과 천천히 숨쉬는 움직임. 삼각대 고정 샷. 실사 따뜻한 소아과 진료실 배경. 실사 영화 화질. 자연스럽게 이어지는 4초 루프`

---

#### 🎬 Idle_Nurse — 간호사 선생님 대기 루프 (4초 loop)
* **[영문 입력용]:**
  > `First-person POV, a friendly Korean female pediatric nurse in pastel pink scrubs waiting with a gentle warm patient smile, subtle natural eye blinking and slow breathing, static tripod shot, bright warm pediatric clinic background, photorealistic cinema quality, seamless 4-second looping video`
* **[한글 해석]:**
  > `1인칭 시점. 파스텔 핑크 스크럽의 친근한 한국인 여성 소아과 간호사가 다정하고 따뜻한 미소를 유지한 채 기다리는 장면. 자연스러운 눈 껌뻑임과 천천히 숨쉬는 움직임. 삼각대 고정 샷. 밝고 따뜻한 소아과 진료실 배경. 실사 영화 화질. 자연스럽게 이어지는 4초 루프`

---

### 📋 전체 프롬프트 요약표

| 클립 ID | 등장인물 | 길이 | 참조 이미지 |
| :--- | :--- | :--- | :--- |
| C1_Arrive | 간호사 | 5s | nurse_turnaround.png + clinic_background.png |
| C1_HiPath | 간호사 | 3s | nurse_turnaround.png |
| C1_HidePath | 간호사 | 3s | nurse_turnaround.png |
| C2_Reception | 간호사 | 5s | nurse_turnaround.png + clinic_background.png |
| C2_WaitingRoom | (배경만) | 6s | clinic_background.png (대기실 버전) |
| C3_NameCall | 간호사 + 복도 | 5s | nurse_turnaround.png |
| C4_DoctorGreet | 의사 | 5s | pediatrician_turnaround.png + clinic_background.png |
| C5A_Stethoscope | 의사 | 6s | pediatrician_turnaround.png |
| C5A_Throat | 의사 | 5s | pediatrician_turnaround.png |
| C5A_Ear | 의사 | 4s | pediatrician_turnaround.png |
| C5B_BearFirst | 의사 + 간호사 | 6s | 두 캐릭터 합성 First Frame |
| C5B_Breathing | 의사 | 5s | pediatrician_turnaround.png |
| C5C_Notice | 의사 | 5s | pediatrician_turnaround.png |
| C5C_ShowTools | 간호사 | 6s | nurse_turnaround.png |
| C5C_BreathPre | 간호사 | 6s | nurse_turnaround.png |
| C5C_ArmChoice | 간호사 | 4s | nurse_turnaround.png |
| C5C_AlcWipe | 간호사 | 5s | nurse_turnaround.png |
| C5C_Injection | 간호사 | 7s | nurse_turnaround.png (얼굴 클로즈업) |
| C5C_Bandage | 간호사 | 5s | nurse_turnaround.png |
| C6_Reward | 의사 | 5s | pediatrician_turnaround.png |
| C6_Farewell | 의사 | 4s | pediatrician_turnaround.png |
| Idle_Doctor | 의사 | 4s loop | pediatrician_turnaround.png |
| Idle_Nurse | 간호사 | 4s loop | nurse_turnaround.png |

**총 클립 수: 23개 / 총 영상 시간(루프 제외): 약 120초 (2분)**

