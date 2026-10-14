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

export const mockKey = {
  session: (id: string) => `mock:session:${id}`,
  result: (id: string) => `mock:result:${id}`,
  attempts: (id: string) => `mock:attempts:${id}`,
};

export function mockAttempts(id: string): MockAttempt[] {
  return raw.get<MockAttempt[]>(mockKey.attempts(id)) ?? [];
}
