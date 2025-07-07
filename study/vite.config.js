import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  root: '.',          // memastikan root proyek adalah direktori ini
  build: {
    outDir: 'dist',
  }
})

