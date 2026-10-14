import { Link as RouterLink, Outlet } from 'react-router-dom';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import FunctionsIcon from '@mui/icons-material/Functions';

export default function Layout() {
  return (
    <Box sx={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <AppBar position="sticky" elevation={0}>
        <Toolbar>
          <Box
            component={RouterLink}
            to="/"
            sx={{ display: 'flex', alignItems: 'center', gap: 1, color: 'inherit', textDecoration: 'none', minWidth: 0 }}
          >
            <FunctionsIcon />
            <Typography variant="h6" component="span" noWrap sx={{ fontSize: { xs: 16, sm: 20 } }}>
              رياضيات التوجيهي — المستوى المتقدم
            </Typography>
          </Box>
          <Box sx={{ flexGrow: 1 }} />
          <Typography variant="body2" sx={{ opacity: 0.85, display: { xs: 'none', sm: 'block' } }}>
            جيل 2008 · حقل العلوم والتكنولوجيا
          </Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg" sx={{ py: { xs: 2, md: 4 }, flexGrow: 1 }}>
        <Outlet />
      </Container>
      <Box component="footer" sx={{ py: 2, textAlign: 'center', color: 'text.secondary', fontSize: 13 }}>
        اختبارات تدريبية على نمط أسئلة الامتحان الوزاري — منهاج الرياضيات المتقدم للصف الثاني عشر
      </Box>
    </Box>
  );
}
