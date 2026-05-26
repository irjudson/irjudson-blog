# Publishing Guide

How to write and publish a post to irjudson.org.

## The short version

1. Write a `.md` file in `_posts/` named `YYYY-MM-DD-slug.md`
2. Add Jekyll frontmatter at the top
3. `git add`, `git commit`, `git push`
4. GitHub Actions builds and deploys automatically (~2 min)

That's it. No WordPress, no plugins, no CMS login.

---

## Frontmatter template

```yaml
---
title: "Your Post Title"
date: 2026-05-26 09:00:00 -0600
categories: [Category1, Category2]
tags: ["tag1", "tag2", "tag3"]
image:
  path: /assets/img/posts/your-post/hero.jpg
  alt: "Description of the hero image"
---
```

- **categories**: broad topics, title-cased — `[Projects, AI]`, `[Astronomy, Hardware]`
- **tags**: specific, lowercase — `["python", "seestar", "astrophotography"]`
- **image**: optional hero image shown at top and in post listing
- **date timezone**: Three Forks, MT is `-0600` (MDT) or `-0700` (MST)

---

## Images

Put images in `assets/img/posts/your-post-slug/`. Reference them in the post as:

```markdown
![Alt text](/assets/img/posts/your-post-slug/filename.jpg)
_Optional caption underneath_
```

Use JPEGs for photos, PNGs for screenshots. Keep photos under 2MB — compress if needed.

---

## Drafts

Work in progress goes in `_drafts/` with the same format but no date in the filename:

```
_drafts/astronomus-follow-up.md
```

To preview drafts locally: `bundle exec jekyll serve --drafts`

Drafts are excluded from the live site until moved to `_posts/`.

---

## Writing with Claude

The typical flow:
1. Write or paste a LinkedIn post, notes, or rough draft
2. Ask Claude to expand it into a blog post — longer, more informal, with links and embedded images
3. Review and adjust tone/detail
4. Drop into `_posts/`, commit, push

For image-heavy posts, tell Claude which images exist in the project and it'll copy them to `assets/img/posts/` and embed them with captions.

---

## After publishing

- Post is live at `irjudson.org` once the Actions build finishes
- Check the **Actions** tab at `github.com/irjudson/irjudson-blog` if you want to watch the build
- Share the URL to LinkedIn/Bluesky/Twitter manually — there's no auto-posting

---

## Checklist

- [ ] Frontmatter is valid YAML (check indentation)
- [ ] Filename is `YYYY-MM-DD-slug.md`
- [ ] Images are in `assets/img/posts/` and paths match
- [ ] Links open to the right places
- [ ] Pushed to `main`
- [ ] Actions build passed
