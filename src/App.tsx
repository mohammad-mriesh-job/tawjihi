import { Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import UnitPage from './pages/UnitPage';
import ExamPage from './pages/ExamPage';
import MockPage from './pages/MockPage';

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="unit/:unitId" element={<UnitPage />} />
      </Route>
      <Route path="exam/:examKey" element={<ExamPage />} />
      <Route path="mock/:paperId" element={<MockPage />} />
    </Routes>
  );
}
