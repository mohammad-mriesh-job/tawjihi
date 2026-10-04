import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
// Relative base: the app uses HashRouter, so it works at any path (e.g. GitHub Pages /tawjihi/).
export default defineConfig({
  base: './',
  plugins: [react()],
})
