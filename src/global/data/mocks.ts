import type { MockPaper, MockSet } from './types';
import { units } from './index';
import { semesters } from '../../semesters';

export const mockSets: MockSet[] = semesters.flatMap((s) => (s.mocks ? [s.mocks] : []));

export const setInfo: Record<string, { semester: string; units: string }> = Object.fromEntries(
  semesters.flatMap((s) => (s.mocks ? [[s.mocks.id, { semester: s.title, units: s.unitsLabel }]] : [])),
);

export function setOfPaper(id: string) {
  return mockSets.find((set) => set.exams.some((e) => e.id === id));
}

export function getPaper(id: string): MockPaper | undefined {
  for (const set of mockSets) {
    const p = set.exams.find((e) => e.id === id);
    if (p) return p;
  }
  return undefined;
}

export function unitOfLesson(lessonId: string) {
  return units.find((u) => u.lessons.some((l) => l.id === lessonId));
}
