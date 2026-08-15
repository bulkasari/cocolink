import hospitalEvents from './hospital_events.json';

const R2_BASE = 'https://pub-3a895f08e79b4437bb379c105f960f7d.r2.dev/Movie/';

export const EPISODE_TYPES = {
  HOSPITAL: 'hospital',
  EYECLINIC: 'eyeclinic'
};

export const EPISODE_META = {
  hospital: {
    id: 'hospital',
    title: '소아과 병원',
    sub: '소아과 병원 적응 인터랙티브 에피소드',
    desc: '발달지연·자폐스펙트럼 아동을 위한 4단계 체험',
    badge: '🐻',
    tag: 'Hospital Episode (1~4단계)',
    movieBase: import.meta.env.VITE_MOVIE_BASE_URL || `${R2_BASE}Hospital/`,
    hudSteps: [
      { id: 1, icon: '🏥', label: '입구' },
      { id: 2, icon: '📋', label: '접수' },
      { id: 3, icon: '🩺', label: '진료' },
      { id: 4, icon: '💉', label: '주사' },
      { id: 5, icon: '🎁', label: '보상' },
    ],
    scheduleCards: [
      ['🏥', '1단계', '병원 입구'],
      ['📋', '2단계', '접수 대기'],
      ['🩺', '3단계', '의사 진료'],
      ['💉', '4단계', '건강 주사'],
      ['🎁', '5단계', '칭찬 보상']
    ]
  },
  eyeclinic: {
    id: 'eyeclinic',
    title: '소아 안과',
    sub: '소아 안과 적응 인터랙티브 에피소드',
    desc: '시각 감각 완충 & 입체 기계 체험 (1~3단계)',
    badge: '🦉',
    tag: 'Eye Clinic Episode (1~3단계)',
    movieBase: `${R2_BASE}EyeClinic/`,
    hudSteps: [
      { id: 1, icon: '🏥', label: '안과 입구' },
      { id: 2, icon: '📋', label: '접수' },
      { id: 3, icon: '🎈', label: '눈 검사' },
      { id: 4, icon: '👁️', label: '진료실' },
      { id: 5, icon: '🕶️', label: '보상' },
    ],
    scheduleCards: [
      ['🏥', '1단계', '안과 입구'],
      ['📋', '2단계', '접수 대기'],
      ['🎈', '3단계', '눈 검사기'],
      ['👁️', '4단계', '선생님 진료'],
      ['🕶️', '5단계', '별 선글라스']
    ]
  }
};

// Quick map for JSON events
export const eventMap = {};
hospitalEvents.hospital_events.forEach(ev => {
  eventMap[ev.id] = ev;
});

// Hospital Episode Nodes (Step 1~4)
export const HOSPITAL_EPISODE = [
  { type: 'stepLabel', icon: '🐻', num: '1단계', title: '병원 동화 미리보기', desc: '병원이 어떤 곳인지 따뜻한 동화로 먼저 만나요!' },
  { type: 'video', id: '1-1', file: '1-1.mp4', section: '📖 1단계 · 병원 동화 미리보기', subLabel: '기침과 열이 나요', skip: true },
  { type: 'video', id: '1-2', file: '1-2.mp4', section: '📖 1단계 · 병원 동화 미리보기', subLabel: '병원 건물 구경하기', skip: true },
  { type: 'video', id: '1-3', file: '1-3.mp4', section: '📖 1단계 · 병원 동화 미리보기', subLabel: '친절한 의사 선생님', skip: true },
  { type: 'schedule' },
  { type: 'stepLabel', icon: '🎠', num: '2단계', title: '곰돌이의 병원 체험 관찰', desc: '곰돌이 코코가 먼저 병원을 경험해요! 같이 구경해요 😊' },
  { type: 'video', id: '3-1', file: '3-1.mp4', section: '🐻 2단계 · 곰돌이의 병원 체험 관찰', subLabel: '코코 병원 도착', skip: true },
  { type: 'video', id: '3-2', file: '3-2.mp4', section: '🐻 2단계 · 곰돌이의 병원 체험 관찰', subLabel: '진료 및 검사', skip: true },
  { type: 'video', id: '3-3', file: '3-3.mp4', section: '🐻 2단계 · 곰돌이의 병원 체험 관찰', subLabel: '칭찬 스티커 받기', skip: true },
  { type: 'stepLabel', icon: '🏥', num: '3단계', title: '내가 직접 체험하기', desc: '이제 내가 주인공! 선택하면서 함께 병원을 경험해요 🌟' },
  { type: 'video', id: 'C1_Arrive', file: 'C1_Arrive.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '병원 도착 및 입구', hudActive: 1, skip: false, afterEnd: 'choice-c1', action: eventMap['C1_Arrive']?.action },
  { type: 'choice', id: 'choice-c1', question: '간호사 선생님이 손을 흔들어요!\n어떻게 할까요? 👋', options: [ { icon: '👋', label: '인사하기', next: 'C1_HiPath' }, { icon: '🙈', label: '숨기', next: 'C1_HidePath' } ] },
  { type: 'video', id: 'C1_HiPath', file: 'C1_HiPath.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '반갑게 인사해요', skip: false, action: eventMap['C1_HiPath']?.action },
  { type: 'video', id: 'C1_HidePath', file: 'C1_HidePath.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '수줍어서 살짝 숨어요', skip: false, action: eventMap['C1_HidePath']?.action },
  { type: 'video', id: 'C2_Reception', file: 'C2_Reception.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '접수하기', hudActive: 2, skip: false, action: eventMap['C2_Reception']?.action },
  { type: 'video', id: 'C2_WaitingRoom', file: 'C2_WaitingRoom.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '대기실 구경', hudActive: 2, skip: false, action: eventMap['C2_WaitingRoom']?.action },
  { type: 'video', id: 'C3_NameCall', file: 'C3_NameCall.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '내 이름 호명 듣기', skip: false, action: eventMap['C3_NameCall']?.action },
  { type: 'video', id: 'C4_DoctorGreet', file: 'C4_DoctorGreet.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '의사 선생님 인사', hudActive: 3, skip: false, afterEnd: 'choice-c5-route', action: eventMap['C4_DoctorGreet']?.action, actions: eventMap['C4_DoctorGreet']?.actions },
  { type: 'choice', id: 'choice-c5-route', question: '의사 선생님이 진료를 시작해요!\n어떤 방법으로 해볼까요?', options: [ { icon: '🩺', label: '검사해봐요\n(5-A 신뢰 루트)', next: 'C5A_Stethoscope' }, { icon: '🐻', label: '곰돌이 먼저요!\n(5-B 달래기 루트)', next: 'C5B_Stethoscope' } ] },
  { type: 'video', id: 'C5A_Stethoscope', file: 'C5A_Stethoscope.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '청진기 가슴 검사', hudActive: 3, skip: false, action: eventMap['C5A_Stethoscope']?.action, sensory: eventMap['C5A_Stethoscope']?.sensory, at: eventMap['C5A_Stethoscope']?.sensory?.at || 1 },
  { type: 'video', id: 'C5A_Throat', file: 'C5A_Throat.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '목 안 손전등 검사', hudActive: 3, skip: false, action: eventMap['C5A_Throat']?.action, sensory: eventMap['C5A_Throat']?.sensory, at: eventMap['C5A_Throat']?.sensory?.at || 1 },
  { type: 'video', id: 'C5A_Ear', file: 'C5A_Ear.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '귓속 이경 검사', hudActive: 3, skip: false, action: eventMap['C5A_Ear']?.action },
  { type: 'video', id: 'C5B_Stethoscope', file: 'C5A_Stethoscope.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '곰돌이 청진기 검사', hudActive: 3, skip: false, action: eventMap['C5B_Stethoscope']?.action, sensory: eventMap['C5B_Stethoscope']?.sensory, at: eventMap['C5B_Stethoscope']?.sensory?.at || 1 },
  { type: 'video', id: 'C5B_Throat', file: 'C5A_Throat.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '곰돌이 목 검사', hudActive: 3, skip: false, action: eventMap['C5B_Throat']?.action, sensory: eventMap['C5B_Throat']?.sensory, at: eventMap['C5B_Throat']?.sensory?.at || 1 },
  { type: 'video', id: 'C5B_Ear', file: 'C5A_Ear.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '곰돌이 귀 검사', hudActive: 3, skip: false, action: eventMap['C5B_Ear']?.action },
  { type: 'video', id: 'C5C_Notice', file: 'C5C_Notice.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '주사 준비', hudActive: 4, skip: false, action: eventMap['C5C_Notice']?.action, sensory: eventMap['C5C_Notice']?.sensory, at: eventMap['C5C_Notice']?.sensory?.at || 2 },
  { type: 'video', id: 'C5C_AlcWipe', file: 'C5C_AlcWipe.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '알코올 솜 쓱쓱', hudActive: 4, skip: false, action: eventMap['C5C_AlcWipe']?.action, sensory: eventMap['C5C_AlcWipe']?.sensory, at: eventMap['C5C_AlcWipe']?.sensory?.at || 0.5 },
  { type: 'video', id: 'C5C_Injection', file: 'C5C_Injection.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '예방 주사 맞기', hudActive: 4, skip: false, action: eventMap['C5C_Injection']?.action },
  { type: 'video', id: 'C5C_Bandage', file: 'C5C_Bandage.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '뽀로로 반창고', hudActive: 4, skip: false, action: eventMap['C5C_Bandage']?.action },
  { type: 'video', id: 'C6_Farewell', file: 'C6_Farewell.mp4', section: '🌟 3단계 · 내가 직접 체험하기', subLabel: '칭찬 스티커', hudActive: 5, skip: false, action: eventMap['C6_Farewell']?.action },
  { type: 'ending', title: '병원 진료 성공!', desc: '오늘 정말 용감하고 멋졌어요! 🐻💕' }
];

// Eye Clinic Episode Nodes (Step 1~3)
export const EYECLINIC_EPISODE = [
  { type: 'stepLabel', icon: '📖', num: '1단계', title: '안과 동화 미리보기', desc: '안과는 어떤 곳인지 따뜻하고 편안한 동화로 먼저 만나요!' },
  { type: 'video', id: 'eye-1-1', file: '1-1.mp4', section: '📖 1단계 · 안과 동화 미리보기', subLabel: '눈이 침침해요', skip: true },
  { type: 'video', id: 'eye-1-2', file: '1-2.mp4', section: '📖 1단계 · 안과 동화 미리보기', subLabel: '안과 건물의 모습', skip: true },
  { type: 'video', id: 'eye-1-3', file: '1-3.mp4', section: '📖 1단계 · 안과 동화 미리보기', subLabel: '눈이 반짝반짝', skip: true },
  { type: 'schedule' },
  { type: 'stepLabel', icon: '🧸', num: '2단계', title: '곰돌이의 입체 안과 기계 체험', desc: '곰돌이 코코가 신기한 안과 검사기를 먼저 체험해요! 🎈' },
  { type: 'video', id: 'eye-3-1', file: '3-1.mp4', section: '🧸 2단계 · 곰돌이의 안과 체험', subLabel: '턱받침에 턱 대기', skip: true },
  { type: 'video', id: 'eye-3-2', file: '3-2.mp4', section: '🧸 2단계 · 곰돌이의 안과 체험', subLabel: '열기구 관찰하기', skip: true },
  { type: 'video', id: 'eye-3-3', file: '3-3.mp4', section: '🧸 2단계 · 곰돌이의 안과 체험', subLabel: '멋진 별 선글라스 획득', skip: true },
  { type: 'ending', title: '안과 체험 성공!', desc: '코코와 함께 안과 탐험을 멋지게 완료했어요! 🦉🕶️✨' }
];

// Backwards compatibility default
export const EPISODE = HOSPITAL_EPISODE;
export const MOVIE_BASE = EPISODE_META.hospital.movieBase;

export const RESUME_AFTER_BRANCH = {
  'C1_HiPath': 'C2_Reception',
  'C1_HidePath': 'C2_Reception',
  'C5B_Stethoscope': 'C5B_Throat',
  'C5B_Throat': 'C5B_Ear',
  'C5B_Ear': 'C5C_Notice',
  'C5A_Ear': 'C5C_Notice'
};

export const episodeById = {};
HOSPITAL_EPISODE.forEach((node, i) => { if (node.id) episodeById[node.id] = i; });
