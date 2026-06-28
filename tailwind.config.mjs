/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        navy: {
          DEFAULT: '#0A2540',
          dark: '#061829',
          light: '#14365A',
        },
        stone: {
          DEFAULT: '#D2C8B6',
          dark: '#B8AA94',
        },
        gold: {
          DEFAULT: '#C9A66B',
          light: '#D9BC8A',
          dark: '#A8884F',
        },
        'warm-gray': '#F5F2ED',
        ink: '#2A2724',
        muted: '#7A7268',
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        body: ['"DM Sans"', 'system-ui', 'sans-serif'],
      },
      maxWidth: {
        content: '72rem',
      },
    },
  },
  plugins: [],
};
