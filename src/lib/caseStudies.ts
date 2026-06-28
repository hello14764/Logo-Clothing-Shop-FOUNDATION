import cases from '../../content/case-studies/cases.json';
import type { CaseStudy } from '@/types/caseStudy';

export const caseStudies = cases as CaseStudy[];

export function getCaseStudy(slug: string): CaseStudy | undefined {
  return caseStudies.find((c) => c.slug === slug);
}

export function getFeaturedCaseStudies(): CaseStudy[] {
  return caseStudies.filter((c) => c.featured);
}

export function getCaseStudiesByGroup(): Map<string, CaseStudy[]> {
  const map = new Map<string, CaseStudy[]>();
  for (const study of caseStudies) {
    const list = map.get(study.group) ?? [];
    list.push(study);
    map.set(study.group, list);
  }
  return map;
}

export function renderList(items: string | string[]): string[] {
  return Array.isArray(items) ? items : [items];
}
