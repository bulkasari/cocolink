# [콘텐츠 라이브러리 총괄] CocoLink Social 풀 에피소드 시나리오 팩
## : `Docs/Hospital/full_episode_scenario.md` 규격 기반 9대 실전 상황별 풀 프로덕션 명세

> **문서 목적:** 실제 앱에서 지속적으로 아동을 교육하고 AI 비디오/애니메이션 클립을 즉시 생성할 수 있도록, 9대 핵심 상황별 폴더 및 4-Step 풀 시나리오(AI 프롬프트, 1인칭 POV 분기, QTE, 속마음 오버레이, 큐카드) 완비.

---

## 1. `Docs/Social/scenario` ➔ `content/` 폴더 1:1 매핑 내역

| 기존 scenario 파일 | 생성된 content 폴더 및 풀 시나리오 링크 | 원전 서적 및 세션 |
| :--- | :--- | :--- |
| **01_딜_만들기와_협상하기.md** | [01_놀이_갈등_딜_만들기와_협상하기/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/01_놀이_갈등_딜_만들기와_협상하기/full_episode_scenario.md) | Fast Track Unit III (Session 11&12) |
| **02_누가_먼저할지_공정하게_순서정하기.md** | [02_장난감_순서_정하기와_차례_지키기/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/02_장난감_순서_정하기와_차례_지키기/full_episode_scenario.md) | Fast Track Unit III (Session 14&15) |
| **03_이겼을때_졌을때_스포츠맨십.md** | [03_게임_승패와_스포츠맨십_대화/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/03_게임_승패와_스포츠맨십_대화/full_episode_scenario.md) | Fast Track Unit IV (Session 16) |
| **04_속임수_치팅_충동_참기.md** | [04_보드게임_속임수_치팅_충동_참기/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/04_보드게임_속임수_치팅_충동_참기/full_episode_scenario.md) | Fast Track Unit IV (Session 17&18) |
| **05_바디랭귀지와_불편한_신호_알아차리기.md** | [05_친구의_불편한_바디랭귀지_신호_알아차리기/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/05_친구의_불편한_바디랭귀지_신호_알아차리기/full_episode_scenario.md) | Fast Track Unit V (Session 19&20) |
| **06_비꼬기와_진짜칭찬_구별하기.md** | [06_친구의_반어법_비꼬기와_진짜칭찬_구별하기/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/06_친구의_반어법_비꼬기와_진짜칭찬_구별하기/full_episode_scenario.md) | UCLA PEERS (Chapter 5) |
| **07_대화가_어색해졌을때_살려내기.md** | [07_대화가_어색해졌을때_살려내기_대화복구/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/07_대화가_어색해졌을때_살려내기_대화복구/full_episode_scenario.md) | UCLA PEERS (Chapter 6) |
| **08_관심사_일방통행_방지_핑퐁토크.md** | [08_관심사_독점_방지와_주고받는_핑퐁토크/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/08_관심사_독점_방지와_주고받는_핑퐁토크/full_episode_scenario.md) | UCLA PEERS (Chapter 4&7) |
| **09_놀림과_장난에_쿨하게_대처하기.md** | [09_친구의_짓궂은_놀림에_쿨하게_대처하기/full_episode_scenario.md](file:///C:/Users/bulka/orca/workspaces/cocolink/cocolink/Docs/Social/scenario/content/09_친구의_짓궂은_놀림에_쿨하게_대처하기/full_episode_scenario.md) | UCLA PEERS (Chapter 11) |

---

## 2. 공통 에피소드 아키텍처 규격 (Standard 5-Step Structure)

모든 풀 에피소드는 `Docs/Hospital/full_episode_scenario.md`와 100% 동일한 프로덕션 체계를 따릅니다:

1. **🎨 참조 그래픽 에셋 라이브러리:** 3D 애니메이션 스타일(`Graphic/social/animation/`)과 1인칭 실사 스타일(`Graphic/social/real/`) 분리
2. **🎬 STEP 1 (Pre-Story):** 30초 3D 숏폼 동화 (AI 프롬프트 영문/한글 완비)
3. **🧭 STEP 2 (Visual Schedule):** 상시 5단계 아이콘 네비게이션 HUD
4. **🎬 STEP 3 (Model-First):** 코코 곰돌이의 대비 모델링 (서툰 행동 ➔ 생각 말풍선 ➔ 올바른 행동)
5. **🎬 STEP 4 (Interactive POV Simulation):** 6개 챕터 풀 인터랙션 (실사 POV 프롬프트, QTE, PECS 2지선다, 상태 머신)
6. **📱 STEP 5 (Home Bridge Card):** 보호자 10초 실전 팁 및 잠금화면 큐카드
