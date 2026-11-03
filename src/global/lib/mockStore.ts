import { raw } from './storage';

export interface MockSession {
  startedAt: number;
  endsAt: number;
  answers: (number | null)[];
  answeredAt: (number | null)[];
  announced: number[];
}
export interface MockResult {
  session: MockSession;
  finishedAt: number;
}
export interface MockAttempt {
  date: number;
  correct: number;
  total: number;
  seconds: number;
}

/** Papers whose questions were rewritten after publication. A saved session or result stores option indexes of the
 *  old questions, so those two keys get a revision suffix and old data is never applied to the new questions; the
 *  score history (attempts) is kept. */
const REVISION: Record<string, number> = {
  // 2026-10-15: semester-1 papers 6-10 rewritten; 2026-11-03: all ten semester-1 papers revised for variety
  's1-m1': 2, 's1-m2': 2, 's1-m3': 2, 's1-m4': 2, 's1-m5': 2,
  's1-m6': 3, 's1-m7': 3, 's1-m8': 3, 's1-m9': 3, 's1-m10': 3,
};
const rev = (id: string) => (REVISION[id] ? `@${REVISION[id]}` : '');

export const mockKey = {
  session: (id: string) => `mock:session:${id}${rev(id)}`,
  result: (id: string) => `mock:result:${id}${rev(id)}`,
  attempts: (id: string) => `mock:attempts:${id}`,
};

export function mockAttempts(id: string): MockAttempt[] {
  return raw.get<MockAttempt[]>(mockKey.attempts(id)) ?? [];
}
