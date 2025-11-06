# Converting Markdown to WordPress

Quick guide for converting blog posts from markdown to WordPress-ready HTML.

---

## Using the Converter

### Method 1: VS Code Task (Easiest)

1. Open your markdown post in VS Code (e.g., `posts/2024-11-preparing-for-opportunity.md`)
2. Press `Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows/Linux)
3. Select "Convert to WordPress"
4. The converter will:
   - Create a `.html` file next to your markdown
   - Display all metadata in the terminal
   - Show you what's ready to paste

### Method 2: Command Line

```bash
# From blog repository root
./convert-to-wordpress.py posts/2024-11-preparing-for-opportunity.md -m

# Output will be: posts/2024-11-preparing-for-opportunity.html
```

**Options:**
- `-m` or `--metadata` - Display metadata for WordPress (title, categories, tags, SEO)
- `-o FILE` or `--output FILE` - Specify custom output file

---

## What the Converter Does

### Converts:
- `**bold**` → `<strong>bold</strong>`
- `*italic*` → `<em>italic</em>`
- `[link](url)` → `<a href="url">link</a>`
- `## Headers` → `<h2>Headers</h2>`
- Bullet lists → `<ul><li>` HTML lists
- Code blocks → `<pre><code>` blocks
- Paragraphs → `<p>` tags

### Extracts:
- Title
- Categories
- Tags
- SEO Title
- Meta Description
- URL Slug

### Handles:
- Automatically finds `# BLOG POST VERSION` section
- Stops before `# LINKEDIN VERSION`
- Skips all metadata at the top

---

## WordPress Publishing Workflow

### Step 1: Convert
```bash
./convert-to-wordpress.py posts/2024-11-preparing-for-opportunity.md -m
```

### Step 2: Copy Metadata
From the terminal output, you'll see:
```
Title: [copy this]
Categories: [copy this]
Tags: [copy this]
SEO Title: [copy this]
Meta Description: [copy this]
URL Slug: [copy this]
```

### Step 3: Copy HTML
```bash
# Open the HTML file
cat posts/2024-11-preparing-for-opportunity.html

# Or copy to clipboard (Mac)
pbcopy < posts/2024-11-preparing-for-opportunity.html

# Or copy to clipboard (Linux)
xclip -selection clipboard < posts/2024-11-preparing-for-opportunity.html
```

### Step 4: Paste into WordPress
1. Go to: https://irjudson.org/wp-admin/post-new.php
2. Click the three dots (⋮) in top right → "Code editor"
3. Paste the HTML
4. Click "Visual editor" to see formatted result
5. Add metadata (categories, tags, SEO settings)
6. Add images
7. Preview and publish

---

## VS Code Keyboard Shortcuts

Once configured:

**Convert current file:**
- Mac: `Cmd+Shift+B`
- Windows/Linux: `Ctrl+Shift+B`

This runs the converter on whatever markdown file you have open.

---

## Example: Converting the Opportunity Post

```bash
# Convert the post
./convert-to-wordpress.py posts/2024-11-preparing-for-opportunity.md -m

# Output shows:
✓ Converted to WordPress HTML: posts/2024-11-preparing-for-opportunity.html

============================================================
METADATA FOR WORDPRESS:
============================================================

Title:
Preparing for Opportunity: A GitHub Profile Toolkit

Categories:
Technology, Professional

Tags:
github, career-development, job-search, preparation, opportunity, professional-visibility, serendipity

SEO Title:
Preparing for Opportunity: GitHub Profile Toolkit

Meta Description:
Seneca said luck is what happens when preparation meets opportunity. This GitHub profile toolkit helps engineers prepare so when opportunity comes, they're ready to be found.

URL Slug:
preparing-for-opportunity-github-profile

============================================================

Ready to paste into WordPress!
1. Open: https://irjudson.org/wp-admin/post-new.php
2. Copy contents of: posts/2024-11-preparing-for-opportunity.html
3. Paste into WordPress editor
```

---

## Troubleshooting

### Converter not executable
```bash
chmod +x convert-to-wordpress.py
```

### Python not found
Make sure Python 3 is installed:
```bash
python3 --version
```

### VS Code task not appearing
1. Make sure you opened the blog folder as the workspace
2. Try `Cmd+Shift+P` → "Tasks: Run Task" → "Convert to WordPress"

### HTML looks wrong in WordPress
1. Switch to "Code editor" view in WordPress
2. Paste there first
3. Then switch to "Visual editor" to see result

---

## Tips

**Before converting:**
- Make sure your markdown file follows the standard format
- Ensure `# BLOG POST VERSION` section exists
- Check that markdown formatting is clean

**After converting:**
- Review the HTML in a text editor first
- Check that lists converted properly
- Verify links are correct

**In WordPress:**
- Always preview before publishing
- Check both desktop and mobile views
- Verify images are in the right places

---

## What Gets Skipped

The converter automatically skips:
- Top metadata section (Published, Categories, Tags, Copyright, SEO Metadata)
- The `# LINKEDIN VERSION` section
- Empty lines before and after sections

You only get the clean blog post content, ready for WordPress.

---

## Future Enhancements

Possible additions:
- Direct WordPress API publishing
- Image upload automation
- Category/tag auto-creation
- Preview generation
- Batch conversion

For now, the two-step process (convert → paste) is fast and reliable.
