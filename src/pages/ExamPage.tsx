import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { Link as RouterLink, useParams } from 'react-router-dom';
import Alert from '@mui/material/Alert';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Chip from '@mui/material/Chip';
import Container from '@mui/material/Container';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import Divider from '@mui/material/Divider';
import LinearProgress from '@mui/material/LinearProgress';
import Paper from '@mui/material/Paper';
import Snackbar from '@mui/material/Snackbar';
import Stack from '@mui/material/Stack';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import FlagIcon from '@mui/icons-material/Flag';
import OutlinedFlagIcon from '@mui/icons-material/OutlinedFlag';
import TimerOutlinedIcon from '@mui/icons-material/TimerOutlined';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import CancelIcon from '@mui/icons-material/Cancel';
import MathText from '../components/MathText';
import SolutionView from '../components/SolutionView';
import { getExam, minutesFor, questionById, units } from '../data';
import type { ExamDescriptor } from '../data';
import type { Question } from '../data/types';
import { shuffle } from '../lib/random';
import { storage } from '../lib/storage';
import type { Result, Session } from '../lib/storage';
import { examMinutes, formatClock, formatMinutes } from '../lib/timing';

// same labels as the ministry question paper (a–d ↔ أ–د on the answer sheet)
const LETTERS = ['a', 'b', 'c', 'd'];
const LEVEL = { easy: 'سهل', medium: 'متوسط', hard: 'صعب' } as const;

const lessonTitle = new Map<string, string>();
for (const u of units) u.lessons.forEach((l) => lessonTitle.set(l.id, l.title));

function questionsOf(s: Session): Question[] {
  return s.questionIds.map((id) => questionById.get(id)!).filter(Boolean);
}

function score(s: Session) {
  const qs = questionsOf(s);
  return qs.reduce((n, q, i) => n + (s.answers[i] === q.answer ? 1 : 0), 0);
}

function Figure({ src }: { src?: string }) {
  if (!src) return null;
  return (
    <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2.5 }}>
      <Box
        component="img"
        src={import.meta.env.BASE_URL + src}
        alt="شكل السؤال"
        sx={{ width: '100%', maxWidth: 440, border: 1, borderColor: 'divider', borderRadius: 2, bgcolor: 'white' }}
      />
    </Box>
  );
}

/* ------------------------------------------------------------------ */

function Intro({ exam, onStart, lastResult, onShowResult }: {
  exam: ExamDescriptor;
  onStart: () => void;
  lastResult: Result | null;
  onShowResult: () => void;
}) {
  const preview = useMemo(() => exam.pickQuestions(), [exam]);
  const minutes = minutesFor(exam, preview);
  return (
    <Container maxWidth="sm" sx={{ py: 4 }}>
      <Button component={RouterLink} to={exam.backTo} startIcon={<ArrowForwardIcon />} sx={{ mb: 2 }}>
        رجوع
      </Button>
      <Paper sx={{ p: { xs: 2.5, sm: 4 } }} variant="outlined">
        <Typography variant="overline" color="text.secondary">
          {exam.subtitle}
        </Typography>
        <Typography variant="h4" gutterBottom>
          {exam.title}
        </Typography>
        <Stack direction="row" sx={{ gap: 1, flexWrap: 'wrap', my: 2 }}>
          <Chip label={`عدد الأسئلة: ${preview.length}`} />
          <Chip icon={<TimerOutlinedIcon />} label={`الزمن: ${formatMinutes(minutes)}`} color="primary" />
        </Stack>
        <Typography variant="h6" sx={{ mt: 2 }}>
          تعليمات الامتحان
        </Typography>
        <Box component="ul" sx={{ pr: 2.5, mt: 1, lineHeight: 2 }}>
          <li>جميع الأسئلة من نوع الاختيار من متعدد، ولكل سؤال إجابة صحيحة واحدة فقط من أربعة بدائل (a, b, c, d) كما في ورقة الأسئلة الوزارية.</li>
          <li>يبدأ المؤقّت عند الضغط على «ابدئي»، ويُسلَّم الامتحان تلقائيًا عند انتهاء الزمن.</li>
          <li>يمكنك التنقّل بين الأسئلة ووضع علامة 🚩 على السؤال للرجوع إليه لاحقًا.</li>
          <li>جهّزي ورقة وقلمًا للحلّ كما في قاعة الامتحان، ويُسمح بالآلة الحاسبة غير القابلة للبرمجة.</li>
          <li>إذا أُغلقت الصفحة، يستمر المؤقّت ويمكنك المتابعة من حيث توقّفتِ.</li>
        </Box>
        <Stack direction={{ xs: 'column', sm: 'row' }} spacing={1.5} sx={{ mt: 3 }}>
          <Button variant="contained" size="large" onClick={onStart} sx={{ flexGrow: 1 }}>
            ابدئي الامتحان
          </Button>
          {lastResult && (
            <Button variant="outlined" size="large" onClick={onShowResult}>
              نتيجة آخر محاولة
            </Button>
          )}
        </Stack>
      </Paper>
    </Container>
  );
}

/* ------------------------------------------------------------------ */

function OptionCard({ index, text, state, onClick }: {
  index: number;
  text: string;
  state: 'idle' | 'selected' | 'correct' | 'wrong' | 'missed';
  onClick?: () => void;
}) {
  const colors = {
    idle: { border: 'divider', bg: 'background.paper', badge: 'grey.200', badgeText: 'text.primary' },
    selected: { border: 'primary.main', bg: 'rgba(29,78,137,0.07)', badge: 'primary.main', badgeText: 'white' },
    correct: { border: 'success.main', bg: 'rgba(46,125,50,0.09)', badge: 'success.main', badgeText: 'white' },
    wrong: { border: 'error.main', bg: 'rgba(211,47,47,0.07)', badge: 'error.main', badgeText: 'white' },
    missed: { border: 'success.main', bg: 'background.paper', badge: 'success.light', badgeText: 'white' },
  }[state];
  return (
    <Box
      onClick={onClick}
      role={onClick ? 'button' : undefined}
      sx={{
        display: 'flex',
        alignItems: 'center',
        gap: 1.5,
        p: 1.25,
        pl: 2,
        border: 2,
        borderColor: colors.border,
        bgcolor: colors.bg,
        borderRadius: 2,
        cursor: onClick ? 'pointer' : 'default',
        transition: 'all .12s',
        '&:hover': onClick ? { borderColor: 'primary.light' } : undefined,
      }}
    >
      <Box
        sx={{
          width: 34,
          height: 34,
          borderRadius: '50%',
          display: 'grid',
          placeItems: 'center',
          fontWeight: 800,
          flexShrink: 0,
          bgcolor: colors.badge,
          color: colors.badgeText,
        }}
      >
        <span dir="ltr">{LETTERS[index]}</span>
      </Box>
      <MathText sx={{ fontSize: 17, flexGrow: 1, minWidth: 0 }}>{text}</MathText>
      {state === 'correct' && <CheckCircleIcon color="success" />}
      {state === 'wrong' && <CancelIcon color="error" />}
    </Box>
  );
}

/* ------------------------------------------------------------------ */

function Running({ exam, session, onChange, onFinish }: {
  exam: ExamDescriptor;
  session: Session;
  onChange: (s: Session) => void;
  onFinish: () => void;
}) {
  const questions = useMemo(() => questionsOf(session), [session]);
  const [now, setNow] = useState(() => Date.now());
  const [confirm, setConfirm] = useState(false);
  const [warn, setWarn] = useState(false);
  const warned = useRef(false);
  const finished = useRef(false);

  const remaining = (session.endsAt - now) / 1000;
  const total = (session.endsAt - session.startedAt) / 1000;

  useEffect(() => {
    const t = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(t);
  }, []);

  useEffect(() => {
    if (remaining <= 0 && !finished.current) {
      finished.current = true;
      onFinish();
    } else if (remaining <= 300 && total > 600 && !warned.current) {
      warned.current = true;
      setWarn(true);
    }
  }, [remaining, total, onFinish]);

  const i = session.current;
  const q = questions[i];
  const order = session.optionOrder[i];
  const answered = session.answers.filter((a) => a !== null).length;

  const go = (n: number) => onChange({ ...session, current: Math.min(questions.length - 1, Math.max(0, n)) });
  const select = (orig: number) => {
    const answers = [...session.answers];
    answers[i] = answers[i] === orig ? null : orig;
    onChange({ ...session, answers });
  };
  const toggleFlag = () => {
    const flags = [...session.flags];
    flags[i] = !flags[i];
    onChange({ ...session, flags });
  };

  const low = remaining <= 300;

  return (
    <Box sx={{ minHeight: '100vh', bgcolor: 'background.default' }}>
      <AppBar position="sticky" color="inherit" elevation={1}>
        <Toolbar sx={{ gap: 1.5 }}>
          <Box sx={{ flexGrow: 1, minWidth: 0 }}>
            <Typography variant="subtitle1" noWrap sx={{ fontWeight: 800 }}>
              {exam.title}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              أجبتِ عن {answered} من {questions.length}
            </Typography>
          </Box>
          <Chip
            icon={<TimerOutlinedIcon />}
            label={formatClock(remaining)}
            color={low ? 'error' : 'primary'}
            variant={low ? 'filled' : 'outlined'}
            sx={{ fontSize: 18, fontWeight: 800, height: 40, px: 1, direction: 'ltr', fontVariantNumeric: 'tabular-nums' }}
          />
          <Button variant="contained" color="secondary" onClick={() => setConfirm(true)}>
            تسليم
          </Button>
        </Toolbar>
        <LinearProgress
          variant="determinate"
          value={Math.max(0, (remaining / total) * 100)}
          color={low ? 'error' : 'primary'}
          sx={{ height: 4 }}
        />
      </AppBar>

      <Container maxWidth="lg" sx={{ py: 3 }}>
        <Box sx={{ display: 'grid', gap: 3, gridTemplateColumns: { xs: 'minmax(0, 1fr)', md: 'minmax(0, 1fr) 260px' }, alignItems: 'start' }}>
          <Paper variant="outlined" sx={{ p: { xs: 2, sm: 3 } }}>
            <Stack direction="row" sx={{ alignItems: 'center', gap: 1, mb: 2, flexWrap: 'wrap' }}>
              <Typography variant="h6">
                السؤال {i + 1} من {questions.length}
              </Typography>
              <Chip size="small" variant="outlined" label={lessonTitle.get(q.lesson) ?? ''} />
              <Box sx={{ flexGrow: 1 }} />
              <Button
                size="small"
                color={session.flags[i] ? 'error' : 'inherit'}
                startIcon={session.flags[i] ? <FlagIcon /> : <OutlinedFlagIcon />}
                onClick={toggleFlag}
              >
                {session.flags[i] ? 'مُعلَّم للمراجعة' : 'علّمي للمراجعة'}
              </Button>
            </Stack>
            <MathText component="div" sx={{ fontSize: 18, mb: 2.5 }}>
              {q.text}
            </MathText>
            <Figure src={q.figure} />
            <Stack spacing={1.25}>
              {order.map((orig, k) => (
                <OptionCard
                  key={orig}
                  index={k}
                  text={q.options[orig]}
                  state={session.answers[i] === orig ? 'selected' : 'idle'}
                  onClick={() => select(orig)}
                />
              ))}
            </Stack>
            <Divider sx={{ my: 2.5 }} />
            <Stack direction="row" sx={{ justifyContent: 'space-between' }}>
              <Button startIcon={<ChevronRightIcon />} disabled={i === 0} onClick={() => go(i - 1)}>
                السابق
              </Button>
              {i < questions.length - 1 ? (
                <Button variant="contained" endIcon={<ChevronLeftIcon />} onClick={() => go(i + 1)}>
                  التالي
                </Button>
              ) : (
                <Button variant="contained" color="secondary" onClick={() => setConfirm(true)}>
                  إنهاء وتسليم
                </Button>
              )}
            </Stack>
          </Paper>

          <Paper variant="outlined" sx={{ p: 2, position: { md: 'sticky' }, top: { md: 96 } }}>
            <Typography variant="subtitle2" sx={{ mb: 1.5 }}>
              خريطة الأسئلة
            </Typography>
            <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(38px, 1fr))', gap: 0.75 }}>
              {questions.map((_, k) => {
                const isAns = session.answers[k] !== null;
                return (
                  <Box
                    key={k}
                    onClick={() => go(k)}
                    sx={{
                      position: 'relative',
                      height: 38,
                      display: 'grid',
                      placeItems: 'center',
                      borderRadius: 1.5,
                      cursor: 'pointer',
                      fontWeight: 700,
                      border: 2,
                      borderColor: k === i ? 'secondary.main' : isAns ? 'primary.main' : 'divider',
                      bgcolor: isAns ? 'primary.main' : 'background.paper',
                      color: isAns ? 'white' : 'text.primary',
                    }}
                  >
                    {k + 1}
                    {session.flags[k] && (
                      <FlagIcon sx={{ position: 'absolute', top: -7, left: -7, fontSize: 16, color: 'error.main' }} />
                    )}
                  </Box>
                );
              })}
            </Box>
            <Stack spacing={0.5} sx={{ mt: 2, fontSize: 12, color: 'text.secondary' }}>
              <span>■ أزرق: تمت الإجابة</span>
              <span>🚩 مُعلَّم للمراجعة</span>
            </Stack>
          </Paper>
        </Box>
      </Container>

      <Dialog open={confirm} onClose={() => setConfirm(false)}>
        <DialogTitle>تسليم الامتحان؟</DialogTitle>
        <DialogContent>
          <Typography>
            أجبتِ عن {answered} من {questions.length} سؤالًا.
            {answered < questions.length && ` بقي ${questions.length - answered} سؤالًا دون إجابة.`}
          </Typography>
          {session.flags.some(Boolean) && (
            <Typography color="error" sx={{ mt: 1 }}>
              لديك {session.flags.filter(Boolean).length} سؤالًا مُعلَّمًا للمراجعة.
            </Typography>
          )}
          <Typography color="text.secondary" sx={{ mt: 1 }}>
            الوقت المتبقي: {formatClock(remaining)}
          </Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setConfirm(false)}>متابعة الحل</Button>
          <Button
            variant="contained"
            color="secondary"
            onClick={() => {
              finished.current = true;
              setConfirm(false);
              onFinish();
            }}
          >
            تسليم
          </Button>
        </DialogActions>
      </Dialog>

      <Snackbar open={warn} autoHideDuration={6000} onClose={() => setWarn(false)} anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}>
        <Alert severity="warning" variant="filled" onClose={() => setWarn(false)}>
          بقي 5 دقائق على انتهاء الامتحان!
        </Alert>
      </Snackbar>
    </Box>
  );
}

/* ------------------------------------------------------------------ */

type Filter = 'all' | 'wrong' | 'flagged';

function Review({ exam, result, onRetry }: { exam: ExamDescriptor; result: Result; onRetry: () => void }) {
  const s = result.session;
  const questions = useMemo(() => questionsOf(s), [s]);
  const correct = score(s);
  const pct = Math.round((correct / questions.length) * 100);
  const used = Math.min(result.finishedAt, s.endsAt) - s.startedAt;
  const allowed = s.endsAt - s.startedAt;
  const [filter, setFilter] = useState<Filter>('all');

  const byLesson = new Map<string, { c: number; t: number }>();
  questions.forEach((q, k) => {
    const r = byLesson.get(q.lesson) ?? { c: 0, t: 0 };
    r.t++;
    if (s.answers[k] === q.answer) r.c++;
    byLesson.set(q.lesson, r);
  });

  const verdict =
    pct >= 85 ? 'ممتاز! مستواك جاهز للامتحان في هذه المادة 🌟' :
    pct >= 70 ? 'جيد جدًا، راجعي الأسئلة الخاطئة وأعيدي المحاولة 💪' :
    pct >= 50 ? 'ناجحة، لكن تحتاجين مراجعة الدروس الضعيفة في الجدول أدناه.' :
    'تحتاجين مراجعة دروس هذه الوحدة ثم إعادة الاختبار — لا تستسلمي!';

  const shown = questions
    .map((q, k) => ({ q, k }))
    .filter(({ q, k }) =>
      filter === 'all' ? true : filter === 'wrong' ? s.answers[k] !== q.answer : s.flags[k],
    );

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Button component={RouterLink} to={exam.backTo} startIcon={<ArrowForwardIcon />} sx={{ mb: 2 }}>
        رجوع
      </Button>
      <Paper variant="outlined" sx={{ p: { xs: 2.5, sm: 4 }, mb: 3, textAlign: 'center' }}>
        <Typography variant="overline" color="text.secondary">
          نتيجة {exam.title}
        </Typography>
        <Typography variant="h2" sx={{ fontWeight: 800, color: pct >= 50 ? 'success.main' : 'error.main' }}>
          {pct}%
        </Typography>
        <Typography variant="h6">
          {correct} من {questions.length} إجابة صحيحة
        </Typography>
        <Typography color="text.secondary" sx={{ mt: 1 }}>
          الوقت المستخدم: {formatClock(used / 1000)} من {formatClock(allowed / 1000)}
        </Typography>
        <Alert severity={pct >= 50 ? 'success' : 'warning'} sx={{ mt: 2, textAlign: 'right' }}>
          {verdict}
        </Alert>
        <Stack direction="row" spacing={1.5} sx={{ justifyContent: 'center', mt: 2 }}>
          <Button variant="contained" onClick={onRetry}>
            إعادة الامتحان
          </Button>
          <Button variant="outlined" component={RouterLink} to={exam.backTo}>
            اختبار آخر
          </Button>
        </Stack>
      </Paper>

      <Paper variant="outlined" sx={{ mb: 3, overflowX: 'auto' }}>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>الدرس</TableCell>
              <TableCell align="center">الصحيح</TableCell>
              <TableCell align="center">النسبة</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {[...byLesson.entries()].map(([id, r]) => {
              const p = Math.round((r.c / r.t) * 100);
              return (
                <TableRow key={id}>
                  <TableCell>{lessonTitle.get(id)}</TableCell>
                  <TableCell align="center">
                    {r.c} من {r.t}
                  </TableCell>
                  <TableCell align="center" sx={{ color: p >= 50 ? 'success.main' : 'error.main', fontWeight: 700 }}>
                    {p}%
                  </TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </Paper>

      <Stack direction="row" sx={{ alignItems: 'center', mb: 2, gap: 2, flexWrap: 'wrap' }}>
        <Typography variant="h5">مراجعة الأسئلة والحلول</Typography>
        <ToggleButtonGroup size="small" exclusive value={filter} onChange={(_, v) => v && setFilter(v)}>
          <ToggleButton value="all">الكل</ToggleButton>
          <ToggleButton value="wrong">الخاطئة وغير المجابة</ToggleButton>
          <ToggleButton value="flagged">المُعلَّمة</ToggleButton>
        </ToggleButtonGroup>
      </Stack>

      <Stack spacing={2}>
        {shown.length === 0 && <Typography color="text.secondary">لا توجد أسئلة هنا.</Typography>}
        {shown.map(({ q, k }) => {
          const chosen = s.answers[k];
          const ok = chosen === q.answer;
          return (
            <Paper key={q.id} variant="outlined" sx={{ p: { xs: 2, sm: 3 }, borderColor: ok ? 'success.light' : 'error.light' }}>
              <Stack direction="row" sx={{ alignItems: 'center', gap: 1, mb: 1.5, flexWrap: 'wrap' }}>
                <Typography variant="subtitle1" sx={{ fontWeight: 800 }}>
                  السؤال {k + 1}
                </Typography>
                <Chip size="small" variant="outlined" label={lessonTitle.get(q.lesson)} />
                <Chip size="small" variant="outlined" label={LEVEL[q.difficulty]} />
                <Box sx={{ flexGrow: 1 }} />
                {ok ? (
                  <Chip size="small" color="success" label="صحيحة" />
                ) : chosen === null ? (
                  <Chip size="small" color="warning" label="لم تُجب" />
                ) : (
                  <Chip size="small" color="error" label="خاطئة" />
                )}
              </Stack>
              <MathText component="div" sx={{ fontSize: 17, mb: 2 }}>
                {q.text}
              </MathText>
              <Figure src={q.figure} />
              <Stack spacing={1}>
                {s.optionOrder[k].map((orig, pos) => (
                  <OptionCard
                    key={orig}
                    index={pos}
                    text={q.options[orig]}
                    state={
                      orig === q.answer ? (chosen === orig ? 'correct' : 'missed') : chosen === orig ? 'wrong' : 'idle'
                    }
                  />
                ))}
              </Stack>
              <Box sx={{ mt: 2 }}>
                <SolutionView q={q} order={s.optionOrder[k]} letters={LETTERS} chosen={chosen} />
              </Box>
            </Paper>
          );
        })}
      </Stack>
    </Container>
  );
}

/* ------------------------------------------------------------------ */

type Phase = 'intro' | 'running' | 'review';

export default function ExamPage() {
  const { examKey = '' } = useParams();
  const exam = useMemo(() => getExam(examKey), [examKey]);
  const [session, setSession] = useState<Session | null>(() => storage.session(examKey));
  const [result, setResult] = useState<Result | null>(() => storage.result(examKey));
  const [phase, setPhase] = useState<Phase>(() => (storage.session(examKey) ? 'running' : 'intro'));

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [phase]);

  const start = () => {
    if (!exam) return;
    const qs = exam.pickQuestions();
    const minutes = exam.fixedMinutes ?? examMinutes(qs);
    const now = Date.now();
    const s: Session = {
      questionIds: qs.map((q) => q.id),
      optionOrder: qs.map(() => shuffle([0, 1, 2, 3])),
      answers: qs.map(() => null),
      flags: qs.map(() => false),
      current: 0,
      startedAt: now,
      endsAt: now + minutes * 60_000,
    };
    storage.saveSession(examKey, s);
    setSession(s);
    setPhase('running');
  };

  const change = (s: Session) => {
    storage.saveSession(examKey, s);
    setSession(s);
  };

  const finish = useCallback(() => {
    const s = storage.session(examKey);
    if (!s) return;
    const r: Result = { session: s, finishedAt: Date.now() };
    const total = s.questionIds.length;
    storage.addAttempt(examKey, {
      date: r.finishedAt,
      correct: score(s),
      total,
      seconds: Math.round((Math.min(r.finishedAt, s.endsAt) - s.startedAt) / 1000),
    });
    storage.saveResult(examKey, r);
    storage.clearSession(examKey);
    setResult(r);
    setSession(null);
    setPhase('review');
  }, [examKey]);

  if (!exam)
    return (
      <Container sx={{ py: 6 }}>
        <Typography>الامتحان غير موجود.</Typography>
        <Button component={RouterLink} to="/">
          الرئيسية
        </Button>
      </Container>
    );

  if (phase === 'running' && session)
    return <Running exam={exam} session={session} onChange={change} onFinish={finish} />;

  if (phase === 'review' && result) return <Review exam={exam} result={result} onRetry={start} />;

  return <Intro exam={exam} onStart={start} lastResult={result} onShowResult={() => setPhase('review')} />;
}

