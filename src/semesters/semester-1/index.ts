import type { Semester } from '../../global/data/types';
import u1 from './unit-1/u1';
import u2 from './unit-2/u2';
import u3 from './unit-3/u3';
import u4 from './unit-4/u4';
import mocks from './mock-exams/s1';

const semester: Semester = {
  number: 1,
  title: 'الفصل الأول',
  unitsLabel: 'الوحدات من 1 إلى 4',
  units: [u1, u2, u3, u4],
  mocks,
};

export default semester;
