# Publishing Workflow

## The Simple Way

**ONE command. TWO outputs. THREE minutes.**

```bash
./publish.py posts/my-post.md -u https://irjudson.org/my-post-url/
```

Or in VS Code:
1. Open your `.md` file
2. Press `Cmd+Shift+B`
3. Enter the blog URL
4. Done!

## What It Does

✅ Generates WordPress HTML (paste into WordPress code editor)
✅ Generates LinkedIn text (copies to clipboard automatically)
✅ Uses ONLY reliable formatting (no Unicode copy/paste issues)

## Output Files

- `my-post.wordpress.html` - Paste into WordPress code editor
- `my-post.linkedin.txt` - Already copied to clipboard (or manually copy)

## LinkedIn Formatting Strategy

After extensive testing, we use **reliable formatting only**:
- ✅ Emojis for visual anchors
- ✅ Line breaks for scannability
- ✅ ALL CAPS for emphasis
- ✅ Bullet arrows (→) and separators (━━━)
- ❌ No Unicode bold/italic (unreliable in copy/paste)

This ensures consistent formatting across all devices and platforms.

## WordPress Workflow

1. Run `./publish.py` (see above)
2. Go to WordPress admin: https://irjudson.org/wp-admin
3. Create new post
4. Switch to "Code editor" (Ctrl+Shift+Alt+M)
5. Paste the `.wordpress.html` content
6. Add featured image if needed
7. Publish!

## LinkedIn Workflow

1. Run `./publish.py` (see above)
2. Text is automatically in clipboard (Mac)
3. Go to: https://www.linkedin.com
4. Click "Start a post"
5. Paste (Cmd+V)
6. Review formatting
7. Post!

If clipboard didn't work: manually copy from `posts/my-post.linkedin.txt`

## Post Template

Every blog post should have this structure:

```markdown
# Post Title

**Published:** November 2024
**Categories:** Technology, Professional
**Tags:** tag1, tag2, tag3
**LinkedIn:** YES

---

**Copyright © 2024 Ivan Judson. All Rights Reserved.**

---

## SEO Metadata

- **SEO Title:** ...
- **Meta Description:** ...
- **URL Slug:** ...

---

# BLOG POST VERSION

Your full blog content here...

---

# LINKEDIN VERSION

Condensed LinkedIn version here (Smart Brevity principles)...

---

**Engagement prompt:** "Question to ask your audience?"
```

## Next Post - Simple Checklist

1. ✅ Write blog post in unified `.md` format
2. ✅ Run `./publish.py posts/my-post.md -u https://irjudson.org/url/`
3. ✅ Paste WordPress HTML into WordPress
4. ✅ Paste LinkedIn text into LinkedIn
5. ✅ Done in 3 minutes!

## Troubleshooting

**LinkedIn formatting looks wrong?**
- Make sure you're copying from the `.linkedin.txt` file
- Don't use the `.linkedin.md` file (has different formatting)
- The formatting uses plain text + emojis (no Unicode tricks)

**WordPress looks wrong?**
- Make sure you're pasting into "Code editor" not "Visual editor"
- Switch with Ctrl+Shift+Alt+M

**Script not executable?**
```bash
chmod +x publish.py
```

## Philosophy

Keep it simple. One command. Reliable formatting. No Unicode tricks. Just works.
