# Blog Workflow - Draft Iterations

**Topic:** Building a blog publishing workflow with Claude Code

**Status:** DRAFT - Not yet published

**Target Publication:** TBD (potential next post)

---

## Purpose

Document the journey of building this blog workflow and repository with Claude Code, including:
- Converting markdown to WordPress HTML
- Converting markdown to LinkedIn format
- Automating the publishing process
- Managing drafts and published content
- Version control for blog posts

---

## Potential Angles

### Option 1: Technical How-To
"Building a Blog Publishing Workflow with Claude Code"
- Focus: Technical implementation details
- Audience: Developers who want to automate their blog
- Value: Copy the workflow for their own blog

### Option 2: AI Collaboration Story
"How Claude Code Helped Me Build a Better Blogging Workflow"
- Focus: AI pair programming experience
- Audience: Developers curious about AI coding tools
- Value: Real-world example of AI assistance

### Option 3: Meta-Blog Post
"This Post Was Prepared Using the Workflow It Describes"
- Focus: Self-referential demonstration
- Audience: Bloggers looking for efficiency
- Value: Proof by example

---

## Key Components to Cover

### The Problem
- Pasting markdown into WordPress looks ugly
- Pasting markdown into LinkedIn loses formatting
- Multiple manual steps for each post
- Scattered files and drafts
- No clear workflow

### The Solution
- One unified markdown file per post (blog + LinkedIn versions)
- One command to generate all outputs
- Automated formatting for each platform
- Organized structure for drafts and published content
- VS Code integration for easy publishing

### The Tech Stack
- Python scripts for conversion
- Markdown as source format
- Unicode formatting for LinkedIn
- VS Code tasks for automation
- Git for version control

### The Workflow
```bash
./publish.py posts/my-post.md -u https://irjudson.org/url/
```
- Generates WordPress HTML
- Generates LinkedIn text with Unicode bold/italic
- Copies to clipboard
- 5 minutes to publish vs 30+ minutes manually

---

## Files in This Directory

| File | Description | Status |
|------|-------------|--------|
| `2024-11-building-blog-workflow-with-claude.md` | Full technical post | Draft |
| `2024-11-building-blog-workflow-with-claude-linkedin.md` | LinkedIn version | Draft |

---

## Challenges Documented

### Challenge 1: LinkedIn Formatting
- Problem: LinkedIn doesn't support markdown bold/italic
- Iterations:
  1. Plain text (no formatting) ❌
  2. Tried to preserve markdown ❌
  3. Unicode bold/italic ✅
- Solution: Unicode character mapping for bold/italic
- Lesson: Research platform constraints before building

### Challenge 2: Copy/Paste Issues
- Problem: Unicode didn't copy correctly from .txt files
- Iterations:
  1. Output as .txt ❌
  2. Output as .md ✅
  3. Direct clipboard copy ✅
- Solution: Use .md extension and pbcopy command
- Lesson: Test the full workflow, not just generation

### Challenge 3: Too Many Scripts
- Problem: Separate scripts for WordPress, LinkedIn, each iteration
- Solution: One master `publish.py` script
- Lesson: Consolidate early, don't let complexity grow

### Challenge 4: Scattered Files
- Problem: Drafts mixed with published posts
- Solution: Organized directory structure by article
- Lesson: Organization matters from day one

---

## Lessons for Future Posts

### What Worked
- Starting with the problem (ugly copy/paste)
- Iterating based on real testing
- Consolidating multiple tools into one
- Documenting the journey along the way

### What Could Be Better
- Should have researched LinkedIn constraints first
- Could have organized files earlier
- Testing Unicode sooner would have saved time

### Writing Approach
- If publishing this, use Smart Brevity
- Focus on the problem → solution → results
- Include code examples that actually work
- Make it actionable (readers can copy workflow)

---

## Potential Value Adds

If publishing this article, consider adding:

1. **Complete repository template**
   - Everything needed to start a similar workflow
   - MIT licensed for others to use
   - Include all scripts and templates

2. **Video walkthrough**
   - Show the workflow in action
   - Demonstrate the 5-minute publish process
   - Share on YouTube and embed in post

3. **GitHub Actions integration**
   - Auto-generate outputs on commit
   - Validate post format
   - Check for broken links

4. **Additional platform support**
   - Medium export
   - Dev.to export
   - Twitter thread generator

---

## Meta Notes

This directory itself demonstrates the value of organized drafts:
- Easy to find all related work
- Shows iteration history
- Documents learnings for future
- Makes it easy to reference when writing final version

**This is the workflow the post would describe!**

---

## Publication Checklist

When ready to publish:

- [ ] Decide on final angle (technical/story/meta)
- [ ] Apply Smart Brevity (aim for 600-800 words)
- [ ] Add screenshots of workflow in action
- [ ] Test all code examples
- [ ] Create GitHub repository or gist with complete workflow
- [ ] Generate WordPress + LinkedIn versions with `publish.py`
- [ ] Move to `posts/published/` after posting
- [ ] Track engagement and feedback
- [ ] Update README with metrics

---

## Repository Links

- **Blog Repository:** This repo
- **GitHub Profile Tool:** https://github.com/irjudson/github-profile-upgrade (related post)
- **Publishing Documentation:** See `PUBLISHING.md` and `STRUCTURE.md`
