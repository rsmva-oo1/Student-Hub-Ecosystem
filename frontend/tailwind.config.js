export default {
 
  darkMode: 'class', 

  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}", 
  ],
  theme: {
    extend: {
      colors: {
        slate: {
          850: '#1e293b', 
        }
      }
    },
  },
  plugins: [],
}
