# START HERE - Blog Repository Guide

Welcome to your blog repository for irjudson.org!

This repository contains everything you need to create, manage, and publish blog posts efficiently.

---

## What's in This Repository

### 📝 **Current Post Ready to Publish**

Your first blog post is ready to go:
- **Post:** `posts/2024-github-profile-upgrade-toolkit.md`
- **Publishing instructions:** `PUBLISHING-GUIDE.md` ← **Start here to publish!**

Estimated time to publish: ~25 minutes

---

## Repository Structure

```
blog/
├── posts/              # Published blog posts
├── drafts/             # Work-in-progress posts
├── assets/             # Images and media
│   ├── featured-images/
│   └── screenshots/
├── workflows/          # Documentation for the process
│   ├── blog-post-workflow.md
│   └── wordpress-publishing.md
└── templates/          # Templates and prompts
    ├── blog-post-template.md
    ├── claude-prompts.md
    └── quick-reference.md
```

---

## Quick Start Guides

### To Publish Your First Post
→ **Read:** `PUBLISHING-GUIDE.md`

This walks you through publishing the GitHub Profile Toolkit post step-by-step.

### To Create a New Post
→ **Use:** `templates/claude-prompts.md`

Pick a prompt template, fill in your ideas, give to Claude, get complete blog post package.

### Daily Reference
→ **Use:** `templates/quick-reference.md`

Quick lookup for WordPress steps, post types, SEO checklist, etc.

### Understanding the Workflow
→ **Read:** `workflows/blog-post-workflow.md`

Complete documentation of how you work with Claude to create posts.

---

## Your Workflow (The 10-30 Minute Process)

1. **Give Claude your ideas** (use a prompt from `templates/claude-prompts.md`)
2. **Claude creates complete package:**
   - Polished blog post
   - SEO metadata
   - LinkedIn version (if appropriate)
   - Featured image concept
   - Publishing checklist
3. **You publish to WordPress** (follow `workflows/wordpress-publishing.md`)
4. **Archive in this repo** (move from drafts/ to posts/)

---

## Site Information

- **Domain:** irjudson.org
- **Platform:** WordPress on SiteGround
- **Admin:** https://irjudson.org/wp-admin
- **Theme:** Twenty Twenty-Four

### Key Plugins
- Yoast SEO (SEO optimization)
- Blog2Social (LinkedIn integration)
- Really Simple SSL (HTTPS)

---

## Next Steps

### Immediate
1. **Publish the GitHub Profile post** using `PUBLISHING-GUIDE.md`
2. **Initialize git repository** (if you want version control)
   ```bash
   git init
   git add .
   git commit -m "Initial blog repository setup"
   ```

### Soon
3. **Try creating a new post** using the workflow
4. **Customize templates** to match your preferences
5. **Set up GitHub repo** (optional, for backup and version control)

### Future Ideas
- GitHub Action to auto-generate featured images
- Script to convert markdown to WordPress API format
- Analytics integration
- Template variations for common post types

---

## Common Questions

### Where do I start writing a new post?
Start in the `drafts/` folder. Use `templates/blog-post-template.md` as a starting point, or just create a new markdown file.

### How do I work with Claude to create content?
Use the prompts in `templates/claude-prompts.md`. Pick the one that matches your post type, customize it with your ideas, and Claude will create the complete package.

### What if I want to edit an existing post?
Just tell Claude: "I have this draft [paste content]. Please [what you need]." Claude can refine, expand, shorten, or adjust tone.

### Do I need to learn markdown?
Not really - Claude handles the formatting. Just give your ideas in whatever format is easy for you.

### How do I know if a post should go to LinkedIn?
See the decision tree in `templates/quick-reference.md`. Generally: professional content YES, personal content NO.

### Can I automate the WordPress publishing?
Possibly in the future using WordPress API. For now, manual publishing is quick enough (5-10 min).

---

## File Naming Conventions

**Blog posts:** `YYYY-topic-slug.md`
- Example: `2024-github-profile-upgrade-toolkit.md`

**LinkedIn versions:** `YYYY-topic-slug-linkedin.md`

**Featured images:** `topic-slug-featured.png`

---

## Resources

### Documentation
- `workflows/blog-post-workflow.md` - Complete workflow
- `workflows/wordpress-publishing.md` - WordPress steps
- `PUBLISHING-GUIDE.md` - First post publishing guide

### Templates
- `templates/blog-post-template.md` - Post structure
- `templates/claude-prompts.md` - Claude prompts for different post types
- `templates/quick-reference.md` - Quick lookup guide

### Current Content
- `posts/2024-github-profile-upgrade-toolkit.md` - Ready to publish!
- `posts/2024-github-profile-upgrade-toolkit-linkedin.md` - LinkedIn version

---

## Tips for Success

1. **Start messy** - Give Claude rough ideas; it'll polish them
2. **Iterate freely** - Ask Claude to adjust tone, length, structure
3. **Trust the workflow** - It's designed to be fast and low-friction
4. **Use templates** - They save time and ensure consistency
5. **Preview in WordPress** - Always preview before publishing
6. **Track what works** - Note which posts get traction

---

## Getting Help

### With the Workflow
- Review `workflows/blog-post-workflow.md`
- Check `templates/quick-reference.md`
- Ask Claude to clarify any step

### With WordPress
- Review `workflows/wordpress-publishing.md`
- WordPress admin help: https://wordpress.org/support/
- SiteGround support for hosting issues

### With Claude
- Use the prompts in `templates/claude-prompts.md`
- Be specific about what you need
- Iterate until it's right

---

## Version Control (Optional)

If you want to track changes with git:

```bash
# Initialize repo
git init

# Add remote (if you create a GitHub repo)
git remote add origin https://github.com/irjudson/blog.git

# Regular workflow
git add .
git commit -m "Published: [post title]"
git push
```

---

**Ready to publish your first post? Open `PUBLISHING-GUIDE.md` and let's go!**
