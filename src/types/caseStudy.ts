export interface CaseStudyQuote {
  text: string;
  name: string;
  title: string;
  context?: string;
}

export interface CaseStudy {
  slug: string;
  title: string;
  category: string;
  group: string;
  featured?: boolean;
  summary: string;
  card_teaser: string;
  client: string;
  goal: string;
  challenge: string | string[];
  solution: string | string[];
  result: string | string[];
  takeaway: string;
  quote?: CaseStudyQuote;
  quote_followup?: CaseStudyQuote;
  note?: string;
}
