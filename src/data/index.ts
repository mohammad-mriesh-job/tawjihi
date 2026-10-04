import type { Question, Unit } from './types';
import { examMinutes } from '../lib/timing';
import { sample } from '../lib/random';
import u1 from './units/u1';
import u2 from './units/u2';
import u3 from './units/u3';
import u4 from './units/u4';
import u5 from './units/u5';
import u6 from './units/u6';
import u7 from './units/u7';

export const units: Unit[] = [u1, u2, u3, u4, u5, u6, u7];

export const questionById = new Map<string, Question>();
export const unitOfQuestion = new Map<string, Unit>();
for (const u of units)
  for (const e of u.exams)
    for (const q of e.questions) {
      if (questionById.has(q.id)) throw new Error(`duplicate question id ${q.id}`);
      questionById.set(q.id, q);
      unitOfQuestion.set(q.id, u);
    }

export function getUnit(id: string): Unit | undefined {
  return units.find((u) => u.id === id);
}

export interface ExamDescriptor {
  key: string;
  title: string;
  subtitle: string;
  backTo: string;
  /** fixed duration (mock exams) — otherwise derived from the questions */
  fixedMinutes?: number;
  pickQuestions: () => Question[];
}

export function minutesFor(d: ExamDescriptor, questions: Question[]): number {
  return d.fixedMinutes ?? examMinutes(questions);
}

interface MockDef {
  key: string;
  title: string;
  subtitle: string;
  minutes: number;
  /** questions drawn from each unit */
  perUnit: Record<string, number>;
}

/** Items per unit exactly as in the ministry paper of 2 July 2026 (50 items / 3 hours):
 *  U1 Q1–3, U2 Q4–8, U3 Q9–18, U4 Q19–25, U5 Q26–37, U6 Q38–45, U7 Q46–50. */
export const mocks: MockDef[] = [
  {
    key: 'mock-full',
    title: 'امتحان وزاري تجريبي شامل',
    subtitle: '50 سؤالًا من جميع الوحدات للفصلين — نفس عدد أسئلة وزمن الامتحان الوزاري',
    minutes: 180,
    perUnit: { u1: 3, u2: 5, u3: 10, u4: 7, u5: 12, u6: 8, u7: 5 },
  },
  {
    key: 'mock-s1',
    title: 'امتحان تجريبي — الفصل الأول',
    subtitle: '25 سؤالًا من وحدات الفصل الأول',
    minutes: 90,
    perUnit: { u1: 3, u2: 5, u3: 10, u4: 7 },
  },
  {
    key: 'mock-s2',
    title: 'امتحان تجريبي — الفصل الثاني',
    subtitle: '25 سؤالًا من وحدات الفصل الثاني',
    minutes: 90,
    perUnit: { u5: 12, u6: 8, u7: 5 },
  },
];

export function getExam(key: string): ExamDescriptor | undefined {
  const mock = mocks.find((m) => m.key === key);
  if (mock) {
    return {
      key,
      title: mock.title,
      subtitle: mock.subtitle,
      backTo: '/',
      fixedMinutes: mock.minutes,
      pickQuestions: () =>
        units.flatMap((u) => {
          const n = mock.perUnit[u.id] ?? 0;
          if (!n) return [];
          const pool = u.exams.flatMap((e) => e.questions);
          const order = new Map(pool.map((q, i) => [q.id, i]));
          return sample(pool, n).sort((a, b) => order.get(a.id)! - order.get(b.id)!);
        }),
    };
  }
  for (const u of units) {
    const exam = u.exams.find((e) => e.id === key);
    if (exam)
      return {
        key,
        title: exam.title,
        subtitle: `الوحدة ${u.number}: ${u.title}`,
        backTo: `/unit/${u.id}`,
        pickQuestions: () => exam.questions,
      };
  }
  return undefined;
}
