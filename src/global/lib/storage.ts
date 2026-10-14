const PREFIX = 'tawjihi-math-v2:';

function read<T>(key: string): T | null {
  try {
    const raw = localStorage.getItem(PREFIX + key);
    return raw ? (JSON.parse(raw) as T) : null;
  } catch {
    return null;
  }
}

function write(key: string, value: unknown) {
  try {
    localStorage.setItem(PREFIX + key, JSON.stringify(value));
  } catch {
    /* storage unavailable: progress simply isn't kept */
  }
}

function remove(key: string) {
  try {
    localStorage.removeItem(PREFIX + key);
  } catch {
    /* ignore */
  }
}

export interface Attempt {
  date: number;
  correct: number;
  total: number;
  seconds: number;
}

export interface Session {
  questionIds: string[];
  /** per question: permutation of the 4 original option indexes, in display order */
  optionOrder: number[][];
  /** per question: selected ORIGINAL option index, or null */
  answers: (number | null)[];
  flags: boolean[];
  current: number;
  startedAt: number;
  endsAt: number;
}

export interface Result {
  session: Session;
  finishedAt: number;
}

export const raw = { get: read, set: write, del: remove };

export const storage = {
  attempts: (examKey: string) => read<Attempt[]>(`attempts:${examKey}`) ?? [],
  addAttempt(examKey: string, a: Attempt) {
    write(`attempts:${examKey}`, [...storage.attempts(examKey), a]);
  },
  session: (examKey: string) => read<Session>(`session:${examKey}`),
  saveSession: (examKey: string, s: Session) => write(`session:${examKey}`, s),
  clearSession: (examKey: string) => remove(`session:${examKey}`),
  result: (examKey: string) => read<Result>(`result:${examKey}`),
  saveResult: (examKey: string, r: Result) => write(`result:${examKey}`, r),
  clearResult: (examKey: string) => remove(`result:${examKey}`),
};

export function bestPercent(examKey: string): number | null {
  const list = storage.attempts(examKey);
  if (!list.length) return null;
  return Math.max(...list.map((a) => Math.round((a.correct / a.total) * 100)));
}
