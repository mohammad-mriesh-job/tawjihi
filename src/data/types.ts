export type Difficulty = 'easy' | 'medium' | 'hard';

/**
 * Text fields support inline math between $...$ and display math between $$...$$ (KaTeX).
 */
/** Teaching-style worked solution shown when reviewing a question. */
export interface Explanation {
  /** how to recognise the method from the wording of the question */
  idea: string;
  /** numbered steps, each with its reason */
  steps: string[];
  /** a faster exam technique (substituting options, elimination), when one genuinely exists */
  quick?: string;
  /** why each option is wrong, indexed like `options` (null for the correct one) */
  wrong: (string | null)[];
  /** a warning or habit for the exam */
  tip?: string;
}

export interface Question {
  id: string;
  lesson: string;
  difficulty: Difficulty;
  text: string;
  options: [string, string, string, string];
  /** index of the correct option in `options` */
  answer: 0 | 1 | 2 | 3;
  solution: string;
  /** detailed explanation; when present it replaces `solution` in the review */
  explain?: Explanation;
  /** optional figure (path under public/, e.g. "fig/u3e1q5.svg") shown under the question text */
  figure?: string;
}

export interface Lesson {
  id: string;
  title: string;
}

export interface Exam {
  id: string;
  title: string;
  questions: Question[];
}

export interface Unit {
  id: string;
  number: number;
  semester: 1 | 2;
  title: string;
  description: string;
  lessons: Lesson[];
  exams: Exam[];
}

export interface MockQuestion extends Question {
  /** skill group used in the results analysis */
  tag: string;
  /** finer question pattern shown in the review */
  pattern?: string;
  /** shared stem / note printed above this item (like the ministry paper) */
  lead?: string;
  /** number of consecutive items (starting here) that share the lead and stay on one page */
  group?: number;
}

export interface MockPaper {
  id: string;
  model: number;
  title: string;
  minutes: number;
  questions: MockQuestion[];
  answerSpread: number[];
}

export interface MockSet {
  id: string;
  title: string;
  subtitle: string;
  exams: MockPaper[];
}
