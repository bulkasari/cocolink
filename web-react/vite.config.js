import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Custom Domain: https://link.metaspacehub.com/ or https://bulkasari.github.io/
export default defineConfig({
  plugins: [react()],
  base: '/',
  build: {
    rollupOptions: {
      output: {
        // 빌드될 때마다 파일명 뒤에 고유 해시값을 추가하여 캐시를 무효화함
        entryFileNames: `assets/[name]-[hash].js`,
        chunkFileNames: `assets/[name]-[hash].js`,
        assetFileNames: `assets/[name]-[hash].[ext]`
      }
    }
  }
})


