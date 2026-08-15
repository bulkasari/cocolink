import { useState, useEffect, useRef, useCallback } from 'react';
import { 
  EPISODE_TYPES, 
  EPISODE_META, 
  HOSPITAL_EPISODE, 
  EYECLINIC_EPISODE, 
  RESUME_AFTER_BRANCH, 
  eventMap 
} from './data/episode';
import './App.css';

export default function App() {
  const [selectedEpisode, setSelectedEpisode] = useState(EPISODE_TYPES.HOSPITAL);
  const [screen, setScreen] = useState('intro'); // intro | stepLabel | schedule | video | ending
  const [cursor, setCursor] = useState(-1);
  const [currentNode, setCurrentNode] = useState(null);
  const [hudActive, setHudActive] = useState(0);
  const [stepData, setStepData] = useState(null);
  const [choices, setChoices] = useState(null);
  const [sensory, setSensory] = useState(null);
  const [showSkip, setShowSkip] = useState(false);
  const [showTap, setShowTap] = useState(false);
  const [progress, setProgress] = useState(0);
  const [clipLabel, setClipLabel] = useState('');
  const [actionPrompt, setActionPrompt] = useState(null);

  const videoARef = useRef(null);
  const videoBRef = useRef(null);
  const activeRef = useRef(null);
  const inactiveRef = useRef(null);
  const sensoryTimer = useRef(null);
  const preloadDone = useRef(false);
  const actionDone = useRef(false);
  const currentNodeRef = useRef(null);

  // Active Episode Data
  const currentEpisodeList = selectedEpisode === EPISODE_TYPES.EYECLINIC ? EYECLINIC_EPISODE : HOSPITAL_EPISODE;
  const currentMeta = EPISODE_META[selectedEpisode] || EPISODE_META.hospital;
  const episodeMovieBase = currentMeta.movieBase;

  // Build id->index map
  const episodeMap = useRef({});
  useEffect(() => {
    const map = {};
    currentEpisodeList.forEach((node, i) => {
      if (node.id) map[node.id] = i;
    });
    episodeMap.current = map;
  }, [selectedEpisode, currentEpisodeList]);

  // ── Navigation helpers ──────────────────────────────────────────────
  const advance = useCallback((id) => {
    const idx = episodeMap.current[id];
    if (idx !== undefined) setCursor(idx);
  }, []);

  const nextAfterNode = useCallback((node) => {
    if (!node) return;
    if (node.afterEnd) { advance(node.afterEnd); return; }
    if (RESUME_AFTER_BRANCH[node.id]) { advance(RESUME_AFTER_BRANCH[node.id]); return; }
    setCursor(prev => {
      let next = prev + 1;
      while (next < currentEpisodeList.length && currentEpisodeList[next].type === 'choice') next++;
      return next;
    });
  }, [advance, currentEpisodeList]);

  const clearSensory = useCallback(() => {
    if (sensoryTimer.current) clearTimeout(sensoryTimer.current);
    setSensory(null);
  }, []);

  const showSensoryMsg = useCallback((icon, text, delay) => {
    clearSensory();
    sensoryTimer.current = setTimeout(() => {
      setSensory({ icon, text });
      sensoryTimer.current = setTimeout(() => setSensory(null), 3000);
    }, delay * 1000);
  }, [clearSensory]);

  // ── Play a node ──────────────────────────────────────────────────────
  const playNode = useCallback((node) => {
    if (!node) return;
    setCurrentNode(node);
    clearSensory();
    setChoices(null);

    if (node.type === 'stepLabel') {
      setScreen('stepLabel');
      setStepData(node);
      return;
    }

    if (node.type === 'schedule') {
      setScreen('schedule');
      return;
    }

    if (node.type === 'choice') {
      setChoices(node);
      return;
    }

    if (node.type === 'ending') {
      setScreen('ending');
      setProgress(100);
      return;
    }

    if (node.type === 'video') {
      // Dynamic merge from eventMap
      if (node.id && eventMap[node.id]) {
        const ev = eventMap[node.id];
        if (ev.action) node.action = ev.action;
        if (ev.actions) node.actions = ev.actions;
        if (ev.sensory) node.sensory = ev.sensory;
      }

      setScreen('video');
      setClipLabel({ section: node.section || '', sub: node.subLabel || node.label || '' });
      setShowSkip(!!node.skip);
      setShowTap(false);
      setProgress(0);
      setActionPrompt(null);
      preloadDone.current = false;
      actionDone.current = false;
      if (node.actions && Array.isArray(node.actions)) {
        node.actions.forEach(a => { a.triggered = false; });
      }
      if (node.hudActive) setHudActive(node.hudActive);
      if (node.sensory && node.sensory.enabled !== false) {
        showSensoryMsg(node.sensory.icon, node.sensory.text, node.sensory.at || node.at || 1);
      }

      const target = inactiveRef.current;
      const old = activeRef.current;
      if (!target) return;

      const videoUrl = episodeMovieBase + node.file;
      console.log('[CocoLink Video] Loading:', videoUrl);
      target.src = videoUrl;
      target.load();
      target.currentTime = 0;
      target.muted = false;
      const p = target.play();
      if (p !== undefined) {
        p.catch((err) => {
          console.warn('[CocoLink Video] Auto-play unmuted failed, falling back to muted playback:', err);
          target.muted = true;
          target.play().catch((err2) => {
            console.warn('[CocoLink Video] Muted play also failed:', err2);
            setShowTap(true);
          });
        });
      }

      // crossfade
      target.style.opacity = '1';
      target.style.pointerEvents = 'all';
      if (old) { old.style.opacity = '0'; old.style.pointerEvents = 'none'; }

      // swap
      const temp = activeRef.current;
      activeRef.current = inactiveRef.current;
      inactiveRef.current = temp;
    }
  }, [clearSensory, episodeMovieBase, showSensoryMsg]);

  // Sync ref
  useEffect(() => {
    currentNodeRef.current = currentNode;
  }, [currentNode]);

  // Init dual video refs
  useEffect(() => {
    activeRef.current = videoARef.current;
    inactiveRef.current = videoBRef.current;
  }, []);

  // Cursor change trigger
  useEffect(() => {
    if (cursor < 0 || cursor >= currentEpisodeList.length) return;
    playNode(currentEpisodeList[cursor]);
  }, [cursor, playNode, currentEpisodeList]);

  // Video End / TimeUpdate handlers
  const handleVideoEnded = useCallback((v) => {
    if (v !== activeRef.current) return;
    const node = currentNodeRef.current;
    if (!node) return;

    if (node.afterEnd) { advance(node.afterEnd); return; }
    if (RESUME_AFTER_BRANCH[node.id]) { advance(RESUME_AFTER_BRANCH[node.id]); return; }

    setCursor(prev => {
      let next = prev + 1;
      while (next < currentEpisodeList.length && currentEpisodeList[next].type === 'choice') next++;
      return next;
    });
  }, [advance, currentEpisodeList]);

  const handleTimeUpdate = useCallback((v) => {
    if (v !== activeRef.current || !v.duration) return;
    const pct = (v.currentTime / v.duration) * 100;
    setProgress(pct);

    const node = currentNodeRef.current;
    if (node) {
      // Multiple Actions
      if (node.actions && Array.isArray(node.actions)) {
        node.actions.forEach(act => {
          if (!act.triggered && v.currentTime >= act.at) {
            act.triggered = true;
            v.pause();
            setActionPrompt(act);
          }
        });
      }
      // Single Action
      else if (node.action && !actionDone.current && typeof node.action.at === 'number') {
        if (v.currentTime >= node.action.at) {
          v.pause();
          actionDone.current = true;
          setActionPrompt(node.action);
        }
      }

      // Preload at 50%
      if (!preloadDone.current && pct >= 50) {
        preloadDone.current = true;
        const cur = currentEpisodeList.findIndex(n => n.file && v.src.endsWith(n.file));
        let next = cur + 1;
        while (next < currentEpisodeList.length && currentEpisodeList[next].type !== 'video') next++;
        if (next < currentEpisodeList.length && inactiveRef.current) {
          inactiveRef.current.src = episodeMovieBase + currentEpisodeList[next].file;
          inactiveRef.current.load();
        }
      }
    }
  }, [currentEpisodeList, episodeMovieBase]);

  const skipVideo = useCallback(() => {
    activeRef.current?.pause();
    clearSensory();
    setActionPrompt(null);
    setCurrentNode(prev => { nextAfterNode(prev); return prev; });
  }, [clearSensory, nextAfterNode]);

  // Keyboard Shortcuts
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'ArrowRight' || e.key === 'n' || e.key === 'N') {
        e.preventDefault();
        activeRef.current?.pause();
        clearSensory();
        setActionPrompt(null);
        setCursor(prev => Math.min(prev + 1, currentEpisodeList.length - 1));
      } else if (e.key === 'ArrowLeft' || e.key === 'p' || e.key === 'P') {
        e.preventDefault();
        activeRef.current?.pause();
        clearSensory();
        setActionPrompt(null);
        setCursor(prev => Math.max(prev - 1, 0));
      } else if (e.key === ' ' || e.key === 'Spacebar') {
        e.preventDefault();
        skipVideo();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [clearSensory, skipVideo, currentEpisodeList]);

  const handleRestart = useCallback(() => {
    setCurrentNode(null);
    setHudActive(0);
    setProgress(0);
    setChoices(null);
    setSensory(null);
    setCursor(-1);
    setScreen('intro');
  }, []);

  const handleStart = useCallback((episodeType) => {
    setSelectedEpisode(episodeType);
    if (videoARef.current) videoARef.current.muted = false;
    if (videoBRef.current) videoBRef.current.muted = false;
    
    // Select episode list based on clicked type
    const targetList = episodeType === EPISODE_TYPES.EYECLINIC ? EYECLINIC_EPISODE : HOSPITAL_EPISODE;
    setCursor(0);
    playNode(targetList[0]);
  }, [playNode]);

  return (
    <div id="app">
      {/* Top Floating Home Button on Step Screens */}
      {(screen === 'stepLabel' || screen === 'schedule') && (
        <button className="btn-home-floating" onClick={handleRestart} title="처음 메뉴로 돌아가기">
          🏠 처음으로
        </button>
      )}

      {/* HUD Bar (Top Navigation) */}
      {screen === 'video' && (
        <div id="hud">
          <div className="hud-left">
            <button className="hud-home-btn" onClick={handleRestart} title="처음 메뉴로 돌아가기">
              🏠
            </button>
            <span className="hud-logo">{currentMeta.badge} CocoLink</span>
            {typeof clipLabel === 'object' && clipLabel.section && (
              <div className="hud-current-info">
                <span className="hud-section-badge">{clipLabel.section}</span>
                <span className="hud-sub-title">| {clipLabel.sub}</span>
              </div>
            )}
          </div>
          <div className="hud-steps">
            {currentMeta.hudSteps.map((s, i) => (
              <span key={s.id} style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                {i > 0 && <span className="hud-arrow">›</span>}
                <div className={`hud-step ${hudActive === s.id ? 'active' : hudActive > s.id ? 'done' : ''}`}>
                  <span>{s.icon}</span> <span className="hud-step-text">{s.label}</span>
                </div>
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Progress bar */}
      <div id="progress-bar" style={{ width: `${progress}%` }} />

      {/* Intro & Episode Selector */}
      {screen === 'intro' && (
        <div id="screen-intro" className="screen active">
          <div className="intro-badge">✨</div>
          <h1 className="intro-title">CocoLink</h1>
          <p className="intro-sub">아이들의 편안하고 즐거운 병원 적응을 돕는 인터랙티브 체험</p>
          
          <div className="episode-selector">
            <div 
              className={`episode-card ${selectedEpisode === EPISODE_TYPES.HOSPITAL ? 'selected' : ''}`}
              onClick={() => setSelectedEpisode(EPISODE_TYPES.HOSPITAL)}
            >
              <div className="card-badge">🐻</div>
              <div className="card-title">소아과 병원</div>
              <div className="card-desc">1~4단계 풀 에피소드<br/>(동화 ➔ 관찰 ➔ 1인칭 실사)</div>
              <button className="btn-play-card" onClick={(e) => { e.stopPropagation(); handleStart(EPISODE_TYPES.HOSPITAL); }}>
                소아과 시작하기 ▶
              </button>
            </div>

            <div 
              className={`episode-card ${selectedEpisode === EPISODE_TYPES.EYECLINIC ? 'selected' : ''}`}
              onClick={() => setSelectedEpisode(EPISODE_TYPES.EYECLINIC)}
            >
              <div className="card-badge">🦉</div>
              <div className="card-title">소아 안과 (신규)</div>
              <div className="card-desc">1~3단계 적응 에피소드<br/>(2D 동화 ➔ 3D 기계 시연)</div>
              <button className="btn-play-card" onClick={(e) => { e.stopPropagation(); handleStart(EPISODE_TYPES.EYECLINIC); }}>
                안과 시작하기 ▶
              </button>
            </div>
          </div>

          <div className="version-tag">v1.3 · Hospital & EyeClinic Multi-Episode</div>
        </div>
      )}

      {/* Step Label */}
      {screen === 'stepLabel' && stepData && (
        <div id="screen-step-label" className="screen active">
          <div className="step-label-icon">{stepData.icon}</div>
          <div className="step-label-num">{stepData.num}</div>
          <div className="step-label-title">{stepData.title}</div>
          <div className="step-label-desc">{stepData.desc}</div>
          <button className="btn-next-step" onClick={() => setCursor(prev => prev + 1)}>
            다음 단계로 이동하기 ▶
          </button>
        </div>
      )}

      {/* Visual Schedule */}
      {screen === 'schedule' && (
        <div id="screen-schedule" className="screen active">
          <div className="schedule-title">🗓️ 오늘 {currentMeta.title}에서는요~</div>
          <div className="schedule-cards">
            {currentMeta.scheduleCards.map(([icon, step, label]) => (
              <div key={step} className="sched-card">
                <div className="sched-icon">{icon}</div>
                <div className="sched-label">{step}<br />{label}</div>
              </div>
            ))}
          </div>
          <button className="btn-next-step" onClick={() => setCursor(prev => prev + 1)} style={{ marginTop: '24px' }}>
            체험 시작하기 ▶
          </button>
        </div>
      )}

      {/* Video Container */}
      <div id="screen-video" className={`screen ${screen === 'video' ? 'active' : ''}`} style={screen !== 'video' ? { display: 'none' } : {}}>
        <div id="player-wrap">
          <video
            ref={videoARef}
            className="video-layer"
            playsInline
            preload="auto"
            onEnded={() => handleVideoEnded(videoARef.current)}
            onTimeUpdate={() => handleTimeUpdate(videoARef.current)}
            onError={(e) => console.error('[Video Error A]:', e.target.error, e.target.src)}
          />
          <video
            ref={videoBRef}
            className="video-layer"
            playsInline
            preload="auto"
            onEnded={() => handleVideoEnded(videoBRef.current)}
            onTimeUpdate={() => handleTimeUpdate(videoBRef.current)}
            onError={(e) => console.error('[Video Error B]:', e.target.error, e.target.src)}
          />

          {/* Sensory popup */}
          {sensory && (
            <div id="sensory-popup" className="show">
              <span>{sensory.icon}</span>
              <span>{sensory.text}</span>
            </div>
          )}

          {/* Action Prompt Overlay */}
          {actionPrompt && (
            <div id="action-overlay" className="show">
              <button
                className="action-btn"
                onClick={() => {
                  setActionPrompt(null);
                  if (activeRef.current) activeRef.current.play();
                }}
              >
                <span className="action-icon">{actionPrompt.icon}</span>
                <span className="action-text">{actionPrompt.label}</span>
              </button>
            </div>
          )}

          {/* PECS choice overlay */}
          {choices && (
            <div id="choices-overlay" className="show">
              <div className="choices-question">{choices.question}</div>
              <div className="choices-row">
                {choices.options.map(opt => (
                  <div key={opt.next} className="choice-card" onClick={() => { setChoices(null); advance(opt.next); }}>
                    <div className="choice-icon">{opt.icon}</div>
                    <div className="choice-label">{opt.label.replace(/\n/g, '\n')}</div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {showSkip && <button id="skip-btn" onClick={skipVideo}>건너뛰기 ›</button>}
          {showTap && (
            <div
              id="tap-continue"
              className="show"
              onClick={() => {
                setShowTap(false);
                if (activeRef.current) {
                  activeRef.current.muted = false;
                  activeRef.current.play();
                }
              }}
            >
              👆 화면을 탭하여 재생하기
            </div>
          )}
        </div>
      </div>

      {/* Ending */}
      {screen === 'ending' && (
        <div id="screen-ending" className="screen active">
          <div className="ending-badge">{selectedEpisode === EPISODE_TYPES.EYECLINIC ? '🕶️' : '🏅'}</div>
          <div className="ending-title">{currentNode?.title || '진료 성공!'}</div>
          <p style={{ color: 'var(--text-dim)', fontSize: '18px' }}>
            {currentNode?.desc || '오늘 정말 용감하고 멋졌어요! 🐻💕'}
          </p>
          <button className="btn-restart" onClick={handleRestart}>다른 에피소드 선택 🔄</button>
        </div>
      )}
    </div>
  );
}
