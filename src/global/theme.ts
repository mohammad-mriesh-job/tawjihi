import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  direction: 'rtl',
  palette: {
    mode: 'light',
    primary: { main: '#1d4e89' },
    secondary: { main: '#e07a1f' },
    success: { main: '#2e7d32' },
    background: { default: '#f4f6fa', paper: '#ffffff' },
  },
  shape: { borderRadius: 12 },
  typography: {
    fontFamily: '"Cairo", "Segoe UI", Tahoma, sans-serif',
    h4: { fontWeight: 800 },
    h5: { fontWeight: 800 },
    h6: { fontWeight: 700 },
    button: { fontWeight: 700 },
  },
  components: {
    MuiButton: { styleOverrides: { root: { textTransform: 'none' } } },
    MuiCard: { defaultProps: { elevation: 0 }, styleOverrides: { root: { border: '1px solid #e2e6ee' } } },
    MuiPaper: { styleOverrides: { rounded: { borderRadius: 14 } } },
  },
});

export default theme;
