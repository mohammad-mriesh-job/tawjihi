import { Fragment, useCallback, useEffect, useMemo, useRef, useState } from 'react';
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
import Drawer from '@mui/material/Drawer';
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
import useMediaQuery from '@mui/material/useMediaQuery';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import TimerOutlinedIcon from '@mui/icons-material/TimerOutlined';
import CampaignIcon from '@mui/icons-material/Campaign';
import FactCheckOutlinedIcon from '@mui/icons-material/FactCheckOutlined';
import MathText from '../components/MathText';
import { getPaper, setInfo, setOfPaper, unitOfLesson } from '../data/mocks';
import type { MockPaper, MockQuestion } from '../data/types';
import { raw } from '../lib/storage';
import { mockAttempts, mockKey as key } from '../lib/mockStore';
import type { MockResult, MockSession } from '../lib/mockStore';
import { formatClock } from '../lib/timing';

/* ------------------------------------------------------------------ model */

const PAPER_LETTERS = ['a', 'b', 'c', 'd'];
const SHEET_LETTERS = ['أ', 'ب', 'ج', 'د'];
const ORDINAL = ['الأولى', 'الثانية', 'الثالثة', 'الرابعة', 'الخامسة', 'السادسة', 'السابعة', 'الثامنة', 'التاسعة', 'العاشرة', 'الحادية عشرة', 'الثانية عشرة', 'الثالثة عشرة', 'الرابعة عشرة'];
const ANNOUNCE_AT = [30, 15, 5]; // minutes left

/** items grouped into printed pages (a shared stem stays on the same page as both of its items) */
function paginate(qs: MockQuestion[]): number[][] {
  const weight = (q: MockQuestion) => (q.figure ? 2.4 : 1) + (q.lead ? 0.3 : 0) + (q.options.some((o) => o.length > 60) ? 0.4 : 0);
  const blocks: number[][] = [];
  for (let i = 0; i < qs.length; i++) {
    const size = qs[i].group ?? (qs[i].lead?.startsWith('❖') ? 2 : 1);
    const block = Array.from({ length: Math.min(size, qs.length - i) }, (_, k) => i + k);
    blocks.push(block);
    i += block.length - 1;
  }
  const pages: number[][] = [];
  let cur: number[] = [];
  let w = 0;
  for (const b of blocks) {
    const bw = b.reduce((sum, i) => sum + weight(qs[i]), 0);
    if (cur.length && w + bw > 4.2) {
      pages.push(cur);
      cur = [];
      w = 0;
    }
    cur.push(...b);
    w += bw;
  }
  if (cur.length) pages.push(cur);
  return pages;
}

/* ------------------------------------------------------------------ cover */

function Cover({ paper, pages, onStart, onShowResult, hasResult }: {
  paper: MockPaper;
  pages: number;
  onStart: () => void;
  onShowResult: () => void;
  hasResult: boolean;
}) {
  const attempts = mockAttempts(paper.id);
  const set = setOfPaper(paper.id);
  const info = set ? setInfo[set.id] : undefined;
  const hm = `${Math.floor(paper.minutes / 60)}:${String(paper.minutes % 60).padStart(2, '0')}`;
  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Button component={RouterLink} to="/" startIcon={<ArrowForwardIcon />} sx={{ mb: 2 }}>
        الرئيسية
      </Button>
      <Paper variant="outlined" sx={{ p: { xs: 2, sm: 4 }, borderWidth: 2, borderColor: '#333', borderRadius: 1, bgcolor: '#fffef9' }}>
        <Typography align="center" sx={{ fontWeight: 800, mb: 0.5 }}>
          امتحان تجريبي — محاكاة لامتحان شهادة الدراسة الثانوية العامة
        </Typography>
        <Typography align="center" variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          (للتدريب فقط — ليس صادرًا عن وزارة التربية والتعليم)
        </Typography>
        <Box sx={{ display: 'grid', gridTemplateColumns: { xs: '1fr', sm: '1fr 1fr 1fr' }, gap: 1, border: 1, borderColor: '#333', p: 1.5, mb: 2, fontSize: 15 }}>
          <div><b>المبحث:</b> الرياضيات (المستوى المتقدم)</div>
          <div><b>رقم النموذج:</b> ({paper.model})</div>
          <div><b>مدة الامتحان:</b> <span dir="ltr">{hm}</span></div>
          <div><b>المحتوى:</b> {info ? `${info.semester} (${info.units})` : '—'}</div>
          <div><b>عدد الفقرات:</b> {paper.questions.length}</div>
          <div><b>عدد الصفحات:</b> {pages}</div>
        </Box>
        <Typography sx={{ lineHeight: 2.1, textAlign: 'justify' }}>
          <b style={{ textDecoration: 'underline' }}>ملحوظة مهمة:</b> اختر رمز الإجابة الصحيحة في كل فقرة ممّا يأتي، ثم ظلّل بشكل غامق
          الدائرة التي تشير إلى رمز الإجابة في <b>ورقة القارئ الضوئي</b>، وانتبه عند تظليل إجابتك أنّ رمز الإجابة <b dir="ltr">(a)</b> على
          ورقة الأسئلة يقابله <b>(أ)</b> على ورقة القارئ الضوئي، و <b dir="ltr">(b)</b> يقابله <b>(ب)</b>، و <b dir="ltr">(c)</b> يقابله{' '}
          <b>(ج)</b>، و <b dir="ltr">(d)</b> يقابله <b>(د)</b>، علمًا أنّ عدد الفقرات ({paper.questions.length})، وعدد الصفحات ({pages}).
        </Typography>
        <Box sx={{ mt: 2, p: 2, bgcolor: 'rgba(29,78,137,0.06)', borderRadius: 1 }}>
          <Typography sx={{ fontWeight: 700, mb: 1 }}>قبل أن تبدئي — عيشي جوّ القاعة:</Typography>
          <Box component="ul" sx={{ m: 0, pr: 2.5, lineHeight: 2 }}>
            <li>جهّزي ورقة مسودّة وقلمًا وآلة حاسبة غير مبرمجة، وأغلقي الهاتف والكتاب.</li>
            <li>خصّصي {paper.minutes} دقيقة متواصلة دون مقاطعة، كما في الامتحان الحقيقي.</li>
            <li>الإجابة تكون بالتظليل على ورقة القارئ الضوئي فقط (البدائل في ورقة الأسئلة للقراءة).</li>
            <li>سيُنبّهك «المراقب» عندما يبقى 30 و 15 و 5 دقائق، ويُسلَّم الامتحان تلقائيًّا عند انتهاء الوقت.</li>
            <li>ابدئي بالأسئلة السهلة ولا تتوقّفي طويلًا عند سؤال واحد: المعدّل المناسب 3 دقائق لكل فقرة.</li>
          </Box>
        </Box>
        <Stack direction={{ xs: 'column', sm: 'row' }} spacing={1.5} sx={{ mt: 3 }}>
          <Button variant="contained" size="large" onClick={onStart} sx={{ flexGrow: 1 }}>
            ابدئي الامتحان
          </Button>
          {hasResult && (
            <Button variant="outlined" size="large" onClick={onShowResult}>
              نتيجة آخر محاولة
            </Button>
          )}
        </Stack>
        {attempts.length > 0 && (
          <Typography variant="body2" color="text.secondary" sx={{ mt: 2 }}>
            محاولاتك السابقة:{' '}
            {attempts.map((a) => `${Math.round((a.correct / a.total) * 100)}%`).join(' ، ')}
          </Typography>
        )}
      </Paper>
    </Container>
  );
}

/* ------------------------------------------------------------------ printed paper */

function PrintedItem({ q, n, mode, chosen }: { q: MockQuestion; n: number; mode: 'exam' | 'review'; chosen?: number | null }) {
  return (
    <Box id={`item-${n}`} sx={{ py: 1.5, scrollMarginTop: 90 }}>
      {q.lead && (
        <MathText component="div" sx={{ fontWeight: 700, fontSize: 16.5, mb: 1 }}>
          {q.lead}
        </MathText>
      )}
      <Stack direction="row" spacing={1} sx={{ alignItems: 'flex-start' }}>
        <Typography sx={{ fontWeight: 800, fontSize: 17, minWidth: 30, lineHeight: 2 }}>{n})</Typography>
        <Box sx={{ flexGrow: 1, minWidth: 0 }}>
          <MathText component="div" sx={{ fontSize: 17 }}>
            {q.text}
          </MathText>
          {q.figure && (
            <Box sx={{ display: 'flex', justifyContent: 'center', my: 1 }}>
              <Box component="img" src={import.meta.env.BASE_URL + q.figure} alt="شكل" sx={{ width: '100%', maxWidth: 380 }} />
            </Box>
          )}
          <Stack spacing={0.5} sx={{ mt: 0.5, pr: { xs: 0, sm: 2 } }}>
            {q.options.map((o, k) => {
              const isAns = mode === 'review' && k === q.answer;
              const isWrong = mode === 'review' && chosen === k && k !== q.answer;
              return (
                <Stack
                  key={k}
                  direction="row"
                  spacing={1}
                  sx={{
                    alignItems: 'center',
                    px: 1,
                    borderRadius: 1,
                    bgcolor: isAns ? 'rgba(46,125,50,0.12)' : isWrong ? 'rgba(211,47,47,0.1)' : 'transparent',
                  }}
                >
                  <Typography dir="ltr" sx={{ fontWeight: 700, minWidth: 24, fontSize: 16 }}>
                    {PAPER_LETTERS[k]})
                  </Typography>
                  <MathText sx={{ fontSize: 16.5 }}>{o}</MathText>
                  {isAns && <Chip size="small" color="success" label="الإجابة الصحيحة" sx={{ mr: 'auto' }} />}
                  {isWrong && <Chip size="small" color="error" label="إجابتك" sx={{ mr: 'auto' }} />}
                </Stack>
              );
            })}
          </Stack>
        </Box>
      </Stack>
    </Box>
  );
}

function PrintedPages({ paper, pages, mode, answers, renderAfter }: {
  paper: MockPaper;
  pages: number[][];
  mode: 'exam' | 'review';
  answers?: (number | null)[];
  renderAfter?: (i: number) => React.ReactNode;
}) {
  return (
    <Stack spacing={3}>
      {pages.map((items, p) => (
        <Paper key={p} elevation={2} sx={{ px: { xs: 2, sm: 4 }, py: 2.5, borderRadius: 0.5, bgcolor: '#fffef9', border: '1px solid #d8d4c8' }}>
          <Typography align="center" sx={{ fontWeight: 800, mb: 1, borderBottom: '1px solid #ccc', pb: 1 }}>
            الصفحة {ORDINAL[p] ?? p + 1}/نموذج ({paper.model})
          </Typography>
          {items.map((i) => (
            <Fragment key={i}>
              <PrintedItem q={paper.questions[i]} n={i + 1} mode={mode} chosen={answers?.[i]} />
              {renderAfter?.(i)}
            </Fragment>
          ))}
          <Typography sx={{ mt: 1, fontWeight: 700, color: 'text.secondary', textAlign: p === pages.length - 1 ? 'center' : 'left' }}>
            {p === pages.length - 1 ? '« انتهت الأسئلة »' : `يتبع الصفحة ${ORDINAL[p + 1] ?? p + 2} ....`}
          </Typography>
        </Paper>
      ))}
    </Stack>
  );
}

/* ------------------------------------------------------------------ answer sheet */

function AnswerSheet({ paper, answers, onPick, onJump }: {
  paper: MockPaper;
  answers: (number | null)[];
  onPick: (i: number, k: number) => void;
  onJump: (i: number) => void;
}) {
  return (
    <Box>
      <Typography sx={{ fontWeight: 800, textAlign: 'center', mb: 0.5 }}>ورقة القارئ الضوئي</Typography>
      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', textAlign: 'center', mb: 1.5 }}>
        نموذج ({paper.model}) · ظلّلي دائرة واحدة لكل فقرة · اضغطي الدائرة المظلّلة لمسحها
      </Typography>
      <Stack direction="row" sx={{ px: 1, mb: 0.5, color: 'text.secondary', fontSize: 12 }}>
        <Box sx={{ width: 34 }} />
        {SHEET_LETTERS.map((l) => (
          <Box key={l} sx={{ width: 34, textAlign: 'center', fontWeight: 700 }}>
            {l}
          </Box>
        ))}
      </Stack>
      <Stack spacing={0.4}>
        {paper.questions.map((_, i) => (
          <Stack
            key={i}
            direction="row"
            sx={{ alignItems: 'center', px: 1, py: 0.2, borderRadius: 1, bgcolor: i % 5 === 4 ? 'rgba(0,0,0,0.03)' : 'transparent' }}
          >
            <Box
              onClick={() => onJump(i)}
              sx={{ width: 34, fontWeight: 800, fontSize: 14, cursor: 'pointer', color: answers[i] === null ? 'text.primary' : 'primary.main' }}
              title="انتقلي إلى الفقرة"
            >
              {i + 1}
            </Box>
            {SHEET_LETTERS.map((l, k) => {
              const on = answers[i] === k;
              return (
                <Box key={k} sx={{ width: 34, display: 'grid', placeItems: 'center' }}>
                  <Box
                    role="button"
                    aria-label={`الفقرة ${i + 1} الخيار ${l}`}
                    onClick={() => onPick(i, k)}
                    sx={{
                      width: 24,
                      height: 24,
                      borderRadius: '50%',
                      border: '1.5px solid #444',
                      display: 'grid',
                      placeItems: 'center',
                      fontSize: 11,
                      fontWeight: 700,
                      cursor: 'pointer',
                      bgcolor: on ? '#111' : 'white',
                      color: on ? '#111' : '#666',
                      transition: 'background .1s',
                      '&:hover': { borderColor: 'primary.main' },
                    }}
                  >
                    {on ? '' : l}
                  </Box>
                </Box>
              );
            })}
          </Stack>
        ))}
      </Stack>
    </Box>
  );
}

/* ------------------------------------------------------------------ running exam */

function Running({ paper, pages, session, onChange, onFinish }: {
  paper: MockPaper;
  pages: number[][];
  session: MockSession;
  onChange: (s: MockSession) => void;
  onFinish: () => void;
}) {
  const [now, setNow] = useState(() => Date.now());
  const [confirm, setConfirm] = useState(false);
  const [sheetOpen, setSheetOpen] = useState(false);
  const [announce, setAnnounce] = useState<string | null>(null);
  const finished = useRef(false);
  const wide = useMediaQuery('(min-width:1000px)');
  const remaining = (session.endsAt - now) / 1000;
  const total = (session.endsAt - session.startedAt) / 1000;
  const answered = session.answers.filter((a) => a !== null).length;

  // latest props for the 1-second tick (timer, invigilator announcements, auto-submit)
  const latest = useRef({ session, onChange, onFinish });
  useEffect(() => {
    latest.current = { session, onChange, onFinish };
  });
  useEffect(() => {
    const tick = () => {
      const t0 = Date.now();
      setNow(t0);
      const { session: s, onChange: change, onFinish: finish } = latest.current;
      const left = (s.endsAt - t0) / 1000;
      const span = (s.endsAt - s.startedAt) / 1000;
      if (left <= 0) {
        if (!finished.current) {
          finished.current = true;
          finish();
        }
        return;
      }
      const mins = ANNOUNCE_AT.find((m) => left <= m * 60 && !s.announced.includes(m) && span > m * 60);
      if (mins) {
        setAnnounce(`بقي ${mins} دقيقة على انتهاء وقت الامتحان. تأكّدي من تظليل إجاباتك على ورقة القارئ الضوئي.`);
        change({ ...s, announced: [...s.announced, ...ANNOUNCE_AT.filter((m) => left <= m * 60)] });
      }
    };
    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []);

  const pick = (i: number, k: number) => {
    const answers = [...session.answers];
    const answeredAt = [...session.answeredAt];
    answers[i] = answers[i] === k ? null : k;
    answeredAt[i] = answers[i] === null ? null : Date.now();
    onChange({ ...session, answers, answeredAt });
  };
  const jump = (i: number) => {
    document.getElementById(`item-${i + 1}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    setSheetOpen(false);
  };

  const low = remaining <= 300;
  const sheet = <AnswerSheet paper={paper} answers={session.answers} onPick={pick} onJump={jump} />;

  return (
    <Box sx={{ minHeight: '100vh', bgcolor: '#e9e7e1' }}>
      <AppBar position="sticky" color="inherit" elevation={1}>
        <Toolbar sx={{ gap: 1.5 }}>
          <Box sx={{ flexGrow: 1, minWidth: 0 }}>
            <Typography variant="subtitle1" noWrap sx={{ fontWeight: 800 }}>
              {wide ? `امتحان تجريبي — نموذج (${paper.model})` : `نموذج (${paper.model})`}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              ظلّلتِ {answered} من {paper.questions.length}
            </Typography>
          </Box>
          <Chip
            icon={<TimerOutlinedIcon />}
            label={formatClock(remaining)}
            color={low ? 'error' : 'primary'}
            variant={low ? 'filled' : 'outlined'}
            sx={{ fontSize: 18, fontWeight: 800, height: 40, px: 1, direction: 'ltr', fontVariantNumeric: 'tabular-nums' }}
          />
          {!wide && (
            <Button variant="outlined" size="small" startIcon={<FactCheckOutlinedIcon />} onClick={() => setSheetOpen(true)} sx={{ whiteSpace: 'nowrap', flexShrink: 0 }}>
              ورقة الإجابة
            </Button>
          )}
          <Button variant="contained" color="secondary" onClick={() => setConfirm(true)}>
            تسليم
          </Button>
        </Toolbar>
        <LinearProgress variant="determinate" value={Math.max(0, (remaining / total) * 100)} color={low ? 'error' : 'primary'} sx={{ height: 4 }} />
      </AppBar>

      <Container maxWidth="lg" sx={{ py: 3 }}>
        <Box sx={{ display: 'grid', gap: 3, gridTemplateColumns: wide ? 'minmax(0,1fr) 230px' : 'minmax(0,1fr)', alignItems: 'start' }}>
          <PrintedPages paper={paper} pages={pages} mode="exam" />
          {wide && (
            <Paper variant="outlined" sx={{ p: 1.5, position: 'sticky', top: 88, maxHeight: 'calc(100vh - 110px)', overflowY: 'auto', bgcolor: '#fcfbf5' }}>
              {sheet}
            </Paper>
          )}
        </Box>
      </Container>

      <Drawer anchor="bottom" open={sheetOpen} onClose={() => setSheetOpen(false)} slotProps={{ paper: { sx: { maxHeight: '80vh', p: 2, bgcolor: '#fcfbf5' } } }}>
        {sheet}
      </Drawer>

      <Dialog open={confirm} onClose={() => setConfirm(false)}>
        <DialogTitle>تسليم ورقة الإجابة؟</DialogTitle>
        <DialogContent>
          <Typography>
            ظلّلتِ {answered} من {paper.questions.length} فقرة.
            {answered < paper.questions.length && ` بقي ${paper.questions.length - answered} فقرة دون تظليل.`}
          </Typography>
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

      <Snackbar open={!!announce} onClose={() => setAnnounce(null)} autoHideDuration={9000} anchorOrigin={{ vertical: 'top', horizontal: 'center' }}>
        <Alert icon={<CampaignIcon />} severity="warning" variant="filled" onClose={() => setAnnounce(null)} sx={{ fontSize: 16 }}>
          <b>المراقب:</b> {announce}
        </Alert>
      </Snackbar>
    </Box>
  );
}

/* ------------------------------------------------------------------ results */

type Filter = 'all' | 'wrong';

function Results({ paper, pages, result, onRetry }: { paper: MockPaper; pages: number[][]; result: MockResult; onRetry: () => void }) {
  const s = result.session;
  const qs = paper.questions;
  const correct = qs.filter((q, i) => s.answers[i] === q.answer).length;
  const blank = s.answers.filter((a) => a === null).length;
  const pct = Math.round((correct / qs.length) * 100);
  const used = (Math.min(result.finishedAt, s.endsAt) - s.startedAt) / 1000;
  const [filter, setFilter] = useState<Filter>('all');

  const byUnit = new Map<string, { title: string; unitId: string; c: number; t: number }>();
  const bySkill = new Map<string, { c: number; t: number; unitId: string }>();
  qs.forEach((q, i) => {
    const u = unitOfLesson(q.lesson);
    const k = u?.id ?? '?';
    const ru = byUnit.get(k) ?? { title: u ? `الوحدة ${u.number}: ${u.title}` : k, unitId: k, c: 0, t: 0 };
    const rs = bySkill.get(q.tag) ?? { c: 0, t: 0, unitId: k };
    ru.t++;
    rs.t++;
    if (s.answers[i] === q.answer) {
      ru.c++;
      rs.c++;
    }
    byUnit.set(k, ru);
    bySkill.set(q.tag, rs);
  });
  const skills = [...bySkill.entries()].sort((a, b) => a[1].c / a[1].t - b[1].c / b[1].t);
  const weak = skills.filter(([, r]) => r.c / r.t < 0.5);

  // pace: how many items were shaded by the half-way point
  const half = s.startedAt + (s.endsAt - s.startedAt) / 2;
  const byHalf = s.answeredAt.filter((t) => t !== null && t <= half).length;

  const verdict =
    pct >= 85 ? 'ممتاز! أنتِ جاهزة لهذا المستوى من الأسئلة 🌟' :
    pct >= 70 ? 'جيد جدًا — راجعي المهارات الضعيفة في الجدول وأعيدي المحاولة بعد يومين.' :
    pct >= 50 ? 'ناجحة — لكن ركّزي على المهارات المذكورة أدناه قبل النموذج التالي.' :
    'لا تقلقي — هذا هو هدف التجريبي. راجعي الحلول والمهارات الضعيفة ثم أعيدي.';

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Button component={RouterLink} to="/" startIcon={<ArrowForwardIcon />} sx={{ mb: 2 }}>
        الرئيسية
      </Button>
      <Paper variant="outlined" sx={{ p: { xs: 2.5, sm: 4 }, mb: 3, textAlign: 'center' }}>
        <Typography variant="overline" color="text.secondary">
          نتيجة الامتحان التجريبي — نموذج ({paper.model})
        </Typography>
        <Typography variant="h2" sx={{ fontWeight: 800, color: pct >= 50 ? 'success.main' : 'error.main' }}>
          {pct}%
        </Typography>
        <Typography variant="h6">
          {correct} من {qs.length} فقرة صحيحة · العلامة المكافئة {pct} من 100
        </Typography>
        <Stack direction="row" sx={{ justifyContent: 'center', flexWrap: 'wrap', gap: 1, mt: 1.5 }}>
          <Chip label={`الوقت المستخدم: ${formatClock(used)}`} />
          <Chip label={`فقرات متروكة: ${blank}`} color={blank ? 'warning' : 'default'} />
          <Chip label={`ظلّلتِ ${byHalf} فقرة في النصف الأول من الوقت`} />
        </Stack>
        <Alert severity={pct >= 50 ? 'success' : 'warning'} sx={{ mt: 2, textAlign: 'right' }}>
          {verdict}
        </Alert>
        <Stack direction="row" spacing={1.5} sx={{ justifyContent: 'center', mt: 2 }}>
          <Button variant="contained" onClick={onRetry}>
            إعادة النموذج
          </Button>
          <Button variant="outlined" component={RouterLink} to="/">
            نموذج آخر
          </Button>
        </Stack>
      </Paper>

      <Paper variant="outlined" sx={{ mb: 3, overflowX: 'auto' }}>
        <Typography sx={{ fontWeight: 800, p: 2, pb: 0 }}>حسب الوحدة</Typography>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>الوحدة</TableCell>
              <TableCell align="center">الصحيح</TableCell>
              <TableCell align="center">النسبة</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {[...byUnit.values()].map((r) => {
              const p = Math.round((r.c / r.t) * 100);
              return (
                <TableRow key={r.unitId}>
                  <TableCell>{r.title}</TableCell>
                  <TableCell align="center">{r.c} من {r.t}</TableCell>
                  <TableCell align="center" sx={{ fontWeight: 700, color: p >= 50 ? 'success.main' : 'error.main' }}>{p}%</TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </Paper>

      <Paper variant="outlined" sx={{ mb: 3, overflowX: 'auto' }}>
        <Typography sx={{ fontWeight: 800, p: 2, pb: 0 }}>حسب المهارة (الأضعف أولًا)</Typography>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>المهارة</TableCell>
              <TableCell align="center">الصحيح</TableCell>
              <TableCell align="center">مراجعة</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {skills.map(([name, r]) => {
              const p = r.c / r.t;
              return (
                <TableRow key={name}>
                  <TableCell sx={{ color: p < 0.5 ? 'error.main' : undefined, fontWeight: p < 0.5 ? 700 : 400 }}>{name}</TableCell>
                  <TableCell align="center">{r.c} من {r.t}</TableCell>
                  <TableCell align="center">
                    {p < 1 ? (
                      <Button size="small" component={RouterLink} to={`/unit/${r.unitId}`}>
                        اختبارات الوحدة
                      </Button>
                    ) : (
                      '✔'
                    )}
                  </TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
        {weak.length > 0 && (
          <Alert severity="info" sx={{ m: 2 }}>
            ركّزي في مراجعتك على: {weak.map(([n]) => n).join('، ')}.
          </Alert>
        )}
      </Paper>

      <Stack direction="row" sx={{ alignItems: 'center', mb: 2, gap: 2, flexWrap: 'wrap' }}>
        <Typography variant="h5">ورقة الأسئلة مع الحلول</Typography>
        <ToggleButtonGroup size="small" exclusive value={filter} onChange={(_, v) => v && setFilter(v)}>
          <ToggleButton value="all">كل الفقرات</ToggleButton>
          <ToggleButton value="wrong">الخاطئة والمتروكة فقط</ToggleButton>
        </ToggleButtonGroup>
      </Stack>

      {filter === 'all' ? (
        <PrintedPages
          paper={paper}
          pages={pages}
          mode="review"
          answers={s.answers}
          renderAfter={(i) => <SolutionBox q={qs[i]} chosen={s.answers[i]} />}
        />
      ) : (
        <Stack spacing={2}>
          {qs.map((q, i) =>
            s.answers[i] === q.answer ? null : (
              <Paper key={q.id} sx={{ px: { xs: 2, sm: 4 }, py: 1, bgcolor: '#fffef9', border: '1px solid #d8d4c8' }}>
                <PrintedItem q={q} n={i + 1} mode="review" chosen={s.answers[i]} />
                <SolutionBox q={q} chosen={s.answers[i]} />
              </Paper>
            ),
          )}
          {qs.every((q, i) => s.answers[i] === q.answer) && <Typography>لا توجد إجابات خاطئة 🎉</Typography>}
        </Stack>
      )}
    </Container>
  );
}

function SolutionBox({ q, chosen }: { q: MockQuestion; chosen: number | null | undefined }) {
  const ok = chosen === q.answer;
  return (
    <Box sx={{ mb: 2, mr: { xs: 0, sm: 5 }, p: 1.5, borderRadius: 1, bgcolor: ok ? 'rgba(46,125,50,0.06)' : 'rgba(29,78,137,0.06)' }}>
      <Stack direction="row" sx={{ gap: 1, flexWrap: 'wrap', mb: 0.5, alignItems: 'center' }}>
        <Chip size="small" color={ok ? 'success' : chosen == null ? 'warning' : 'error'} label={ok ? 'صحيحة' : chosen == null ? 'متروكة' : `ظلّلتِ (${SHEET_LETTERS[chosen]})`} />
        <Chip size="small" variant="outlined" label={`الصحيح: (${SHEET_LETTERS[q.answer]}) ↔ ${PAPER_LETTERS[q.answer]})`} />
        {q.pattern && <Chip size="small" variant="outlined" label={q.pattern} />}
      </Stack>
      <MathText component="div" sx={{ fontSize: 15.5 }}>
        {q.solution}
      </MathText>
    </Box>
  );
}

/* ------------------------------------------------------------------ page */

type Phase = 'cover' | 'running' | 'review';

export default function MockPage() {
  const { paperId = '' } = useParams();
  const paper = useMemo(() => getPaper(paperId), [paperId]);
  const pages = useMemo(() => (paper ? paginate(paper.questions) : []), [paper]);
  const [session, setSession] = useState<MockSession | null>(() => raw.get<MockSession>(key.session(paperId)));
  const [result, setResult] = useState<MockResult | null>(() => raw.get<MockResult>(key.result(paperId)));
  const [phase, setPhase] = useState<Phase>(() => (raw.get(key.session(paperId)) ? 'running' : 'cover'));

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [phase]);

  const start = () => {
    if (!paper) return;
    const now = Date.now();
    const s: MockSession = {
      startedAt: now,
      endsAt: now + paper.minutes * 60_000,
      answers: paper.questions.map(() => null),
      answeredAt: paper.questions.map(() => null),
      announced: [],
    };
    raw.set(key.session(paperId), s);
    setSession(s);
    setPhase('running');
  };

  const change = useCallback(
    (s: MockSession) => {
      raw.set(key.session(paperId), s);
      setSession(s);
    },
    [paperId],
  );

  const finish = useCallback(() => {
    const s = raw.get<MockSession>(key.session(paperId));
    if (!s || !paper) return;
    const r: MockResult = { session: s, finishedAt: Date.now() };
    const correct = paper.questions.filter((q, i) => s.answers[i] === q.answer).length;
    raw.set(key.attempts(paperId), [
      ...mockAttempts(paperId),
      { date: r.finishedAt, correct, total: paper.questions.length, seconds: Math.round((Math.min(r.finishedAt, s.endsAt) - s.startedAt) / 1000) },
    ]);
    raw.set(key.result(paperId), r);
    raw.del(key.session(paperId));
    setResult(r);
    setSession(null);
    setPhase('review');
  }, [paperId, paper]);

  if (!paper)
    return (
      <Container sx={{ py: 6 }}>
        <Typography>النموذج غير موجود.</Typography>
        <Button component={RouterLink} to="/">الرئيسية</Button>
      </Container>
    );

  if (phase === 'running' && session) return <Running paper={paper} pages={pages} session={session} onChange={change} onFinish={finish} />;
  if (phase === 'review' && result) return <Results paper={paper} pages={pages} result={result} onRetry={start} />;
  return <Cover paper={paper} pages={pages.length} onStart={start} onShowResult={() => setPhase('review')} hasResult={!!result} />;
}
