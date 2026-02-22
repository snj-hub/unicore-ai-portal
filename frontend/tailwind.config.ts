import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#0F4C81',
        accent: '#C09435'
      }
    }
  },
  plugins: []
};

export default config;
