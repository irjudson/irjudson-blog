# Publishing Guide - GitHub Profile Toolkit Post

This is the complete guide for publishing the first blog post using our new workflow.

## Post Details

**Title:** Building a GitHub Profile Upgrade Toolkit (With Claude's Help)

**Files:**
- Blog post: `posts/2024-github-profile-upgrade-toolkit.md`
- LinkedIn version: `posts/2024-github-profile-upgrade-toolkit-linkedin.md`
- Featured image: `assets/featured-images/github-profile-featured-image.html`

---

## Step 1: Create Featured Image

1. Open `assets/featured-images/github-profile-featured-image.html` in your browser
2. Take a screenshot of the rendered image (1200x630px area)
3. Save as `github-profile-featured.png`
4. Keep this file ready for WordPress upload

**Alternative:** Use a screenshot from your GitHub profile or the github-profile-upgrade repository

---

## Step 2: Prepare Screenshots

The blog post needs these images:

1. **Opening image:**
   - Your polished GitHub profile screenshot
   - Or a before/after comparison

2. **Mid-content image:**
   - Claude Code in action (showing profile setup)
   - Or screenshot of the repository README

3. **Near-end image:**
   - Example of a completed profile from the repo
   - Or your own profile as example

**Quick way to get these:**
- Visit https://github.com/irjudson
- Visit https://github.com/irjudson/github-profile-upgrade
- Take screenshots of relevant sections
- Save to `assets/screenshots/`

---

## Step 3: Log into WordPress

1. Navigate to: https://irjudson.org/wp-admin
2. Log in with your credentials
3. Go to **Posts → Add New**

---

## Step 4: Add Content

1. **Title field:**
   ```
   Building a GitHub Profile Upgrade Toolkit (With Claude's Help)
   ```

2. **Body:**
   - Open `posts/2024-github-profile-upgrade-toolkit.md`
   - Copy everything AFTER the metadata section (after the `---`)
   - Paste into WordPress editor
   - WordPress will convert to blocks automatically

---

## Step 5: Insert Images

Look for these placeholders in the content:

1. **`[Opening: Screenshot of your before/after GitHub profile...]`**
   - Delete this placeholder text
   - Click the + button or /image
   - Upload or select your GitHub profile screenshot
   - Alt text: "Ivan Judson's optimized GitHub profile"

2. **`[Screenshot: Claude Code in action setting up a profile]`**
   - Same process
   - Upload Claude Code or repo screenshot
   - Alt text: "Claude Code automating GitHub profile setup"

3. **`[Screenshot: Example of completed profile from the repo]`**
   - Same process
   - Upload example profile screenshot
   - Alt text: "Example GitHub profile using the toolkit"

---

## Step 6: Set Categories and Tags

**Categories:**
- ✅ Technology
- ✅ Professional

**Tags (copy and paste this list):**
```
github, career-development, claude, ai-tools, developer-tools, professional-visibility, open-source, automation
```

---

## Step 7: Configure Yoast SEO

Scroll down to the **Yoast SEO** section:

**SEO Title:**
```
Building a GitHub Profile Upgrade Toolkit With Claude
```

**Meta Description:**
```
How I built a data-driven toolkit to optimize GitHub profiles in under 5 minutes using Claude automation. From job search insights to open-source resource.
```

**URL Slug:**
```
github-profile-upgrade-toolkit-claude
```

**Focus Keyphrase:** `github profile toolkit`

---

## Step 8: Add Featured Image

1. In the right sidebar, find **Featured Image**
2. Click **Set featured image**
3. Upload the `github-profile-featured.png` you created in Step 1
4. Alt text: `GitHub Profile Upgrade Toolkit with Claude automation`
5. Click **Set featured image**

---

## Step 9: LinkedIn Integration

**Important:** This post should be shared to LinkedIn!

1. Find the **Blog2Social** meta box (usually below Yoast SEO)
2. ✅ **CHECK** the box for "Share to LinkedIn"
3. Verify it's set to auto-post on publish

**The LinkedIn text is already prepared** in `posts/2024-github-profile-upgrade-toolkit-linkedin.md` if you need it.

---

## Step 10: Preview

1. Click **Preview** button (top right)
2. Review in new tab:
   - ✅ Title looks good
   - ✅ Images are placed correctly
   - ✅ All links work
   - ✅ Formatting is clean
   - ✅ No typos or weird formatting
3. Check mobile view if possible

---

## Step 11: Publish!

1. When everything looks good, click **Publish**
2. Visit the live post to verify: https://irjudson.org/[the-url-slug]/
3. Check LinkedIn to verify the post was shared

---

## Step 12: Archive in Git

After successful publishing:

```bash
cd /home/irjudson/Projects/irjudson/blog
git init  # if not already a git repo
git add .
git commit -m "Published: Building a GitHub Profile Upgrade Toolkit"
```

Update the main README to show this as published.

---

## Troubleshooting

### Featured Image Not Converting from HTML
- The HTML file needs to be screenshot and saved as PNG
- Open in browser (Chrome/Firefox)
- Use screenshot tool or browser dev tools
- Make sure it's 1200x630 or at least 800x600

### LinkedIn Not Auto-Posting
- Check Blog2Social plugin settings
- Verify LinkedIn connection is active
- Manual backup: Copy from `-linkedin.md` file and post manually

### Images Too Large
- WordPress prefers images under 500KB
- Use compression tool if needed
- Or resize before uploading

### Formatting Looks Wrong
- WordPress block editor gives granular control
- Adjust spacing, sizing as needed
- Preview frequently

---

## Post-Publishing Checklist

Within 24 hours:

- [ ] Verify post is live at irjudson.org
- [ ] Confirm LinkedIn auto-post worked
- [ ] Share on other channels if desired (Twitter, etc.)
- [ ] Monitor for any comments
- [ ] Fix any discovered issues
- [ ] Archive in git repository

---

## Estimated Time

- Featured image creation: 5 minutes
- Screenshots: 5 minutes
- WordPress setup: 10 minutes
- Review and publish: 5 minutes

**Total: ~25 minutes**

---

Good luck! This is your first post with the new workflow. After this one, it'll be even faster.
