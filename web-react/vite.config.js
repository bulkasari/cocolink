import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Custom Domain: https://link.metaspacehub.com/ or https://bulkasari.github.io/
export default defineConfig({
  plugins: [react()],
  base: '/',
})

