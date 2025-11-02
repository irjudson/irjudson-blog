#!/usr/bin/env python3
"""
Parse WordPress XML export and convert posts to markdown.
"""

import xml.etree.ElementTree as ET
import html
import re
from pathlib import Path
from datetime import datetime

# WordPress namespaces
NAMESPACES = {
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wfw': 'http://wellformedweb.org/CommentAPI/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'wp': 'http://wordpress.org/export/1.2/',
}

def clean_html(html_content):
    """Convert HTML to markdown-ish format."""
    if not html_content:
        return ""

    # Unescape HTML entities
    content = html.unescape(html_content)

    # Convert common HTML tags to markdown
    # Headings
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', content, flags=re.DOTALL)

    # Bold and italic
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)

    # Links
    content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)

    # Lists
    content = re.sub(r'<ul[^>]*>', r'\n', content)
    content = re.sub(r'</ul>', r'\n', content)
    content = re.sub(r'<ol[^>]*>', r'\n', content)
    content = re.sub(r'</ol>', r'\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', content, flags=re.DOTALL)

    # Paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)

    # Line breaks
    content = re.sub(r'<br\s*/?>', r'\n', content)

    # Code blocks
    content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', content, flags=re.DOTALL)
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL)

    # Images
    content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', r'![\2](\1)', content)
    content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*>', r'![](\1)', content)

    # Blockquotes
    content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'\n> \1\n', content, flags=re.DOTALL)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Clean up multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Clean up whitespace
    content = content.strip()

    return content

def get_text(element, tag, namespaces=None):
    """Safely get text from an XML element."""
    if namespaces:
        elem = element.find(tag, namespaces)
    else:
        elem = element.find(tag)
    return elem.text if elem is not None and elem.text else ""

def parse_wordpress_export(xml_file):
    """Parse WordPress XML export file."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find all items (posts, pages, etc.)
    items = root.findall('.//item')

    posts = []
    for item in items:
        # Check if it's a post (not page, attachment, etc.)
        post_type = get_text(item, 'wp:post_type', NAMESPACES)
        if post_type != 'post':
            continue

        # Check if it's published
        status = get_text(item, 'wp:status', NAMESPACES)
        if status != 'publish':
            continue

        # Extract post data
        title = get_text(item, 'title')
        post_date = get_text(item, 'wp:post_date', NAMESPACES)
        content = get_text(item, 'content:encoded', NAMESPACES)
        excerpt = get_text(item, 'excerpt:encoded', NAMESPACES)
        post_name = get_text(item, 'wp:post_name', NAMESPACES)

        # Categories and tags
        categories = []
        tags = []
        for category in item.findall('category'):
            domain = category.get('domain', '')
            term = category.text if category.text else ''
            if domain == 'category':
                categories.append(term)
            elif domain == 'post_tag':
                tags.append(term)

        posts.append({
            'title': title,
            'date': post_date,
            'slug': post_name,
            'content': content,
            'excerpt': excerpt,
            'categories': categories,
            'tags': tags,
        })

    return posts

def create_markdown_post(post, output_dir):
    """Create a markdown file from a post."""
    # Parse date
    try:
        date_obj = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
        date_str = date_obj.strftime('%B %Y')
        year = date_obj.strftime('%Y')
        month = date_obj.strftime('%m')
    except:
        date_str = "Unknown"
        year = "unknown"
        month = "unknown"

    # Create filename
    slug = post['slug'] if post['slug'] else re.sub(r'[^\w\s-]', '', post['title'].lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    filename = f"{year}-{month}-{slug}.md"

    # Create markdown content
    md_content = f"""# {post['title']}

**Published:** {date_str}
**Categories:** {', '.join(post['categories']) if post['categories'] else 'Uncategorized'}
**Tags:** {', '.join(post['tags']) if post['tags'] else 'none'}

---

**Copyright © {year} Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

"""

    # Add excerpt if exists
    if post['excerpt']:
        md_content += f"*{clean_html(post['excerpt'])}*\n\n---\n\n"

    # Add content
    md_content += clean_html(post['content'])

    # Add migration note at the end
    md_content += f"""

---

*This post was migrated from WordPress. Original publication date: {post['date']}*
"""

    # Write file
    output_path = output_dir / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    return filename, date_obj

def main():
    # Parse the export file
    xml_file = Path.home() / 'Downloads' / 'ivanrjudson.WordPress.2025-11-02.xml'
    output_dir = Path('posts') / 'legacy'
    output_dir.mkdir(exist_ok=True, parents=True)

    print(f"Parsing {xml_file}...")
    posts = parse_wordpress_export(xml_file)

    print(f"\nFound {len(posts)} published posts")
    print(f"Converting to markdown in {output_dir}/\n")

    created_files = []
    for post in posts:
        filename, date_obj = create_markdown_post(post, output_dir)
        created_files.append((filename, date_obj, post['title']))
        print(f"✓ Created: {filename}")

    print(f"\n✅ Converted {len(created_files)} posts to markdown")

    # Create index file
    index_path = output_dir / 'README.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Legacy Blog Posts\n\n")
        f.write("Posts migrated from WordPress on November 2024.\n\n")
        f.write("**Copyright © Ivan Judson. All Rights Reserved.**\n\n")
        f.write("---\n\n")
        f.write("## Posts by Date\n\n")

        # Sort by date descending
        created_files.sort(key=lambda x: x[1], reverse=True)

        for filename, date_obj, title in created_files:
            date_str = date_obj.strftime('%B %d, %Y')
            f.write(f"- [{title}]({filename}) - {date_str}\n")

    print(f"✓ Created index: {index_path}")

if __name__ == '__main__':
    main()
