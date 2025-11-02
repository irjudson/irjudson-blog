# WordPress Publishing Workflow

## Site Information

- **Domain:** irjudson.org
- **Platform:** WordPress on SiteGround
- **Admin URL:** https://irjudson.org/wp-admin
- **Theme:** Twenty Twenty-Four (block theme)

### Key Plugins
- **Yoast SEO** - SEO optimization and metadata
- **Blog2Social** - LinkedIn auto-posting integration
- **Really Simple SSL** - HTTPS enforcement

---

## Publishing Checklist

### 1. Create New Post
- Navigate to **Posts → Add New** in WordPress admin
- Or use the quick link: `https://irjudson.org/wp-admin/post-new.php`

### 2. Add Content
- **Title:** Copy from the blog post markdown file (the H1 at the top)
- **Body:** Paste the full blog post content
- WordPress will auto-convert markdown formatting to blocks

### 3. Insert Images
Look for image placeholders in the content (marked with `[Screenshot: ...]`):
- Click where the image should go
- Add image block
- Upload or select from media library
- Add alt text for accessibility
- **Add copyright in caption:** "© Ivan Judson" (for original photos)

**Common image locations:**
- Opening: Hero image or profile screenshot
- Mid-content: Process screenshots, examples
- Near end: Results or example outputs

**Copyright for images:**
- All original photos should include © Ivan Judson in caption or metadata
- WordPress preserves EXIF data which includes copyright info
- Consider adding watermark to photos if publicly visible

### 4. Set Categories & Tags

**Categories:**
- Select from: Technology, Professional, Personal, Philosophy, Projects
- Usually 1-2 categories per post

**Tags:**
- Add specific tags from the post metadata
- Common tags: github, ai-tools, career-development, etc.
- 4-8 tags typical

### 5. Configure SEO (Yoast)

Scroll down to the Yoast SEO section:

- **SEO Title:** Use the "SEO Title" from post metadata (usually shorter than actual title)
- **Meta Description:** Copy from post metadata (155-160 characters)
- **URL Slug:** Copy from post metadata (lowercase, hyphens, no special chars)

**Quality checks:**
- Green light on readability (or at least orange)
- All SEO recommendations addressed
- Preview looks good on Google search

### 6. Add Featured Image

- In right sidebar, find "Featured Image"
- Upload the featured image from `assets/featured-images/`
- **Size requirement:** 1200 x 630 px (or at least 800 x 600)
- Add alt text: Brief description of the image

**Creating featured image from HTML:**
1. Open the HTML file in browser
2. Take a screenshot (or use browser dev tools to export)
3. Save as PNG
4. Upload to WordPress

### 7. LinkedIn Integration

If the post metadata says `LinkedIn: YES`:

- ✅ **CHECK** the "Share to LinkedIn" box
- This is usually in the Blog2Social meta box
- Verify it's set to auto-post on publish
- Use the LinkedIn version from `*-linkedin.md` file if you want custom text

**When to share to LinkedIn:**
- Professional insights or technical content
- Career development topics
- Project showcases with professional value
- How-tos and guides

**When NOT to share:**
- Pure personal/hobby content
- Philosophy without professional angle
- Very short posts or quick notes

### 8. Preview & Publish

Before publishing:
1. **Click "Preview"** - Review in new tab
2. **Check formatting** - Headers, paragraphs, images
3. **Check links** - All links work and open correctly
4. **Mobile check** - Preview on mobile if possible
5. **Read through** - Final proofread

When ready:
- **Click "Publish"** (or "Schedule" if you want delayed publishing)
- Verify the post appears correctly on the site
- Check that LinkedIn post went through (if enabled)

---

## Post-Publishing

### Immediate
- [ ] Visit the live post URL to verify it's live
- [ ] Check LinkedIn to confirm auto-post worked
- [ ] Share to other channels if appropriate (Twitter, etc.)

### Within 24 hours
- [ ] Check for any comments
- [ ] Monitor analytics for initial traffic
- [ ] Fix any formatting issues discovered

### Archive
- [ ] Move markdown file from `drafts/` to `posts/` in this repo
- [ ] Add post to the README.md list
- [ ] Commit to git with message: "Published: [post title]"

---

## Troubleshooting

### Featured Image Not Showing
- Check image size (minimum 800x600)
- Verify it's set as "Featured Image" not just inserted in content
- Try re-uploading

### LinkedIn Auto-Post Failed
- Check Blog2Social settings
- Verify LinkedIn connection is active
- Manual post as backup using the LinkedIn version file

### SEO Score Low
- Focus on green/orange, not perfection
- Key items: meta description, focus keyword, readability
- Don't obsess over 100% score

### Formatting Issues
- WordPress may auto-format markdown differently
- Use preview liberally
- Adjust spacing and formatting as needed
- Block editor gives precise control

---

## Quick Commands

**Create new post:**
```
https://irjudson.org/wp-admin/post-new.php
```

**View all posts:**
```
https://irjudson.org/wp-admin/edit.php
```

**Media library:**
```
https://irjudson.org/wp-admin/upload.php
```
