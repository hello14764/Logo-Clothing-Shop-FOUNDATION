// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://logoclothingshop.com',
  trailingSlash: 'always',
  integrations: [tailwind({ applyBaseStyles: false })],
});
