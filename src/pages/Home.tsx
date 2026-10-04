import { Link as RouterLink } from 'react-router-dom';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import CardContent from '@mui/material/CardContent';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid';
import LinearProgress from '@mui/material/LinearProgress';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import TimerOutlinedIcon from '@mui/icons-material/TimerOutlined';
import QuizOutlinedIcon from '@mui/icons-material/QuizOutlined';
import AssignmentTurnedInOutlinedIcon from '@mui/icons-material/AssignmentTurnedInOutlined';
import MenuBookOutlinedIcon from '@mui/icons-material/MenuBookOutlined';
import DescriptionOutlinedIcon from '@mui/icons-material/DescriptionOutlined';
import ShuffleOutlinedIcon from '@mui/icons-material/ShuffleOutlined';
import WorkspacePremiumOutlinedIcon from '@mui/icons-material/WorkspacePremiumOutlined';
import type { ReactNode } from 'react';
import { mocks, units } from '../data';
import { mockSets, setInfo } from '../data/mocks';
import { mockAttempts } from '../lib/mockStore';
import type { MockSet, Unit } from '../data/types';
import { bestPercent } from '../lib/storage';
import { formatMinutes } from '../lib/timing';

const SEMESTERS = [
  { n: 1, title: 'الفصل الدراسي الأول', units: 'الوحدات من 1 إلى 4', color: '#1d4e89', tint: '#eef3fa' },
  { n: 2, title: 'الفصل الدراسي الثاني', units: 'الوحدات من 5 إلى 7', color: '#0f766e', tint: '#ecf6f4' },
];

function scrollTo(id: string) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function UnitCard({ unit, color }: { unit: Unit; color: string }) {
  const scores = unit.exams.map((e) => bestPercent(e.id));
  const done = scores.filter((s) => s !== null).length;
  const questions = unit.exams.reduce((n, e) => n + e.questions.length, 0);
  return (
    <Card sx={{ height: '100%' }}>
      <CardActionArea component={RouterLink} to={`/unit/${unit.id}`} sx={{ height: '100%', alignItems: 'stretch' }}>
        <CardContent>
          <Stack direction="row" spacing={1.5} sx={{ alignItems: 'center', mb: 1 }}>
            <Box
              sx={{
                width: 44,
                height: 44,
                borderRadius: '50%',
                bgcolor: color,
                color: 'white',
                display: 'grid',
                placeItems: 'center',
                fontWeight: 800,
                fontSize: 20,
                flexShrink: 0,
              }}
            >
              {unit.number}
            </Box>
            <Box>
              <Typography variant="caption" color="text.secondary">
                الوحدة {unit.number}
              </Typography>
              <Typography variant="h6" sx={{ lineHeight: 1.3 }}>
                {unit.title}
              </Typography>
            </Box>
          </Stack>
          <Typography variant="body2" color="text.secondary" sx={{ mb: 1.5, minHeight: 44 }}>
            {unit.description}
          </Typography>
          <Stack direction="row" spacing={1} sx={{ mb: 1.5, flexWrap: 'wrap', gap: 1 }}>
            <Chip size="small" label={`${unit.lessons.length} دروس`} />
            <Chip size="small" label={`${unit.exams.length} اختبارات`} />
            <Chip size="small" label={`${questions} سؤالًا`} />
          </Stack>
          <LinearProgress
            variant="determinate"
            value={(done / unit.exams.length) * 100}
            sx={{ height: 8, borderRadius: 4, mb: 0.5, '& .MuiLinearProgress-bar': { bgcolor: color } }}
          />
          <Typography variant="caption" color="text.secondary">
            أنجزتِ {done} من {unit.exams.length} اختبارات
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

function SubHeading({ icon, title, hint, color }: { icon: ReactNode; title: string; hint: string; color: string }) {
  return (
    <Box sx={{ mb: 2 }}>
      <Stack direction="row" spacing={1} sx={{ alignItems: 'center', color }}>
        {icon}
        <Typography variant="h6" sx={{ color: 'text.primary' }}>
          {title}
        </Typography>
      </Stack>
      <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
        {hint}
      </Typography>
    </Box>
  );
}

function MockPaperCards({ set, label }: { set: MockSet; label: string }) {
  return (
    <Grid container spacing={2}>
      {set.exams.map((pp) => {
        const att = mockAttempts(pp.id);
        const best = att.length ? Math.max(...att.map((a) => Math.round((a.correct / a.total) * 100))) : null;
        return (
          <Grid key={pp.id} size={{ xs: 12, sm: 6, md: 2.4 }}>
            <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column', borderColor: '#c9c3b2', bgcolor: '#fffef9' }}>
              <CardContent sx={{ flexGrow: 1, textAlign: 'center' }}>
                <Typography variant="overline" color="text.secondary">
                  {label}
                </Typography>
                <Typography variant="h6">نموذج ({pp.model})</Typography>
                <Typography variant="body2" color="text.secondary">
                  {pp.questions.length} فقرة · {pp.minutes} دقيقة
                </Typography>
                {best !== null && <Chip size="small" color="success" label={`أفضل نتيجة ${best}%`} sx={{ mt: 1 }} />}
              </CardContent>
              <Box sx={{ p: 2, pt: 0 }}>
                <Button component={RouterLink} to={`/mock/${pp.id}`} variant="contained" fullWidth>
                  {att.length ? 'إعادة' : 'ابدئي'}
                </Button>
              </Box>
            </Card>
          </Grid>
        );
      })}
    </Grid>
  );
}

function RandomExamCard({ mockKey }: { mockKey: string }) {
  const m = mocks.find((x) => x.key === mockKey);
  if (!m) return null;
  const best = bestPercent(m.key);
  const count = Object.values(m.perUnit).reduce((a, b) => a + b, 0);
  return (
    <Card sx={{ display: 'flex', flexDirection: { xs: 'column', sm: 'row' }, alignItems: { sm: 'center' } }}>
      <CardContent sx={{ flexGrow: 1 }}>
        <Typography variant="h6">{m.title}</Typography>
        <Typography variant="body2" color="text.secondary" sx={{ my: 1 }}>
          {m.subtitle}
        </Typography>
        <Stack direction="row" sx={{ flexWrap: 'wrap', gap: 1 }}>
          <Chip size="small" icon={<QuizOutlinedIcon />} label={`${count} سؤالًا`} />
          <Chip size="small" icon={<TimerOutlinedIcon />} label={formatMinutes(m.minutes)} />
          {best !== null && <Chip size="small" color="success" label={`أفضل نتيجة ${best}%`} />}
        </Stack>
      </CardContent>
      <Box sx={{ p: 2, pt: { xs: 0, sm: 2 }, minWidth: { sm: 220 } }}>
        <Button component={RouterLink} to={`/exam/${m.key}`} variant="contained" color="secondary" fullWidth>
          ابدئي الامتحان
        </Button>
      </Box>
    </Card>
  );
}

function SemesterSection({ sem }: { sem: (typeof SEMESTERS)[number] }) {
  const semUnits = units.filter((u) => u.semester === sem.n);
  const set = mockSets.find((x) => x.id === `s${sem.n}`);
  const info = set ? setInfo[set.id] : undefined;
  const examsTotal = semUnits.reduce((n, u) => n + u.exams.length, 0);
  const examsDone = semUnits.reduce((n, u) => n + u.exams.filter((e) => bestPercent(e.id) !== null).length, 0);
  const papersDone = set ? set.exams.filter((e) => mockAttempts(e.id).length > 0).length : 0;
  return (
    <Paper id={`sem-${sem.n}`} variant="outlined" sx={{ overflow: 'hidden', borderColor: sem.color, scrollMarginTop: 80 }}>
      <Box
        sx={{
          bgcolor: sem.color,
          color: 'white',
          px: { xs: 2, md: 3 },
          py: 2,
          display: 'flex',
          flexWrap: 'wrap',
          gap: 1.5,
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <Box>
          <Typography variant="h5">{sem.title}</Typography>
          <Typography sx={{ opacity: 0.9 }}>{sem.units}</Typography>
        </Box>
        <Stack direction="row" sx={{ flexWrap: 'wrap', gap: 1 }}>
          <Chip size="small" label={`اختبارات الوحدات: ${examsDone} من ${examsTotal}`} sx={{ bgcolor: 'rgba(255,255,255,0.18)', color: 'white' }} />
          {set && (
            <Chip size="small" label={`النماذج التجريبية: ${papersDone} من ${set.exams.length}`} sx={{ bgcolor: 'rgba(255,255,255,0.18)', color: 'white' }} />
          )}
        </Stack>
      </Box>

      <Stack spacing={4} sx={{ p: { xs: 2, md: 3 }, bgcolor: sem.tint }}>
        <Box>
          <SubHeading
            icon={<MenuBookOutlinedIcon />}
            color={sem.color}
            title="1. الوحدات واختباراتها"
            hint="ابدئي بكل وحدة: اختبارات قصيرة على نمط الوزارة مع حلّ مفصّل لكل سؤال."
          />
          <Grid container spacing={2}>
            {semUnits.map((u) => (
              <Grid key={u.id} size={{ xs: 12, sm: 6, md: 12 / semUnits.length }}>
                <UnitCard unit={u} color={sem.color} />
              </Grid>
            ))}
          </Grid>
        </Box>

        {set && info && (
          <Box>
            <SubHeading
              icon={<DescriptionOutlinedIcon />}
              color={sem.color}
              title="2. امتحانات تجريبية — محاكاة الامتحان الوزاري"
              hint={`5 نماذج كاملة (30 فقرة · 90 دقيقة) بأسئلة جديدة تغطّي كل أنماط الوزارة في ${info.units}: ورقة أسئلة مطبوعة، وتظليل على ورقة القارئ الضوئي، وتنبيهات المراقب، ثم تحليل للنتيجة حسب الوحدة والمهارة.`}
            />
            <MockPaperCards set={set} label={info.semester} />
          </Box>
        )}

        <Box>
          <SubHeading
            icon={<ShuffleOutlinedIcon />}
            color={sem.color}
            title="3. امتحان عشوائي من بنك الأسئلة"
            hint="تُسحب الأسئلة عشوائيًا من بنك أسئلة وحدات هذا الفصل في كل محاولة، فيختلف الامتحان كل مرة."
          />
          <RandomExamCard mockKey={`mock-s${sem.n}`} />
        </Box>
      </Stack>
    </Paper>
  );
}

export default function Home() {
  const jump = [
    { id: 'sem-1', label: 'الفصل الأول' },
    { id: 'sem-2', label: 'الفصل الثاني' },
    { id: 'full', label: 'الامتحان الشامل' },
  ];
  return (
    <Stack spacing={4}>
      <Paper
        sx={{
          p: { xs: 2.5, md: 4 },
          color: 'white',
          background: 'linear-gradient(135deg, #1d4e89 0%, #2f6fb5 60%, #3f8fd6 100%)',
        }}
      >
        <Typography variant="h4" gutterBottom sx={{ fontSize: { xs: 26, md: 34 } }}>
          تدرّبي على امتحان الرياضيات كأنّه الامتحان الوزاري
        </Typography>
        <Typography sx={{ opacity: 0.92, mb: 2, maxWidth: 760 }}>
          اختبارات لكل وحدة من وحدات كتاب الرياضيات (المستوى المتقدم) للفصلين، بأسئلة اختيار من متعدد على نمط
          الأسئلة الوزارية، مع مؤقّت يحسب زمن كل اختبار حسب حجم أسئلته، وحلّ مفصّل لكل سؤال بعد التسليم.
        </Typography>
        <Stack direction="row" sx={{ flexWrap: 'wrap', gap: 1, mb: 2.5 }}>
          {[
            { icon: <QuizOutlinedIcon />, text: 'الامتحان الوزاري: 50 سؤال اختيار من متعدد' },
            { icon: <TimerOutlinedIcon />, text: 'مدة الامتحان: 3 ساعات' },
            { icon: <AssignmentTurnedInOutlinedIcon />, text: '4 بدائل لكل سؤال (a، b، c، d)' },
          ].map((c) => (
            <Chip
              key={c.text}
              icon={c.icon}
              label={c.text}
              sx={{ bgcolor: 'rgba(255,255,255,0.16)', color: 'white', '& .MuiChip-icon': { color: 'white' } }}
            />
          ))}
        </Stack>
        <Stack direction="row" sx={{ flexWrap: 'wrap', gap: 1 }}>
          {jump.map((j) => (
            <Button key={j.id} onClick={() => scrollTo(j.id)} variant="contained" sx={{ bgcolor: 'white', color: 'primary.main', '&:hover': { bgcolor: '#e8eef8' } }}>
              {j.label}
            </Button>
          ))}
        </Stack>
      </Paper>

      {SEMESTERS.map((sem) => (
        <SemesterSection key={sem.n} sem={sem} />
      ))}

      <Paper id="full" variant="outlined" sx={{ overflow: 'hidden', borderColor: 'secondary.main', scrollMarginTop: 80 }}>
        <Box sx={{ bgcolor: 'secondary.main', color: 'white', px: { xs: 2, md: 3 }, py: 2 }}>
          <Stack direction="row" spacing={1} sx={{ alignItems: 'center' }}>
            <WorkspacePremiumOutlinedIcon />
            <Typography variant="h5">الامتحان الشامل — الفصلان معًا</Typography>
          </Stack>
          <Typography sx={{ opacity: 0.92 }}>الخطوة الأخيرة قبل الامتحان: كل الوحدات بنفس عدد أسئلة الامتحان الوزاري وزمنه.</Typography>
        </Box>
        <Box sx={{ p: { xs: 2, md: 3 }, bgcolor: '#fdf4ec' }}>
          <RandomExamCard mockKey="mock-full" />
        </Box>
      </Paper>
    </Stack>
  );
}
