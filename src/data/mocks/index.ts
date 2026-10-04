import type { MockPaper } from '../types';
import { units } from '../index';
import s1 from './s1';
import s2 from './s2';

export const mockSets = [s1, s2];

export const setInfo: Record<string, { semester: string; units: string }> = {
  s1: { semester: 'الفصل الأول', units: 'الوحدات من 1 إلى 4' },
  s2: { semester: 'الفصل الثاني', units: 'الوحدات من 5 إلى 7' },
};

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
