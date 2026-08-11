import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// GitHub Pages: https://bulkasari.github.io/cocolink/
export default defineConfig({
  plugins: [react()],
  base: '/cocolink/',
})
