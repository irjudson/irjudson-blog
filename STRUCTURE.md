# Blog Repository Structure

**Last Updated:** November 4, 2025

This repository contains all blog content, drafts, and publishing tools for irjudson.org.

---

## Directory Structure

```
blog/
├── posts/
│   ├── published/          # Published articles with all generated assets
│   └── legacy/             # Migrated WordPress posts (2014-2025)
├── drafts/
│   ├── {article-name}/     # One directory per article with all iterations
│   ├── github-profile-toolkit/
│   └── blog-workflow/
├── assets/                 # Images, diagrams, media files
├── templates/              # Post templates and style guides
├── workflows/              # Publishing workflow documentation
└── tools/                  # Scripts and automation
```

---

## Content Organization

### Published Articles (`posts/published/`)

**Purpose:** Final published articles with all generated outputs

**Contents per article:**
- `{slug}.md` - Source markdown (unified format with blog + LinkedIn versions)
- `{slug}.wordpress.html` - WordPress HTML output
- `{slug}.linkedin.txt` - LinkedIn formatted text
- `{slug}.linkedin.md` - LinkedIn markdown (if used)
- `{slug}.html` - Other HTML exports (if any)

**Example:**
```
posts/published/
└── 2024-11-preparing-for-opportunity.md
    2024-11-preparing-for-opportunity.wordpress.html
    2024-11-preparing-for-opportunity.linkedin.txt
    2024-11-preparing-for-opportunity.linkedin.md
    2024-11-preparing-for-opportunity.html
```

**Published URLs tracked in post metadata section**

---

### Draft Articles (`drafts/{article-name}/`)

**Purpose:** Work-in-progress articles with all iterations and variations

**Organization:** One directory per article topic

**Contents:**
- All draft versions and iterations
- Early brainstorming versions
- Alternative framings that didn't make the cut
- LinkedIn variations tested

**Example:**
```
drafts/
├── github-profile-toolkit/
│   ├── 2024-11-github-profile-job-search-accelerator.md
│   ├── 2024-11-what-i-learned-optimizing-github-job-search.md
│   ├── 2024-github-profile-upgrade-toolkit.md
│   └── ... (all other iterations)
└── blog-workflow/
    ├── 2024-11-building-blog-workflow-with-claude.md
    └── ... (all iterations)
```

**Why organize this way:**
- Easy to find all work related to one article
- Preserves iteration history
- Shows evolution of ideas
- Makes it easy to reference earlier versions

---

### Legacy Posts (`posts/legacy/`)

**Purpose:** Archived posts migrated from WordPress (2014-2025)

**Contents:**
- 28 posts converted from WordPress XML
- All posts have copyright notices
- Chronological index in README.md

**Topics covered:**
- IoT & embedded systems
- HDInsight & big data
- AllJoyn framework
- Career reflections
- Microsoft experiences

**Not actively maintained** - historical archive only

---

## Publishing Workflow

### Creating a New Article

1. **Start a draft:**
   ```bash
   mkdir drafts/my-article-name
   cp templates/post-template.md drafts/my-article-name/2024-MM-my-article-name.md
   ```

2. **Write and iterate:**
   - Save all iterations in the same directory
   - Use descriptive filenames for different approaches
   - Example: `2024-11-article-name-job-search-angle.md`

3. **When ready to publish:**
   ```bash
   # Generate WordPress + LinkedIn outputs
   ./publish.py drafts/my-article-name/final-version.md -u https://irjudson.org/article-slug/

   # Outputs are generated in same directory
   ```

4. **After publishing:**
   ```bash
   # Move everything to published/
   mv drafts/my-article-name/final-version.* posts/published/

   # Keep drafts for reference or delete
   # (drafts show your thinking process)
   ```

---

## File Naming Conventions

### Dates
- Use ISO format: `YYYY-MM-DD` or `YYYY-MM`
- Example: `2024-11-preparing-for-opportunity.md`

### Slugs
- Lowercase with hyphens
- Match WordPress URL slug
- Keep under 60 characters
- Example: `preparing-for-opportunity`

### Generated Files
- WordPress: `{slug}.wordpress.html`
- LinkedIn: `{slug}.linkedin.txt`
- Other exports: `{slug}.{format}`

---

## Post Template Structure

Every post should use this unified format:

```markdown
# Post Title

**Published:** November 2024
**Categories:** Technology, Professional
**Tags:** tag1, tag2, tag3
**LinkedIn:** YES
**URL:** https://irjudson.org/slug/ (add after publishing)

---

**Copyright © 2024 Ivan Judson. All Rights Reserved.**

---

## SEO Metadata
- **SEO Title:** ...
- **Meta Description:** ...
- **URL Slug:** ...

---

# BLOG POST VERSION

[Full blog content here - Smart Brevity principles]

---

# LINKEDIN VERSION

[Condensed LinkedIn version - even shorter]

---

**Engagement prompt:** "Question for audience?"
```

---

## Tools and Scripts

### Publishing Script
```bash
./publish.py posts/my-post.md -u https://irjudson.org/url/
```
- Generates WordPress HTML
- Generates LinkedIn text with Unicode formatting
- Copies LinkedIn to clipboard (Mac)
- ONE command for everything

### VS Code Integration
- Press `Cmd+Shift+B` in any `.md` file
- Enter blog URL when prompted
- Generates all outputs automatically

### Legacy Tools (Deprecated)
- `convert-to-wordpress.py` - Replaced by `publish.py`
- `convert-to-linkedin.py` - Replaced by `publish.py`
- `convert-to-linkedin-effective.py` - Replaced by `publish.py`
- `convert-to-linkedin-unicode.py` - Replaced by `publish.py`

**Use `publish.py` for everything now**

---

## Asset Management

### Images
- Store in `assets/images/{article-slug}/`
- Use descriptive filenames
- Include source files if edited (PSD, Sketch, etc.)

### Diagrams
- Store in `assets/diagrams/{article-slug}/`
- Include source files (draw.io, mermaid, etc.)

### Screenshots
- Store in `assets/screenshots/{article-slug}/`
- Use descriptive names: `github-profile-before.png`

---

## Version Control

### What to Commit
- ✅ All markdown source files
- ✅ Published assets (images, diagrams)
- ✅ Generated outputs (WordPress HTML, LinkedIn text)
- ✅ Scripts and tools
- ✅ Documentation

### What to .gitignore
- ❌ Temporary files
- ❌ OS files (.DS_Store)
- ❌ Editor files (.vscode/settings.json)
- ❌ Large binary source files (>1MB)

### Commit Messages
- `feat: Add new post about X`
- `draft: GitHub toolkit iteration 3`
- `publish: Preparing for Opportunity`
- `fix: Update WordPress converter`
- `docs: Update publishing workflow`

---

## Workflow Summary

**For Next Post:**

1. Create draft directory: `drafts/article-name/`
2. Write and iterate in that directory
3. When ready: `./publish.py drafts/article-name/final.md -u {URL}`
4. Paste WordPress HTML to WordPress
5. Paste LinkedIn text to LinkedIn (already in clipboard)
6. After publishing: `mv drafts/article-name/final.* posts/published/`
7. Done in 5 minutes!

**Clean, organized, fast.**

---

## Quick Reference

| Task | Command |
|------|---------|
| Create new draft | `mkdir drafts/article-name` |
| Publish article | `./publish.py {file}.md -u {URL}` |
| VS Code publish | `Cmd+Shift+B` |
| Move to published | `mv {file}.* posts/published/` |
| List drafts | `ls -la drafts/*/` |
| List published | `ls -la posts/published/` |

---

## Notes

- **Drafts are valuable** - they show your thinking process and iterations
- **Keep everything organized by article** - makes it easy to find related work
- **Published folder is the source of truth** - what's actually live on the site
- **Legacy posts are archived** - historical reference only, not actively maintained
- **One command to publish** - `publish.py` does everything
