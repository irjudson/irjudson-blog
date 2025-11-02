# Blog Post Creation Workflow

This workflow documents how Ivan creates blog posts with Claude's help, from initial idea to published post.

**Time investment:** 10-30 minutes from idea to published post

---

## The Process

### 1. Ivan Provides Raw Input

Ivan gives Claude:
- Brain dump, bullet points, or casual description
- The topic and what's interesting about it
- Key points to cover
- Any specific angle or audience

**Format:** Doesn't matter - can be messy notes, stream of consciousness, or structured outline

**Examples:**
- "I just built this GitHub profile toolkit, spent a year analyzing what works..."
- "Fixed this interesting bug in the ranch automation system, here's what happened..."
- "Thinking about how craftsmanship applies to software, some thoughts..."

### 2. Claude Creates Complete Package

Claude produces:

**Blog Post Content:**
- 600-1500 words (depending on topic)
- Clear structure with headers
- Engaging opening and strong closing
- Proper voice (technical but accessible, Ivan's style)

**SEO Metadata:**
- SEO-optimized title
- Meta description (155-160 chars)
- URL slug
- Categories and tags

**LinkedIn Version (if professional content):**
- Condensed version for LinkedIn
- Appropriate hashtags
- Professional framing
- Call to action

**Featured Image Suggestions:**
- Concept for featured image
- HTML template (if custom design)
- Or screenshot/photo recommendations

**Publishing Checklist:**
- All the WordPress steps needed
- Image placement notes
- SEO settings
- LinkedIn checkbox reminder

### 3. Ivan Publishes

Ivan takes the complete package and:
1. Copies blog post content into WordPress
2. Adds his own photos/screenshots where indicated
3. Sets categories, tags, and SEO metadata
4. Uploads featured image
5. Checks "Share to LinkedIn" if appropriate
6. Previews and publishes

**Time:** 5-10 minutes of actual WordPress work

---

## Post Types & Approaches

### Project Logs
Making/building/fixing something concrete

**Structure:**
- What you built and why
- The problem it solves
- How it works
- What you learned

**Example:** GitHub Profile Upgrade Toolkit post

**LinkedIn:** Usually YES (shows execution, shares value)

---

### Technical Deep Dives
How something works, architecture decisions, technical insights

**Structure:**
- Context and problem space
- Technical approach
- Implementation details
- Results and lessons

**LinkedIn:** YES if broadly applicable, MAYBE if very niche

---

### Adventures/Experiences
Travel, events, interesting experiences

**Structure:**
- The experience and what made it interesting
- Details and observations
- Broader insights or lessons
- Personal reflection

**LinkedIn:** Usually NO (unless professional event or clear career insight)

---

### Philosophical Reflections
Thinking about craftsmanship, systems, mental models

**Structure:**
- The idea or observation
- Supporting examples
- Connections to broader patterns
- Implications or conclusions

**LinkedIn:** MAYBE (YES if professional angle, NO if purely personal musing)

---

### How-Tos and Guides
Teaching something specific, sharing a technique

**Structure:**
- What you're teaching and why it matters
- Step-by-step or conceptual walkthrough
- Examples and gotchas
- Resources and next steps

**LinkedIn:** Usually YES (provides value to professional network)

---

### Quick Observations
Short posts (300-500 words) about something noticed or learned

**Structure:**
- The observation
- Why it's interesting
- Quick reflection or implication

**LinkedIn:** MAYBE (depends on professional relevance)

---

## LinkedIn Decision Tree

**Share to LinkedIn if:**
- ✅ Professional insights or career lessons
- ✅ Technical content useful to your network
- ✅ Project showcases with clear value
- ✅ How-tos and practical guides
- ✅ Industry observations or trends

**Don't share to LinkedIn if:**
- ❌ Personal hobbies without professional angle
- ❌ Philosophy without career/professional connection
- ❌ Very short posts (under 400 words)
- ❌ Content targeted at non-professional audience

**Gray area (ask yourself):**
- Craftsmanship posts: YES if tied to professional work, NO if purely personal
- Travel: NO unless professional event or clear career insight
- Ranch life: NO unless technology/automation angle

---

## Content Guidelines

### Voice
- **Technical but accessible** - Explain concepts clearly, avoid unnecessary jargon
- **Direct and honest** - Ivan's style is straightforward, not marketing-y
- **Data-informed** - Back claims with examples, metrics, or experience
- **Practical** - Focus on what works, not theory for theory's sake

### Length
- **Short posts:** 300-500 words (quick observations)
- **Standard posts:** 600-1000 words (most common)
- **Deep dives:** 1000-1500 words (technical or comprehensive)
- **Avoid:** Very short (<300) or very long (>2000) unless really justified

### Structure
- **Opening:** Hook with the interesting part, why this matters
- **Body:** Clear sections with headers, logical flow
- **Closing:** Synthesis, lesson, or call to action
- **Links:** Include relevant links (projects, references, resources)

### SEO
- **Title:** Clear, specific, includes key terms (but not keyword-stuffed)
- **Meta description:** Concise summary with value proposition
- **Headers:** Use H2/H3 for structure, include key terms naturally
- **Links:** Internal links to other posts when relevant

---

## File Organization

### While Writing
- Start in `drafts/` directory
- Name: `YYYY-topic-slug.md`
- Include all metadata at top

### After Publishing
- Move to `posts/` directory
- Keep same filename
- Update main README.md with post link
- Commit to git

### Assets
- **Featured images:** `assets/featured-images/`
- **Screenshots:** `assets/screenshots/`
- **Other images:** `assets/images/`

---

## Quality Checks

Before publishing, verify:

- [ ] **Title** is clear and compelling
- [ ] **Opening** hooks the reader in first paragraph
- [ ] **Structure** flows logically with clear sections
- [ ] **Links** all work and are relevant
- [ ] **Images** are placed where indicated, with alt text
- [ ] **SEO metadata** is complete and accurate
- [ ] **Categories/tags** are appropriate
- [ ] **LinkedIn** decision is correct for content type
- [ ] **Proofread** for typos and clarity

---

## Tools Used

- **Claude (claude.ai or Claude Code):** Content creation, editing, structuring
- **WordPress:** Publishing platform
- **Yoast SEO:** SEO optimization in WordPress
- **Blog2Social:** LinkedIn auto-posting
- **This Git Repo:** Version control and organization

---

## Future Automation Ideas

Possible enhancements to streamline further:

- GitHub Action to auto-generate featured images from HTML templates
- Script to convert markdown to WordPress blocks automatically
- API integration to publish directly from git to WordPress
- Template system for common post types
- Analytics integration to track what performs well

For now, the manual WordPress publishing step is quick enough (5-10 min) that automation isn't critical.

---

## Tips for Working with Claude

**Be specific about:**
- Target audience (developers, general, professional network)
- Desired length
- Tone (technical, casual, professional)
- Whether LinkedIn sharing is appropriate

**Provide:**
- Core points you want to make
- Any data, links, or examples to include
- Special formatting needs (code blocks, lists, etc.)

**Claude will handle:**
- Structure and flow
- Transitions and narrative
- SEO optimization
- Formatting and polish
- Creating complete publishing package

**Iterate if needed:**
- "Make it more technical"
- "Shorten to 800 words"
- "Add a section about X"
- "More casual tone"

The workflow is collaborative - Ivan provides the ideas and expertise, Claude handles the mechanical work of structuring and polishing.
