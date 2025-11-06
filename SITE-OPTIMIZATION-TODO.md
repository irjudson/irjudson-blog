# irjudson.org Website Optimization Todo List

**Audit Date:** November 4, 2025
**Site:** https://irjudson.org/

---

## 🔴 CRITICAL ISSUES (Fix ASAP)

### Broken Pages
- [ ] **About page returns 404** - https://irjudson.org/about/
  - Navigation links to it but page doesn't exist
  - Create About page with your bio, experience, current role at Harper

- [ ] **Contact page returns 404** - https://irjudson.org/contact/
  - Navigation links to it but page doesn't exist
  - Add contact form or contact information

### Accessibility Issues
- [ ] **Missing alt text on images**
  - Add descriptive alt text to profile avatar
  - Add alt text to all blog post featured images
  - Check all legacy posts for missing alt text

- [ ] **Color contrast issues**
  - CSS uses `contrast-2` (#65574E) on `base` (#D6D2CE)
  - Test with WCAG contrast checker
  - Update colors to meet WCAG AA minimum (4.5:1 for normal text)

- [ ] **Missing H1 tags**
  - Homepage has no proper H1
  - "Ivan R. Judson" should be H1, not just a link
  - Ensure all pages have proper H1 hierarchy

---

## 🟠 HIGH PRIORITY (Fix This Week)

### SEO Improvements
- [ ] **Fix meta descriptions**
  - Homepage meta is truncated: "Perpetually Learning technology, philosophy, & creative..."
  - Write complete 150-160 character descriptions
  - Add unique meta descriptions to all key pages

- [ ] **Add schema markup**
  - Implement Article schema for blog posts
  - Add Person schema to homepage/about page
  - Verify with Google Structured Data Testing Tool

- [ ] **Internal linking strategy**
  - Link related blog posts to each other
  - Add "Related Posts" section to blog post template
  - Create topic clusters for IoT, career, technology posts

### Content Enhancements
- [ ] **Add screenshots to "Preparing for Opportunity" post**
  - Before/after GitHub profile examples
  - Visual flowchart of the 3-step preparation process
  - Example of optimized profile at each career stage

- [ ] **Expand testimonials with attribution**
  - Add job titles and context to testimonials
  - E.g., "Entry-level data engineer in Seattle"
  - Make success metrics more specific

- [ ] **Add FAQ section to toolkit post**
  - Address common objections
  - Explain technical details (GitHub Actions, Claude Code)
  - Provide troubleshooting guidance

### Navigation & UX
- [ ] **Fix navigation inconsistencies**
  - Blog links go to different URLs (/blog vs /category/news)
  - Standardize on one URL structure
  - Update all internal links

- [ ] **Inconsistent CTA styling**
  - "View Posts" vs "VIEW POSTS" - pick one style
  - Ensure consistent button styling across site

- [ ] **Verify social media links**
  - Test X (Twitter) link functionality
  - Ensure all social links are current
  - Consider adding LinkedIn link prominently

---

## 🟡 MEDIUM PRIORITY (Fix This Month)

### Performance Optimization
- [ ] **Reduce CSS bloat**
  - Remove unused WordPress block styles (~15KB+)
  - Use CSS purge tool to identify unused styles
  - Consider critical CSS inlining

- [ ] **Optimize font loading**
  - Change `font-display: fallback` to `font-display: swap`
  - Reduces layout shift and improves perceived performance
  - Test on slow connections

- [ ] **Consolidate tracking scripts**
  - Dual Google Analytics implementation (MonsterInsights + gtag)
  - Choose one tracking method
  - Reduce JavaScript bloat

- [ ] **Cookie consent cleanup**
  - Multiple consent plugins loaded (wpconsent + Complianz)
  - Choose one consent management solution
  - Avoid conflicts and redundancy

### Mobile Optimization
- [ ] **Test mobile viewport at 320px**
  - Padding uses `var(--wp--preset--spacing--50)` (6.5rem)
  - May cause overflow on small screens
  - Test on actual devices (iPhone SE, small Android)

- [ ] **Review prefetch rules**
  - Overly aggressive prefetch even with "conservative" eagerness
  - May drain bandwidth on mobile
  - Adjust or disable on slow connections

### Content Organization
- [ ] **Add "Related Posts" section**
  - Helps with engagement and SEO
  - Links to similar topics
  - Increases time on site

- [ ] **Create topic landing pages**
  - IoT & Embedded Systems
  - Career Development
  - Microsoft & Cloud Technology
  - Groups related posts for easier navigation

---

## 🟢 LOW PRIORITY (Nice to Have)

### Technical Improvements
- [ ] **Standardize URL trailing slashes**
  - Some URLs have `/`, some don't
  - Pick one convention and redirect
  - Prevents duplicate content issues

- [ ] **Add version strings to theme assets**
  - Theme fonts reference `/twentytwentyfour/assets/fonts/`
  - Add version strings for cache busting
  - Helps with updates and debugging

- [ ] **Optimize images**
  - Convert to WebP format
  - Add responsive image sizes
  - Implement lazy loading

### Content Enhancements
- [ ] **Update profile accuracy**
  - "Over 30 years in technology" - verify this is current
  - Last modified date shows "2025-10-27" - update regularly
  - Keep bio fresh and accurate

- [ ] **Add blog post images**
  - Most posts are text-only
  - Add featured images to improve visual appeal
  - Helps with social media sharing

- [ ] **Enable comments/engagement**
  - Comments section exists but no community response visible
  - Consider enabling discussion
  - Or add "respond on Twitter/LinkedIn" CTAs

### Design Polish
- [ ] **Add social sharing buttons**
  - Make it easy to share posts on LinkedIn, Twitter, etc.
  - Track which posts get shared most
  - Improves reach

- [ ] **Create custom 404 page**
  - Currently using default WordPress 404
  - Add helpful navigation and search
  - Link to popular posts

- [ ] **Add search functionality**
  - Help visitors find old posts
  - Especially useful with 10+ years of content
  - Consider using WordPress native search or Algolia

---

## 📊 TRACKING & ANALYTICS

- [ ] **Set up Core Web Vitals monitoring**
  - Track LCP, FID, CLS scores
  - Use Google PageSpeed Insights
  - Monitor mobile vs desktop performance

- [ ] **Set up broken link monitoring**
  - Use tool like Screaming Frog or Dead Link Checker
  - Check monthly for broken internal/external links
  - Fix as they appear

- [ ] **Review analytics monthly**
  - Which posts get most traffic?
  - Which topics resonate most?
  - Adjust content strategy accordingly

---

## 🎯 QUICK WINS (Do These First!)

If you only have 1 hour, do these:

1. ✅ **Create About page** (20 min)
   - Copy bio from homepage
   - Add current role, experience highlights
   - Link to GitHub, LinkedIn

2. ✅ **Create Contact page** (15 min)
   - Add email or contact form
   - Link to social media
   - Set expectations for response time

3. ✅ **Fix color contrast** (15 min)
   - Use contrast checker: https://webaim.org/resources/contrastchecker/
   - Adjust CSS colors to pass WCAG AA
   - Test with browser accessibility tools

4. ✅ **Add alt text to homepage profile image** (5 min)
   - Something like "Ivan R. Judson, technology leader and software engineer"
   - Improves accessibility immediately

5. ✅ **Fix H1 on homepage** (5 min)
   - Change site title to proper H1 tag
   - Ensures proper semantic structure

---

## 📝 NOTES

**WordPress Theme:** Twenty Twenty-Four
**Current Issues Count:** 34 identified issues
**Estimated Total Time:** ~20-30 hours across all priorities

**Prioritization Strategy:**
1. Fix broken pages (About, Contact) first - these are embarrassing
2. Fix accessibility issues - legal requirement and right thing to do
3. SEO improvements - helps with discoverability
4. Performance optimizations - improves user experience
5. Content enhancements - makes site more valuable

**Tools to Use:**
- WCAG Contrast Checker: https://webaim.org/resources/contrastchecker/
- Google PageSpeed Insights: https://pagespeed.web.dev/
- Structured Data Testing: https://search.google.com/test/rich-results
- Screaming Frog: https://www.screamingfrog.co.uk/seo-spider/
- WordPress plugins: Yoast SEO, Smush (image optimization)
