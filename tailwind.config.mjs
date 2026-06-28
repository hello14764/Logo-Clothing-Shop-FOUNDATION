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
      boxShadow: {
        soft: '0 4px 24px -4px rgba(10, 37, 64, 0.08)',
        card: '0 8px 32px -8px rgba(10, 37, 64, 0.12)',
        'card-hover': '0 16px 48px -12px rgba(10, 37, 64, 0.16)',
        header: '0 1px 0 rgba(210, 200, 182, 0.6), 0 4px 20px -4px rgba(10, 37, 64, 0.06)',
      },
      backgroundImage: {
        'hero-glow':
          'radial-gradient(ellipse 80% 60% at 70% 20%, rgba(201, 166, 107, 0.12) 0%, transparent 55%), radial-gradient(ellipse 50% 40% at 10% 80%, rgba(210, 200, 182, 0.35) 0%, transparent 50%)',
        'navy-depth':
          'linear-gradient(165deg, #0A2540 0%, #061829 45%, #0A2540 100%)',
        'stone-panel':
          'linear-gradient(145deg, rgba(255,255,255,0.9) 0%, rgba(245,242,237,0.95) 50%, rgba(210,200,182,0.25) 100%)',
      },
      animation: {
        'fade-up': 'fadeUp 0.7s ease-out both',
      },
      keyframes: {
        fadeUp: {
          from: { opacity: '0', transform: 'translateY(12px)' },
          to: { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
};
