import path from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    host: '0.0.0.0',
    allowedHosts: ['reddit-wisdom-app-tunnel-bqejltty.devinapps.com', 'reddit-wisdom-app-tunnel-6ocqytyi.devinapps.com', 'reddit-wisdom-app-tunnel-vrqn89al.devinapps.com']
  },
})

