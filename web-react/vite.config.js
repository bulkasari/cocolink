import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// GitHub Pages: https://bulkasari.github.io/cocolink/
export default defineConfig({
  plugins: [react()],
  base: '/cocolink/',
  server: {
    // 로컬 개발 시 영상 파일을 Python 서버(8080)에서 프록시
    proxy: {
      '/cocolink/Movie': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace('/cocolink', ''),
      }
    }
  }
})
