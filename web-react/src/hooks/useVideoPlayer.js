import { useRef, useEffect, useCallback } from 'react';
import { MOVIE_BASE, EPISODE, RESUME_AFTER_BRANCH, episodeById } from '../data/episode';

export function useVideoPlayer({ cursor, setCursor, currentNode, setCurrentNode, onShowScreen }) {
  const videoARef = useRef(null);
  const videoBRef = useRef(null);
  const activeVideoRef = useRef(null);
  const inactiveVideoRef = useRef(null);
  const preloadedRef = useRef(false);

  // Initialize refs
  useEffect(() => {
    activeVideoRef.current = videoARef.current;
    inactiveVideoRef.current = videoBRef.current;
  }, []);

  const nextAfterNode = useCallback((node) => {
    if (!node) return;
    if (node.afterEnd) {
      const idx = episodeById[node.afterEnd];
      if (idx !== undefined) { setCursor(idx); return; }
    }
    if (RESUME_AFTER_BRANCH[node.id]) {
      const idx = episodeById[RESUME_AFTER_BRANCH[node.id]];
      if (idx !== undefined) { setCursor(idx); return; }
    }
    setCursor(prev => {
      let next = prev + 1;
      while (next < EPISODE.length && EPISODE[next].type === 'choice') next++;
      return next >= EPISODE.length ? -1 : next; // -1 = ending
    });
  }, [setCursor]);

  const playVideo = useCallback((node) => {
    const target = inactiveVideoRef.current;
    const old = activeVideoRef.current;
    if (!target) return;

    target.src = MOVIE_BASE + node.file;
    target.currentTime = 0;
    preloadedRef.current = false;

    target.play().catch(() => {});

    target.classList.add('active');
    old?.classList.remove('active');

    activeVideoRef.current = target;
    inactiveVideoRef.current = old;
  }, []);

  const skipCurrent = useCallback(() => {
    activeVideoRef.current?.pause();
    if (currentNode) nextAfterNode(currentNode);
  }, [currentNode, nextAfterNode]);

  return { videoARef, videoBRef, activeVideoRef, inactiveVideoRef, preloadedRef, nextAfterNode, playVideo, skipCurrent };
}
