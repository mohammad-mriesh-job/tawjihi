import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import LightbulbOutlinedIcon from '@mui/icons-material/LightbulbOutlined';
import FormatListNumberedIcon from '@mui/icons-material/FormatListNumbered';
import BoltOutlinedIcon from '@mui/icons-material/BoltOutlined';
import HighlightOffIcon from '@mui/icons-material/HighlightOff';
import ReportProblemOutlinedIcon from '@mui/icons-material/ReportProblemOutlined';
import type { ReactNode } from 'react';
import MathText from './MathText';
import type { Question } from '../data/types';

function Section({ icon, title, color, bg, children }: {
  icon: ReactNode;
  title: string;
  color: string;
  bg: string;
  children: ReactNode;
}) {
  return (
    <Box sx={{ p: 1.5, borderRadius: 2, bgcolor: bg }}>
      <Stack direction="row" spacing={0.75} sx={{ alignItems: 'center', color, mb: 0.5 }}>
        {icon}
        <Typography variant="subtitle2" sx={{ fontWeight: 800 }}>
          {title}
        </Typography>
      </Stack>
      {children}
    </Box>
  );
}

/** Steps starting with "## " are stage headings; the others are numbered consecutively. */
function numberSteps(steps: string[]) {
  let n = 0;
  return steps.map((text) =>
    text.startsWith('## ') ? { text: text.slice(3), n: 0, heading: true } : { text, n: ++n, heading: false },
  );
}

/**
 * Worked solution for review.
 * `order[pos]` is the original option index shown at position `pos`, so the letters match what the student saw;
 * `chosen` is the original index the student picked (null/undefined if unanswered).
 */
export default function SolutionView({ q, order = [0, 1, 2, 3], letters, chosen }: {
  q: Question;
  order?: number[];
  letters: string[];
  chosen: number | null | undefined;
}) {
  const e = q.explain;
  if (!e) {
    return (
      <Box sx={{ p: 2, borderRadius: 2, bgcolor: 'rgba(29,78,137,0.05)' }}>
        <Typography variant="subtitle2" color="primary" sx={{ mb: 0.5 }}>
          الحل
        </Typography>
        <MathText component="div" sx={{ fontSize: 16 }}>
          {q.solution}
        </MathText>
      </Box>
    );
  }
  const letterOf = (orig: number) => letters[order.indexOf(orig)];
  const myMistake = chosen != null && chosen !== q.answer ? e.wrong[chosen] : null;
  const others = order.filter((orig) => orig !== q.answer && orig !== chosen);
  return (
    <Stack spacing={1.25}>
      {myMistake && chosen != null && (
        <Section icon={<HighlightOffIcon fontSize="small" />} title={`لماذا اختيارك (${letterOf(chosen)}) خطأ؟`} color="#b42318" bg="rgba(211,47,47,0.07)">
          <MathText component="div" sx={{ fontSize: 16 }}>
            {myMistake}
          </MathText>
        </Section>
      )}

      <Section icon={<LightbulbOutlinedIcon fontSize="small" />} title="الفكرة: كيف أعرف الطريقة؟" color="#8a5a00" bg="rgba(245,176,65,0.12)">
        <MathText component="div" sx={{ fontSize: 16 }}>
          {e.idea}
        </MathText>
      </Section>

      <Section icon={<FormatListNumberedIcon fontSize="small" />} title="خطوات الحل" color="primary.main" bg="rgba(29,78,137,0.05)">
        {/* explicit number badges: list markers drift outside the box under the RTL style flip */}
        <Stack spacing={1}>
          {numberSteps(e.steps).map(({ text: st, n, heading }, i) =>
            heading ? (
              <Typography key={i} sx={{ fontWeight: 800, color: 'primary.dark', pt: i ? 1 : 0, borderBottom: 1, borderColor: 'rgba(29,78,137,0.15)' }}>
                {st}
              </Typography>
            ) : (
            <Box key={i} sx={{ display: 'flex', gap: 1, alignItems: 'flex-start' }}>
              <Box
                sx={{
                  flexShrink: 0,
                  width: 24,
                  height: 24,
                  mt: '6px',
                  borderRadius: '50%',
                  bgcolor: 'primary.main',
                  color: 'white',
                  fontSize: 13,
                  fontWeight: 800,
                  display: 'grid',
                  placeItems: 'center',
                }}
              >
                {n}
              </Box>
              <MathText component="div" sx={{ fontSize: 16, minWidth: 0, flexGrow: 1 }}>
                {st}
              </MathText>
            </Box>
            ),
          )}
        </Stack>
        <Typography sx={{ mt: 0.5, fontWeight: 800, color: 'success.main' }}>
          الإجابة الصحيحة: (<span dir="ltr">{letterOf(q.answer)}</span>)
        </Typography>
      </Section>

      {e.quick && (
        <Section icon={<BoltOutlinedIcon fontSize="small" />} title="طريقة أسرع في الامتحان" color="#0f766e" bg="rgba(15,118,110,0.07)">
          <MathText component="div" sx={{ fontSize: 16 }}>
            {e.quick}
          </MathText>
        </Section>
      )}

      {others.length > 0 && (
        <Section icon={<HighlightOffIcon fontSize="small" />} title={myMistake ? 'وباقي البدائل الخاطئة' : 'لماذا البدائل الأخرى خطأ؟'} color="text.secondary" bg="rgba(0,0,0,0.035)">
          <Stack spacing={0.75}>
            {others.map((orig) => (
              <Box key={orig} sx={{ display: 'flex', gap: 1, alignItems: 'baseline' }}>
                <Typography sx={{ fontWeight: 800, flexShrink: 0 }}>
                  (<span dir="ltr">{letterOf(orig)}</span>)
                </Typography>
                <MathText component="div" sx={{ fontSize: 15.5, minWidth: 0 }}>
                  {e.wrong[orig] ?? ''}
                </MathText>
              </Box>
            ))}
          </Stack>
        </Section>
      )}

      {e.tip && (
        <Section icon={<ReportProblemOutlinedIcon fontSize="small" />} title="انتبهي" color="#9a3412" bg="rgba(224,122,31,0.09)">
          <MathText component="div" sx={{ fontSize: 16 }}>
            {e.tip}
          </MathText>
        </Section>
      )}
    </Stack>
  );
}
