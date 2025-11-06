#!/usr/bin/env python3
"""
Convert markdown blog posts to LinkedIn-friendly plain text.
Handles the LinkedIn version from the standardized markdown format.
"""

import sys
import re
from pathlib import Path
import argparse


def convert_markdown_to_linkedin(content):
    """Convert markdown to LinkedIn plain text with strategic emojis."""

    # Find LINKEDIN VERSION section
    linkedin_section_match = re.search(r'# LINKEDIN VERSION\s*\n+', content)
    if linkedin_section_match:
        content = content[linkedin_section_match.end():]
    else:
        print("Warning: Could not find # LINKEDIN VERSION section", file=sys.stderr)
        return None

    # Stop at any subsequent major section or end
    next_section_match = re.search(r'\n+---+\s*\n+#', content)
    if next_section_match:
        content = content[:next_section_match.start()]

    # Keep markdown bold (LinkedIn supports it)
    # Don't remove ** - LinkedIn will render it

    # Remove markdown italic (LinkedIn doesn't support single *)
    content = re.sub(r'\*([^*]+?)\*', r'\1', content)

    # Convert markdown links to plain text with URL
    content = re.sub(r'\[(.+?)\]\((.+?)\)', r'\1 (\2)', content)

    # Remove inline code backticks
    content = re.sub(r'`(.+?)`', r'\1', content)

    # Remove horizontal rules
    content = re.sub(r'^---+$', '', content, flags=re.MULTILINE)

    # Add strategic emojis for key sections
    emoji_replacements = [
        (r'(What I built:)', r'🛠️ \1'),
        (r'(What "prepared" looks like:)', r'✅ \1'),
        (r'(Real impact:)', r'📊 \1'),
        (r'(Try it:)', r'🚀 \1'),
        (r'(When to prepare:)', r'⏰ \1'),
        (r'(The compound effect:)', r'📈 \1'),
        (r'(Repository:)', r'🔗 \1'),
        (r'(Full post:)', r'📝 \1'),
    ]

    for pattern, replacement in emoji_replacements:
        content = re.sub(pattern, replacement, content)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Remove leading/trailing whitespace
    content = content.strip()

    return content


def add_blog_url(content, blog_url):
    """Add blog URL to the LinkedIn post."""
    # Find where to insert the blog URL (after repository link)
    repo_match = re.search(r'(Repository: https://github\.com/[^\n]+)', content)
    if repo_match:
        insert_pos = repo_match.end()
        content = content[:insert_pos] + f"\nFull post: {blog_url}" + content[insert_pos:]
    else:
        # If no repository link found, add at the end before hashtags
        hashtag_match = re.search(r'\n#[A-Za-z]+', content)
        if hashtag_match:
            insert_pos = hashtag_match.start()
            content = content[:insert_pos] + f"\n\nFull post: {blog_url}\n" + content[insert_pos:]
        else:
            # Just add at the end
            content += f"\n\nFull post: {blog_url}"

    return content


def main():
    parser = argparse.ArgumentParser(description='Convert markdown blog post to LinkedIn plain text')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-u', '--url', help='Blog post URL to add to LinkedIn version')
    parser.add_argument('-o', '--output', help='Output text file (default: input_file-linkedin.txt)')
    parser.add_argument('-c', '--clipboard', action='store_true', help='Copy to clipboard (Mac only)')

    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Read input file
    content = input_path.read_text(encoding='utf-8')

    # Convert to LinkedIn plain text
    linkedin_text = convert_markdown_to_linkedin(content)

    if linkedin_text is None:
        print("Error: Could not find LinkedIn version in file", file=sys.stderr)
        sys.exit(1)

    # Add blog URL if provided
    if args.url:
        linkedin_text = add_blog_url(linkedin_text, args.url)

    # Determine output file
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix('').with_suffix('.linkedin.md')

    # Write text
    output_path.write_text(linkedin_text, encoding='utf-8')
    print(f"✓ Converted to LinkedIn text: {output_path}")

    # Copy to clipboard if requested (Mac only)
    if args.clipboard:
        import subprocess
        try:
            subprocess.run(['pbcopy'], input=linkedin_text.encode('utf-8'), check=True)
            print("✓ Copied to clipboard!")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Note: Clipboard copy failed (pbcopy not available)", file=sys.stderr)

    print(f"\nReady to paste into LinkedIn!")
    print(f"1. Go to: https://www.linkedin.com")
    print(f"2. Click 'Start a post'")
    print(f"3. Paste from: {output_path}")
    if args.clipboard:
        print("   (or just Cmd+V - already in clipboard!)")
    print(f"4. Review and post")


if __name__ == '__main__':
    main()
