# Blog Repository for irjudson.org

Content repository and workflow documentation for Ivan Judson's blog at [irjudson.org](https://irjudson.org).

This repository contains blog post source files, publishing workflows, and templates for creating content with Claude's assistance.

## Quick Start

**New here?** Start with [START-HERE.md](START-HERE.md)

**Publishing a post?** Follow [PUBLISHING-GUIDE.md](PUBLISHING-GUIDE.md)

**Creating content?** Use the prompts in [templates/claude-prompts.md](templates/claude-prompts.md)

## Repository Structure

```
blog/
├── posts/
│   ├── published/          # Published articles with all generated assets
│   └── legacy/             # Migrated WordPress posts (2014-2025)
├── drafts/
│   └── {article-name}/     # One directory per article with all iterations
├── assets/                 # Images, diagrams, media files
├── templates/              # Post templates and style guides
├── workflows/              # Publishing workflow documentation
└── *.py                    # Publishing automation scripts
```

**Key Files:**
- `publish.py` - Master publishing script (WordPress + LinkedIn)
- `PUBLISHING.md` - Simple 3-minute publishing workflow
- `STRUCTURE.md` - Detailed structure documentation
- `SITE-OPTIMIZATION-TODO.md` - Website improvement checklist

## The Workflow

**ONE command to publish:**

```bash
./publish.py posts/my-post.md -u https://irjudson.org/article-url/
```

Or in VS Code: **Cmd+Shift+B** → enter URL → done!

**What it does:**
- ✅ Generates WordPress HTML (paste into WordPress code editor)
- ✅ Generates LinkedIn text with Unicode bold/italic
- ✅ Copies LinkedIn to clipboard automatically
- ✅ All outputs ready in 5 minutes

**See [PUBLISHING.md](PUBLISHING.md) for complete workflow**

## Site Information

- **Domain:** [irjudson.org](https://irjudson.org)
- **Platform:** WordPress on SiteGround
- **Theme:** Twenty Twenty-Four (block theme)
- **Key Plugins:** Yoast SEO, Blog2Social (LinkedIn integration)

## Published Posts

1. **[Preparing for Opportunity: A GitHub Profile Toolkit](posts/published/2024-11-preparing-for-opportunity.md)** - November 2024
   - URL: https://irjudson.org/preparing-for-opportunity-github-profile/
   - Topics: Career development, GitHub, preparation, serendipity
   - Seneca's wisdom: "Luck is what happens when preparation meets opportunity"

## Drafts in Progress

- **GitHub Profile Toolkit** - Multiple iterations exploring different angles
  - See `drafts/github-profile-toolkit/` for evolution
  - Final version published (see above)

- **Blog Workflow with Claude Code** - Documentation of this workflow's creation
  - See `drafts/blog-workflow/`
  - Potential next post

## Legacy Posts

28 posts migrated from WordPress (2014-2024) are archived in [posts/legacy/](posts/legacy/).

See [posts/legacy/README.md](posts/legacy/README.md) for the complete chronological list.

## Documentation

**Essential Guides:**
- [PUBLISHING.md](PUBLISHING.md) - Simple 3-minute publishing workflow
- [STRUCTURE.md](STRUCTURE.md) - Repository organization and file structure
- [SITE-OPTIMIZATION-TODO.md](SITE-OPTIMIZATION-TODO.md) - Website improvement checklist

**Legacy Guides:**
- [START-HERE.md](START-HERE.md) - Original repository overview
- [PUBLISHING-GUIDE.md](PUBLISHING-GUIDE.md) - Original publishing guide (replaced by PUBLISHING.md)
- [workflows/](workflows/) - Original workflow documentation (mostly replaced by publish.py)

## Copyright and License

**Blog content and images:** © Ivan Judson. All Rights Reserved.
- All blog posts, articles, and written content
- All original photographs and images
- See [COPYRIGHT.md](COPYRIGHT.md) for full copyright notice

**Workflow documentation and templates:** [MIT License](LICENSE)
- Workflow docs, templates, and automation scripts
- Free to use and adapt for your own blog workflow

For licensing questions or permission requests, see [LICENSE](LICENSE) and [COPYRIGHT.md](COPYRIGHT.md).
