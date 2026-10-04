import { Link as RouterLink, useParams } from 'react-router-dom';
import Box from '@mui/material/Box';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid';
import Link from '@mui/material/Link';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import MenuBookOutlinedIcon from '@mui/icons-material/MenuBookOutlined';
import TimerOutlinedIcon from '@mui/icons-material/TimerOutlined';
import QuizOutlinedIcon from '@mui/icons-material/QuizOutlined';
import { getUnit } from '../data';
import { bestPercent, storage } from '../lib/storage';
import { examMinutes, formatMinutes } from '../lib/timing';

const LEVEL = { easy: 'سهل', medium: 'متوسط', hard: 'صعب' } as const;

export default function UnitPage() {
  const { unitId = '' } = useParams();
  const unit = getUnit(unitId);
  if (!unit) return <Typography>الوحدة غير موجودة.</Typography>;

  return (
    <Stack spacing={3}>
      <Breadcrumbs>
        <Link component={RouterLink} to="/" underline="hover" color="inherit">
          الرئيسية
        </Link>
        <Typography color="text.primary">الوحدة {unit.number}</Typography>
      </Breadcrumbs>

      <Box>
        <Typography variant="overline" color="text.secondary">
          {unit.semester === 1 ? 'الفصل الأول' : 'الفصل الثاني'} · الوحدة {unit.number}
        </Typography>
        <Typography variant="h4">{unit.title}</Typography>
        <Typography color="text.secondary" sx={{ mt: 1 }}>
          {unit.description}
        </Typography>
      </Box>

      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 4 }}>
          <Paper sx={{ p: 2 }} variant="outlined">
            <Typography variant="h6" sx={{ mb: 1 }}>
              دروس الوحدة
            </Typography>
            <List dense disablePadding>
              {unit.lessons.map((l, i) => (
                <ListItem key={l.id} disableGutters>
                  <ListItemIcon sx={{ minWidth: 36 }}>
                    <MenuBookOutlinedIcon color="primary" fontSize="small" />
                  </ListItemIcon>
                  <ListItemText primary={`الدرس ${i + 1}: ${l.title}`} />
                </ListItem>
              ))}
            </List>
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 8 }}>
          <Stack spacing={2}>
            {unit.exams.map((exam) => {
              const minutes = examMinutes(exam.questions);
              const best = bestPercent(exam.id);
              const attempts = storage.attempts(exam.id).length;
              const inProgress = storage.session(exam.id) !== null;
              const counts = { easy: 0, medium: 0, hard: 0 };
              exam.questions.forEach((q) => counts[q.difficulty]++);
              return (
                <Card key={exam.id}>
                  <CardContent>
                    <Stack
                      direction={{ xs: 'column', sm: 'row' }}
                      spacing={2}
                      sx={{ justifyContent: 'space-between', alignItems: { sm: 'center' } }}
                    >
                      <Box>
                        <Typography variant="h6">{exam.title}</Typography>
                        <Stack direction="row" sx={{ flexWrap: 'wrap', gap: 1, mt: 1 }}>
                          <Chip size="small" icon={<QuizOutlinedIcon />} label={`${exam.questions.length} سؤالًا`} />
                          <Chip size="small" icon={<TimerOutlinedIcon />} label={formatMinutes(minutes)} />
                          {(Object.keys(counts) as (keyof typeof counts)[])
                            .filter((k) => counts[k])
                            .map((k) => (
                              <Chip key={k} size="small" variant="outlined" label={`${LEVEL[k]}: ${counts[k]}`} />
                            ))}
                        </Stack>
                        <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mt: 1 }}>
                          {attempts
                            ? `عدد المحاولات: ${attempts} · أفضل نتيجة: ${best}%`
                            : 'لم تقدّمي هذا الاختبار بعد'}
                        </Typography>
                      </Box>
                      <Button
                        component={RouterLink}
                        to={`/exam/${exam.id}`}
                        variant="contained"
                        color={inProgress ? 'secondary' : 'primary'}
                        sx={{ flexShrink: 0, minWidth: 140 }}
                      >
                        {inProgress ? 'متابعة الاختبار' : attempts ? 'إعادة الاختبار' : 'ابدئي الاختبار'}
                      </Button>
                    </Stack>
                  </CardContent>
                </Card>
              );
            })}
            <Typography variant="body2" color="text.secondary">
              زمن كل اختبار محسوب حسب حجم أسئلته (سهل 2.5 دقيقة، متوسط 3.5 دقيقة، صعب 5 دقائق)، وهو نفس معدّل الامتحان
              الوزاري تقريبًا: 50 سؤالًا في 180 دقيقة.
            </Typography>
          </Stack>
        </Grid>
      </Grid>
    </Stack>
  );
}
