#!/usr/bin/env python3
"""
Convert markdown blog posts to WordPress-friendly HTML.
Handles the blog post version from the standardized markdown format.
"""

import sys
import re
from pathlib import Path
import argparse


def convert_markdown_to_wordpress(content):
    """Convert markdown to WordPress HTML blocks."""

    # Remove metadata sections (everything before first # BLOG POST VERSION)
    blog_section_match = re.search(r'# BLOG POST VERSION\s*\n+', content)
    if blog_section_match:
        content = content[blog_section_match.end():]

    # Stop at LINKEDIN VERSION
    linkedin_match = re.search(r'\n+---+\s*\n+# LINKEDIN VERSION', content)
    if linkedin_match:
        content = content[:linkedin_match.start()]

    # Convert headers
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)

    # Convert bold
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)

    # Convert italic
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)

    # Convert links
    content = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', content)

    # Convert code blocks
    def replace_code_block(match):
        code = match.group(1)
        return f'<pre><code>{code}</code></pre>'

    content = re.sub(r'```bash\n(.+?)\n```', replace_code_block, content, flags=re.DOTALL)
    content = re.sub(r'```\n(.+?)\n```', replace_code_block, content, flags=re.DOTALL)

    # Convert inline code
    content = re.sub(r'`(.+?)`', r'<code>\1</code>', content)

    # Convert bullet lists
    def convert_list_block(match):
        items = match.group(0).strip().split('\n')
        html_items = []
        for item in items:
            item_text = re.sub(r'^- (.+)$', r'\1', item.strip())
            if item_text:
                html_items.append(f'<li>{item_text}</li>')
        return '<ul>\n' + '\n'.join(html_items) + '\n</ul>'

    # Find blocks of bullet points
    content = re.sub(r'(?:^- .+$\n?)+', convert_list_block, content, flags=re.MULTILINE)

    # Convert horizontal rules
    content = re.sub(r'^---+$', '<hr />', content, flags=re.MULTILINE)

    # Convert paragraphs (lines separated by blank lines)
    paragraphs = content.split('\n\n')
    formatted_paragraphs = []

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # Skip if already wrapped in HTML tag
        if para.startswith('<') and para.endswith('>'):
            formatted_paragraphs.append(para)
        # Skip if it's just a tag on its own line
        elif re.match(r'^<[^>]+>$', para):
            formatted_paragraphs.append(para)
        else:
            # Wrap in paragraph tag
            formatted_paragraphs.append(f'<p>{para}</p>')

    content = '\n\n'.join(formatted_paragraphs)

    # Clean up multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


def extract_metadata(content):
    """Extract metadata from the markdown file."""
    metadata = {}

    # Extract title
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1)

    # Extract categories
    cat_match = re.search(r'\*\*Categories:\*\* (.+)$', content, re.MULTILINE)
    if cat_match:
        metadata['categories'] = cat_match.group(1)

    # Extract tags
    tags_match = re.search(r'\*\*Tags:\*\* (.+)$', content, re.MULTILINE)
    if tags_match:
        metadata['tags'] = tags_match.group(1)

    # Extract SEO metadata
    seo_title_match = re.search(r'- \*\*SEO Title:\*\* (.+)$', content, re.MULTILINE)
    if seo_title_match:
        metadata['seo_title'] = seo_title_match.group(1)

    meta_desc_match = re.search(r'- \*\*Meta Description:\*\* (.+)$', content, re.MULTILINE)
    if meta_desc_match:
        metadata['meta_description'] = meta_desc_match.group(1)

    url_slug_match = re.search(r'- \*\*URL Slug:\*\* (.+)$', content, re.MULTILINE)
    if url_slug_match:
        metadata['url_slug'] = url_slug_match.group(1)

    return metadata


def main():
    parser = argparse.ArgumentParser(description='Convert markdown blog post to WordPress HTML')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output HTML file (default: input_file.html)')
    parser.add_argument('-m', '--metadata', action='store_true', help='Also output metadata')

    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Read input file
    content = input_path.read_text(encoding='utf-8')

    # Convert to WordPress HTML
    html = convert_markdown_to_wordpress(content)

    # Determine output file
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix('.html')

    # Write HTML
    output_path.write_text(html, encoding='utf-8')
    print(f"✓ Converted to WordPress HTML: {output_path}")

    # Extract and display metadata
    if args.metadata:
        metadata = extract_metadata(content)
        print("\n" + "="*60)
        print("METADATA FOR WORDPRESS:")
        print("="*60)

        if 'title' in metadata:
            print(f"\nTitle:\n{metadata['title']}")

        if 'categories' in metadata:
            print(f"\nCategories:\n{metadata['categories']}")

        if 'tags' in metadata:
            print(f"\nTags:\n{metadata['tags']}")

        if 'seo_title' in metadata:
            print(f"\nSEO Title:\n{metadata['seo_title']}")

        if 'meta_description' in metadata:
            print(f"\nMeta Description:\n{metadata['meta_description']}")

        if 'url_slug' in metadata:
            print(f"\nURL Slug:\n{metadata['url_slug']}")

        print("\n" + "="*60)

    print(f"\nReady to paste into WordPress!")
    print(f"1. Open: https://irjudson.org/wp-admin/post-new.php")
    print(f"2. Copy contents of: {output_path}")
    print(f"3. Paste into WordPress editor")


if __name__ == '__main__':
    main()
