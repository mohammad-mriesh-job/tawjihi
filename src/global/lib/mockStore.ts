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
const REVISION: Record<string, number> = { 's1-m6': 2, 's1-m7': 2, 's1-m8': 2, 's1-m9': 2, 's1-m10': 2 };
const rev = (id: string) => (REVISION[id] ? `@${REVISION[id]}` : '');

export const mockKey = {
  session: (id: string) => `mock:session:${id}${rev(id)}`,
  result: (id: string) => `mock:result:${id}${rev(id)}`,
  attempts: (id: string) => `mock:attempts:${id}`,
};

export function mockAttempts(id: string): MockAttempt[] {
  return raw.get<MockAttempt[]>(mockKey.attempts(id)) ?? [];
}
