export const MOVIE_BASE = `${import.meta.env.BASE_URL}Movie/Hospital/`;

export const EPISODE = [
  { type: 'stepLabel', icon: '🐻', num: 'STEP 1', title: '동화 미리보기', desc: '병원이 어떤 곳인지 동화로 먼저 만나봐요!' },
  { type: 'video', id: '1-1', file: '1-1.mp4', label: '📖 1-1. 기침과 열이 나요', skip: true },
  { type: 'video', id: '1-2', file: '1-2.mp4', label: '📖 1-2. 병원 건물 구경하기', skip: true },
  { type: 'video', id: '1-3', file: '1-3.mp4', label: '📖 1-3. 친절한 의사 선생님', skip: true },
  { type: 'schedule' },
  { type: 'stepLabel', icon: '🎠', num: 'STEP 3', title: '코코 체험 보기', desc: '곰돌이가 먼저 병원을 경험해요! 같이 구경해요 😊' },
  { type: 'video', id: '3-1', file: '3-1.mp4', label: '🐻 3-1. 곰돌이 코코 병원 도착', skip: true },
  { type: 'video', id: '3-2', file: '3-2.mp4', label: '🐻 3-2. 곰돌이 진료 및 검사', skip: true },
  { type: 'video', id: '3-3', file: '3-3.mp4', label: '🐻 3-3. 곰돌이 칭찬 스티커', skip: true },
  { type: 'stepLabel', icon: '🏥', num: 'STEP 4', title: '내가 직접 체험하기', desc: '이제 직접 경험해봐요! 선택하면서 함께해요 🌟' },
  { type: 'video', id: 'C1_Arrive', file: 'C1_Arrive.mp4', label: '🌟 4-1. 병원 도착 및 입구', hudActive: 1, skip: false, afterEnd: 'choice-c1', action: { at: 3, icon: '🚪', label: '병원 들어가기' } },
  { type: 'choice', id: 'choice-c1', question: '간호사 선생님이 손을 흔들어요!\n어떻게 할까요? 👋', options: [ { icon: '👋', label: '인사하기', next: 'C1_HiPath' }, { icon: '🙈', label: '숨기', next: 'C1_HidePath' } ] },
  { type: 'video', id: 'C1_HiPath', file: 'C1_HiPath.mp4', label: '🌟 4-1. 반갑게 인사해요', skip: false },
  { type: 'video', id: 'C1_HidePath', file: 'C1_HidePath.mp4', label: '🌟 4-1. 수줍어서 살짝 숨어요', skip: false },
  { type: 'video', id: 'C2_Reception', file: 'C2_Reception.mp4', label: '📋 4-2. 차분하게 접수하기', hudActive: 2, skip: false },
  { type: 'video', id: 'C2_WaitingRoom', file: 'C2_WaitingRoom.mp4', label: '📋 4-2. 장난감 대기실 탐색', hudActive: 2, skip: false },
  { type: 'video', id: 'C3_NameCall', file: 'C3_NameCall.mp4', label: '📋 4-3. 내 이름 호명 듣기', skip: false },
  { type: 'video', id: 'C4_DoctorGreet', file: 'C4_DoctorGreet.mp4', label: '🩺 4-4. 의사 선생님과 반갑게 인사', hudActive: 3, skip: false, afterEnd: 'choice-c5-route' },
  { type: 'choice', id: 'choice-c5-route', question: '의사 선생님이 진료를 시작해요!\n어떤 방법으로 해볼까요?', options: [ { icon: '🩺', label: '검사해봐요\n(5-A 신뢰 루트)', next: 'C5A_Stethoscope' }, { icon: '🐻', label: '곰돌이 먼저요!\n(5-B 달래기 루트)', next: 'C5B_Stethoscope' } ] },
  { type: 'video', id: 'C5A_Stethoscope', file: 'C5A_Stethoscope.mp4', label: '🩺 4-5. 청진기 가슴 검사', hudActive: 3, skip: false, sensory: { icon: '❄️', text: '조금 차가울 수 있어요!' }, at: 1 },
  { type: 'video', id: 'C5A_Throat', file: 'C5A_Throat.mp4', label: '🩺 4-5. 아~ 목 안 손전등 검사', hudActive: 3, skip: false, sensory: { icon: '💡', text: '반짝! 빛이 비춰요!' }, at: 1 },
  { type: 'video', id: 'C5A_Ear', file: 'C5A_Ear.mp4', label: '🩺 4-5. 귓속 체온 및 이경 검사', hudActive: 3, skip: false },
  { type: 'video', id: 'C5B_Stethoscope', file: 'C5A_Stethoscope.mp4', label: '🐻 4-5. 곰돌이 먼저 청진기 검사', hudActive: 3, skip: false, sensory: { icon: '🐻', text: '곰돌이도 안 아파해요!' }, at: 1 },
  { type: 'video', id: 'C5B_Throat', file: 'C5A_Throat.mp4', label: '🐻 4-5. 곰돌이 목 검사', hudActive: 3, skip: false, sensory: { icon: '💡', text: '반짝! 빛이 비춰요!' }, at: 1 },
  { type: 'video', id: 'C5B_Ear', file: 'C5A_Ear.mp4', label: '🐻 4-5. 곰돌이 귀 검사', hudActive: 3, skip: false },
  { type: 'video', id: 'C5C_Notice', file: 'C5C_Notice.mp4', label: '💉 4-6. 주사 맞을 준비', hudActive: 4, skip: false, sensory: { icon: '🌵', text: '따끔! (3초면 끝나요)' }, at: 2 },
  { type: 'video', id: 'C5C_AlcWipe', file: 'C5C_AlcWipe.mp4', label: '💉 4-6. 알코올 솜 쓱쓱', hudActive: 4, skip: false, sensory: { icon: '❄️', text: '차가울 거예요~' }, at: 0.5 },
  { type: 'video', id: 'C5C_Injection', file: 'C5C_Injection.mp4', label: '💉 4-6. 용감하게 예방 주사', hudActive: 4, skip: false },
  { type: 'video', id: 'C5C_Bandage', file: 'C5C_Bandage.mp4', label: '💉 4-6. 귀여운 뽀로로 반창고', hudActive: 4, skip: false },
  { type: 'video', id: 'C6_Farewell', file: 'C6_Farewell.mp4', label: '🎁 4-7. 칭찬 보상 및 작별 인사', hudActive: 5, skip: false },
  { type: 'ending' }
];

export const RESUME_AFTER_BRANCH = {
  'C1_HiPath': 'C2_Reception',
  'C1_HidePath': 'C2_Reception',
  'C5B_Stethoscope': 'C5B_Throat',
  'C5B_Throat': 'C5B_Ear',
  'C5B_Ear': 'C5C_Notice',
  'C5A_Ear': 'C5C_Notice'
};

export const episodeById = {};
EPISODE.forEach((node, i) => { if (node.id) episodeById[node.id] = i; });
