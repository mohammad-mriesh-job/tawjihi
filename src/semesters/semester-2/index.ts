import type { Semester } from '../../global/data/types';
import u5 from './unit-5/u5';
import u6 from './unit-6/u6';
import u7 from './unit-7/u7';
import mocks from './mock-exams/s2';

const semester: Semester = {
  number: 2,
  title: 'الفصل الثاني',
  unitsLabel: 'الوحدات من 5 إلى 7',
  units: [u5, u6, u7],
  mocks,
};

export default semester;
