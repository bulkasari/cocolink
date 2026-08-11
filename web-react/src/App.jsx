import { useState, useEffect, useRef, useCallback } from 'react';
import { EPISODE, MOVIE_BASE, episodeById, RESUME_AFTER_BRANCH } from './data/episode';
import './App.css';

const HUD_STEPS = [
  { id: 1, icon: '🏥', label: '입구' },
  { id: 2, icon: '📋', label: '접수' },
  { id: 3, icon: '🩺', label: '진료' },
  { id: 4, icon: '💉', label: '주사' },
  { id: 5, icon: '🎁', label: '보상' },
];

export default function App() {
  const [screen, setScreen] = useState('intro'); // intro | stepLabel | schedule | video | ending
  const [cursor, setCursor] = useState(0);
  const [currentNode, setCurrentNode] = useState(null);
  const [hudActive, setHudActive] = useState(0);
  const [stepData, setStepData] = useState(null);
  const [choices, setChoices] = useState(null);
  const [sensory, setSensory] = useState(null);
  const [showSkip, setShowSkip] = useState(false);
  const [showTap, setShowTap] = useState(false);
  const [progress, setProgress] = useState(0);
  const [clipLabel, setClipLabel] = useState('');

  const videoARef = useRef(null);
  const videoBRef = useRef(null);
  const activeRef = useRef(null);
  const inactiveRef = useRef(null);
  const sensoryTimer = useRef(null);
  const labelTimer = useRef(null);
  const scheduleTimer = useRef(null);
  const preloadDone = useRef(false);
  const currentNodeRef = useRef(null); // stale closure 방지용 ref

  // Build id->index map
  const episodeMap = useRef(episodeById);

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
      while (next < EPISODE.length && EPISODE[next].type === 'choice') next++;
      return next;
    });
  }, [advance]);

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
      if (labelTimer.current) clearTimeout(labelTimer.current);
      labelTimer.current = setTimeout(() => {
        setCursor(prev => prev + 1);
      }, 3200);
      return;
    }

    if (node.type === 'schedule') {
      setScreen('schedule');
      if (scheduleTimer.current) clearTimeout(scheduleTimer.current);
      scheduleTimer.current = setTimeout(() => {
        setCursor(prev => prev + 1);
      }, 4000);
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
      setScreen('video');
      setClipLabel(node.label || '');
      setShowSkip(!!node.skip);
      setShowTap(false);
      setProgress(0);
      preloadDone.current = false;
      if (node.hudActive) setHudActive(node.hudActive);
      if (node.sensory) showSensoryMsg(node.sensory.icon, node.sensory.text, node.at || 1);

      const target = inactiveRef.current;
      const old = activeRef.current;
      if (!target) return;

      const videoUrl = MOVIE_BASE + node.file;
      console.log('[CocoLink Video] Loading:', videoUrl);
      target.src = videoUrl;
      target.load();
      target.currentTime = 0;
      target.muted = false; // try unmuted playback since user interacted
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

      activeRef.current = target;
      inactiveRef.current = old;
    }
  }, [clearSensory, showSensoryMsg]);

  // currentNode가 바뀔 때마다 ref 동기화
  useEffect(() => { currentNodeRef.current = currentNode; }, [currentNode]);

  // ── Advance cursor → play node ───────────────────────────────────────
  useEffect(() => {
    if (cursor < 0) return;
    if (cursor >= EPISODE.length) {
      playNode({ type: 'ending' });
      return;
    }
    const node = EPISODE[cursor];
    playNode(node);
  }, [cursor]); // eslint-disable-line

  // ── Init video refs ─────────────────────────────────────────────────
  useEffect(() => {
    if (videoARef.current && videoBRef.current) {
      activeRef.current = videoARef.current;
      inactiveRef.current = videoBRef.current;
      // Initialize opacity
      videoARef.current.style.opacity = '0';
      videoBRef.current.style.opacity = '0';
    }
  }, []);

  // ── Video event handlers ────────────────────────────────────────────
  const handleVideoEnded = useCallback((v) => {
    if (v !== activeRef.current) return;
    clearSensory();
    nextAfterNode(currentNodeRef.current); // ref로 최신 값 참조
  }, [clearSensory, nextAfterNode]);

  const handleTimeUpdate = useCallback((v) => {
    if (v !== activeRef.current) return;
    if (v.duration) {
      const pct = (v.currentTime / v.duration) * 100;
      setProgress(pct);
      // Preload at 50%
      if (!preloadDone.current && pct >= 50) {
        preloadDone.current = true;
        const cur = EPISODE.findIndex(n => n.file && v.src.endsWith(n.file));
        let next = cur + 1;
        while (next < EPISODE.length && EPISODE[next].type !== 'video') next++;
        if (next < EPISODE.length && inactiveRef.current) {
          inactiveRef.current.src = MOVIE_BASE + EPISODE[next].file;
          inactiveRef.current.load();
        }
      }
    }
  }, []);

  const skipVideo = useCallback(() => {
    activeRef.current?.pause();
    clearSensory();
    setCurrentNode(prev => { nextAfterNode(prev); return prev; });
  }, [clearSensory, nextAfterNode]);

  const handleRestart = useCallback(() => {
    setCurrentNode(null);
    setHudActive(0);
    setProgress(0);
    setChoices(null);
    setSensory(null);
    setScreen('intro');
  }, []);

  const handleStart = useCallback(() => {
    setCursor(-1);
    setTimeout(() => setCursor(0), 10);
  }, []);

  // ── Render ──────────────────────────────────────────────────────────
  return (
    <div id="app" onClick={screen === 'intro' ? handleStart : undefined} style={screen === 'intro' ? { cursor: 'pointer' } : {}}>
      {/* HUD */}
      {screen === 'video' && (
        <div id="hud">
          <span className="hud-logo">🐻 CocoLink</span>
          <div className="hud-steps">
            {HUD_STEPS.map((s, i) => (
              <>
                {i > 0 && <span key={`arrow-${s.id}`} className="hud-arrow">›</span>}
                <div key={s.id} className={`hud-step ${hudActive === s.id ? 'active' : hudActive > s.id ? 'done' : ''}`}>
                  <span>{s.icon}</span> {s.label}
                </div>
              </>
            ))}
          </div>
        </div>
      )}

      {/* Progress bar */}
      <div id="progress-bar" style={{ width: `${progress}%` }} />

      {/* Intro */}
      {screen === 'intro' && (
        <div id="screen-intro" className="screen active">
          <div className="intro-badge">🐻</div>
          <h1 className="intro-title">CocoLink</h1>
          <p className="intro-sub">소아과 병원 적응 인터랙티브 에피소드<br />발달지연·자폐스펙트럼 아동을 위한 4단계 체험</p>
          <div className="tap-hint">👆 화면을 터치하세요</div>
          <div className="version-tag">v1.2 · Hospital Episode</div>
        </div>
      )}

      {/* Step Label */}
      {screen === 'stepLabel' && stepData && (
        <div id="screen-step-label" className="screen active">
          <div className="step-label-icon">{stepData.icon}</div>
          <div className="step-label-num">{stepData.num}</div>
          <div className="step-label-title">{stepData.title}</div>
          <div className="step-label-desc">{stepData.desc}</div>
        </div>
      )}

      {/* Visual Schedule */}
      {screen === 'schedule' && (
        <div id="screen-schedule" className="screen active">
          <div className="schedule-title">🗓️ 오늘 병원에서는요~</div>
          <div className="schedule-cards">
            {[['🏥','1단계','병원 입구'],['📋','2단계','접수 대기'],['🩺','3단계','의사 진료'],['💉','4단계','건강 주사'],['🎁','5단계','칭찬 보상']].map(([icon, step, label]) => (
              <div key={step} className="sched-card">
                <div className="sched-icon">{icon}</div>
                <div className="sched-label">{step}<br />{label}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Video Container (always mounted so refs are non-null) */}
      <div id="screen-video" className={`screen ${screen === 'video' ? 'active' : ''}`} style={screen !== 'video' ? { display: 'none' } : {}}>
        <div id="player-wrap">
          <video
            ref={videoARef}
            className="video-layer"
            playsInline
            muted
            autoPlay
            preload="auto"
            onEnded={() => handleVideoEnded(videoARef.current)}
            onTimeUpdate={() => handleTimeUpdate(videoARef.current)}
            onError={(e) => console.error('[Video Error A]:', e.target.error, e.target.src)}
          />
          <video
            ref={videoBRef}
            className="video-layer"
            playsInline
            muted
            autoPlay
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

          <div id="clip-label">{clipLabel}</div>
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
          <div className="ending-badge">🏅</div>
          <div className="ending-title">진료 성공!</div>
          <p style={{ color: 'var(--text-dim)', fontSize: '18px' }}>오늘 정말 용감하고 멋졌어요! 🐻💕</p>
          <button className="btn-restart" onClick={handleRestart}>처음부터 다시 🔄</button>
        </div>
      )}
    </div>
  );
}
