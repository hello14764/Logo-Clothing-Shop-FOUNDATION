export const site = {
  name: 'Logo Clothing Shop',
  bridge: 'Becoming Stitch & Stone Co.',
  footerBridge: 'Introducing Stitch & Stone Co., our next chapter. Same team, same craft.',
  tagline: 'Corporate gifting and in-house decoration. Birmingham, Michigan.',
  email: 'hello@logoclothingshop.com',
  phoneOffice: '(248) 382-8182',
  phoneCell: '(248) 470-9926',
  phoneOfficeHref: 'tel:+12483828182',
  phoneCellHref: 'tel:+12484709926',
  address: {
    street: '280 N Old Woodward Ave, Suite 100',
    city: 'Birmingham, MI 48009',
  },
  bookingUrl: 'https://meetings.hubspot.com/joe-toma/introductory-call',
  googleReviewsUrl: 'https://www.google.com/search?q=Logo+Clothing+Shop+Birmingham+MI+reviews',
  url: 'https://logoclothingshop.com',
  seoTitleSuffix: 'Soon Stitch & Stone Co.',
} as const;

export type NavItem = { href: string; label: string };

export type NavDropdown = {
  label: string;
  href?: string;
  children: readonly NavItem[];
};

export const navPrimary: readonly NavItem[] = [
  { href: '/corporate-gifting/', label: 'Corporate Gifting' },
] as const;

export const navServices: NavDropdown = {
  label: 'Services',
  href: '/services/',
  children: [
    { href: '/services/embroidery/', label: 'Embroidery' },
    { href: '/services/screen-printing/', label: 'Screen Printing' },
    { href: '/services/web-store-programs/', label: 'Web Store Programs' },
    { href: '/services/promotional-products/', label: 'Promotional Products' },
  ],
} as const;

export const navIndustries: NavDropdown = {
  label: 'Industries',
  href: '/industries/',
  children: [
    { href: '/industries/construction/', label: 'Construction' },
    { href: '/industries/legal-financial/', label: 'Legal & Financial' },
  ],
} as const;

export const navResources: NavDropdown = {
  label: 'Resources',
  children: [
    { href: '/case-studies/', label: 'Case Studies' },
    { href: '/insights/', label: 'Insights' },
  ],
} as const;

export const navDropdowns = [navServices, navIndustries, navResources] as const;

/** @deprecated Use navPrimary + navDropdowns — kept for simple footer lists */
export const navLinks = [
  ...navPrimary,
  { href: '/services/', label: 'Services' },
  { href: '/industries/', label: 'Industries' },
  { href: '/case-studies/', label: 'Case Studies' },
  { href: '/insights/', label: 'Insights' },
  { href: '/how-it-works/', label: 'How It Works' },
] as const;

export const footerExplore = [
  ...navPrimary,
  { href: '/services/', label: 'Services' },
  { href: '/industries/', label: 'Industries' },
  { href: '/case-studies/', label: 'Case Studies' },
  { href: '/insights/', label: 'Insights' },
  { href: '/how-it-works/', label: 'How It Works' },
] as const;

export const servicesList = [
  {
    slug: 'embroidery',
    title: 'Embroidery',
    teaser: 'Precision thread work for polos, jackets, hats, and corporate apparel.',
  },
  {
    slug: 'screen-printing',
    title: 'Screen Printing',
    teaser: 'Bold, durable prints for tees, hoodies, and event apparel at scale.',
  },
  {
    slug: 'web-store-programs',
    title: 'Web Store Programs',
    teaser: 'Branded employee stores for on-demand uniform and apparel ordering.',
  },
  {
    slug: 'promotional-products',
    title: 'Promotional Products',
    teaser: 'Your partner in promo — sourcing, decoration, and project management.',
  },
] as const;

export const industriesList = [
  {
    slug: 'construction',
    title: 'Construction',
    teaser: 'Crew appreciation, safety milestones, and field-ready gifts that last.',
    caseStudySlug: 'northstar-painting',
  },
  {
    slug: 'legal-financial',
    title: 'Legal & Financial',
    teaser: 'Understated client thank-yous and referral gifts that reflect your standards.',
    caseStudySlug: 'ven-johnson-law',
  },
] as const;
