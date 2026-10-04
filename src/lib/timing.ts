import type { Difficulty, Question } from '../data/types';

/**
 * The 2026 ministry paper: 50 items in 180 minutes (3.6 min / item on average).
 * Each item is weighted by its size so that a typical mix lands on that pace.
 */
export const MINUTES_PER_DIFFICULTY: Record<Difficulty, number> = {
  easy: 2.5,
  medium: 3.5,
  hard: 5,
};

export function examMinutes(questions: Question[]): number {
  const total = questions.reduce((sum, q) => sum + MINUTES_PER_DIFFICULTY[q.difficulty], 0);
  return Math.ceil(total);
}

export function formatClock(totalSeconds: number): string {
  const s = Math.max(0, Math.floor(totalSeconds));
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  const mm = String(m).padStart(2, '0');
  const ss = String(sec).padStart(2, '0');
  return h > 0 ? `${h}:${mm}:${ss}` : `${mm}:${ss}`;
}

export function formatMinutes(min: number): string {
  if (min < 60) return `${min} دقيقة`;
  const h = Math.floor(min / 60);
  const m = min % 60;
  const hours = h === 1 ? 'ساعة' : h === 2 ? 'ساعتان' : `${h} ساعات`;
  return m ? `${hours} و${m} دقيقة` : hours;
}
