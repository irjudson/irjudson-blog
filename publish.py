#!/usr/bin/env python3
"""
Master publish script - ONE command to prepare blog post for all platforms.

Usage:
    ./publish.py posts/my-post.md -u https://irjudson.org/my-post/

Output:
    - WordPress HTML (ready to paste)
    - LinkedIn text (ready to paste with Unicode bold/italic)
    - Automatically copies LinkedIn version to clipboard
"""

import sys
import re
from pathlib import Path
import argparse
import subprocess


# Unicode character mappings for LinkedIn bold/italic
BOLD_MAP = {
    'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵',
    'i': '𝗶', 'j': '𝗷', 'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽',
    'q': '𝗾', 'r': '𝗿', 's': '𝘀', 't': '𝘁', 'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅',
    'y': '𝘆', 'z': '𝘇',
    'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛',
    'I': '𝗜', 'J': '𝗝', 'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣',
    'Q': '𝗤', 'R': '𝗥', 'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫',
    'Y': '𝗬', 'Z': '𝗭',
    '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳',
    '8': '𝟴', '9': '𝟵'
}

ITALIC_MAP = {
    'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧', 'g': '𝘨', 'h': '𝘩',
    'i': '𝘪', 'j': '𝘫', 'k': '𝘬', 'l': '𝘭', 'm': '𝘮', 'n': '𝘯', 'o': '𝘰', 'p': '𝘱',
    'q': '𝘲', 'r': '𝘳', 's': '𝘴', 't': '𝘵', 'u': '𝘶', 'v': '𝘷', 'w': '𝘸', 'x': '𝘹',
    'y': '𝘺', 'z': '𝘻',
    'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍', 'G': '𝘎', 'H': '𝘏',
    'I': '𝘐', 'J': '𝘑', 'K': '𝘒', 'L': '𝘓', 'M': '𝘔', 'N': '𝘕', 'O': '𝘖', 'P': '𝘗',
    'Q': '𝘘', 'R': '𝘙', 'S': '𝘚', 'T': '𝘛', 'U': '𝘜', 'V': '𝘝', 'W': '𝘞', 'X': '𝘟',
    'Y': '𝘠', 'Z': '𝘡'
}


def to_unicode_bold(text):
    """Convert text to Unicode bold characters."""
    return ''.join(BOLD_MAP.get(c, c) for c in text)


def to_unicode_italic(text):
    """Convert text to Unicode italic characters."""
    return ''.join(ITALIC_MAP.get(c, c) for c in text)


def extract_linkedin_section(content):
    """Extract the LINKEDIN VERSION section."""
    linkedin_section_match = re.search(r'# LINKEDIN VERSION\s*\n+', content)
    if not linkedin_section_match:
        return None

    content = content[linkedin_section_match.end():]

    # Stop at next major section
    next_section_match = re.search(r'\n+---+\s*\n+#', content)
    if next_section_match:
        content = content[:next_section_match.start()]

    return content


def convert_to_linkedin_reliable(content, blog_url=None):
    """Convert to LinkedIn format with Unicode bold/italic."""

    content = extract_linkedin_section(content)
    if not content:
        return None

    # Convert markdown bold to Unicode bold
    def replace_bold(match):
        return to_unicode_bold(match.group(1))
    content = re.sub(r'\*\*(.+?)\*\*', replace_bold, content)

    # Convert markdown italic to Unicode italic
    def replace_italic(match):
        return to_unicode_italic(match.group(1))
    content = re.sub(r'\*([^*\n]+?)\*', replace_italic, content)

    # Remove inline code backticks
    content = re.sub(r'`(.+?)`', r'\1', content)

    # Convert links to plain URLs
    content = re.sub(r'\[(.+?)\]\((.+?)\)', r'\2', content)

    # Add strategic emojis (these work perfectly)
    emoji_map = {
        'What I built:': '🛠️ What I built:',
        'What "prepared" looks like:': '✅ What "prepared" looks like:',
        'Real impact:': '📊 Real impact:',
        'Try it:': '🚀 Try it:',
        'When to prepare:': '⏰ When to prepare:',
        'The compound effect:': '📈 The compound effect:',
        'Repository:': '🔗 Repository:',
        'Full post:': '📝 Full post:',
        'Time:': '⏱️ Time:',
        'Benefit:': '✨ Benefit:',
    }

    for key, value in emoji_map.items():
        content = content.replace(key, value)

    # Opening emphasis
    content = re.sub(
        r'^(Seneca: ".+?")',
        r'💡 \1\n\n▶ I call it serendipity.',
        content,
        flags=re.MULTILINE
    )

    # Remove redundant lines
    content = re.sub(r'\n\nI call it serendipity\. And I built.*?\n\n---', '\n\n---', content)

    # Format section headers with spacing
    content = re.sub(r'\n([✅🛠️📊🚀⏰📈] .+?:)\n', r'\n\n\1\n', content)

    # Make ending dramatic
    content = re.sub(
        r"That's not luck\. That's preparation\.",
        r"━━━━━━━━━━━━━━━\n\nThat's not luck.\nThat's PREPARATION.\n\n━━━━━━━━━━━━━━━",
        content
    )

    # Clean up spacing
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    content = re.sub(r'\n*---+\n*', '\n\n---\n\n', content)

    # Add blog URL if provided
    if blog_url:
        repo_pattern = r'(🔗 Repository: https://[^\n]+)'
        if re.search(repo_pattern, content):
            content = re.sub(repo_pattern, f'\\1\n📝 Full post: {blog_url}', content)
        else:
            # Add before hashtags
            hashtag_match = re.search(r'\n\n(#[A-Za-z]+)', content)
            if hashtag_match:
                insert_pos = hashtag_match.start()
                content = content[:insert_pos] + f'\n\n📝 Full post: {blog_url}\n' + content[insert_pos:]

    # Optimize for mobile (break long paragraphs)
    lines = content.split('\n')
    optimized = []
    paragraph_lines = []

    for line in lines:
        if line.strip() == '':
            if paragraph_lines:
                if len(paragraph_lines) > 3:
                    optimized.extend(paragraph_lines[:2])
                    optimized.append('')
                    optimized.extend(paragraph_lines[2:])
                else:
                    optimized.extend(paragraph_lines)
                paragraph_lines = []
            optimized.append(line)
        else:
            paragraph_lines.append(line)

    if paragraph_lines:
        optimized.extend(paragraph_lines)

    content = '\n'.join(optimized)

    # Ensure hashtags are separated
    content = re.sub(r'\n(#[A-Za-z])', r'\n\n\1', content)

    return content.strip()


def extract_blog_section(content):
    """Extract the BLOG POST VERSION section."""
    blog_section_match = re.search(r'# BLOG POST VERSION\s*\n+', content)
    if not blog_section_match:
        return None

    content = content[blog_section_match.end():]

    # Stop at LINKEDIN VERSION or end
    next_section = re.search(r'\n+---+\s*\n+# LINKEDIN VERSION', content)
    if next_section:
        content = content[:next_section.start()]

    return content


def convert_to_wordpress(content):
    """Convert blog section to WordPress HTML."""

    content = extract_blog_section(content)
    if not content:
        return None

    # Convert markdown to HTML
    lines = content.split('\n')
    html_lines = []
    in_list = False
    in_code_block = False
    code_block_lines = []

    for line in lines:
        # Code blocks
        if line.startswith('```'):
            if in_code_block:
                # End code block
                html_lines.append('<pre><code>')
                html_lines.extend(code_block_lines)
                html_lines.append('</code></pre>')
                html_lines.append('')
                code_block_lines = []
                in_code_block = False
            else:
                # Start code block
                in_code_block = True
            continue

        if in_code_block:
            code_block_lines.append(line)
            continue

        # Headings
        if line.startswith('## '):
            if in_list:
                html_lines.append('</ul>')
                html_lines.append('')
                in_list = False
            html_lines.append(f'<h2>{line[3:]}</h2>')
            html_lines.append('')
            continue

        # Lists
        if line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{line[2:]}</li>')
            continue

        # Close list if not continuing
        if in_list and line.strip() and not line.startswith('- '):
            html_lines.append('</ul>')
            html_lines.append('')
            in_list = False

        # Bold, italic, links, inline code
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
        line = re.sub(r'`(.+?)`', r'<code>\1</code>', line)
        line = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', line)

        # Horizontal rules
        if line.strip() == '---':
            html_lines.append('<hr>')
            html_lines.append('')
            continue

        # Paragraphs
        if line.strip():
            html_lines.append(f'<p>{line}</p>')
        else:
            html_lines.append('')

    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)


def main():
    parser = argparse.ArgumentParser(
        description='ONE command to publish blog post to all platforms'
    )
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-u', '--url', help='Blog post URL', required=True)

    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"❌ Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    content = input_path.read_text(encoding='utf-8')

    # Generate WordPress version
    print("📝 Converting to WordPress HTML...")
    wordpress_html = convert_to_wordpress(content)
    if wordpress_html:
        wp_output = input_path.with_suffix('').with_suffix('.wordpress.html')
        wp_output.write_text(wordpress_html, encoding='utf-8')
        print(f"✅ WordPress HTML: {wp_output}")
    else:
        print("⚠️  No BLOG POST VERSION section found")

    # Generate LinkedIn version
    print("\n📱 Converting to LinkedIn (reliable formatting)...")
    linkedin_text = convert_to_linkedin_reliable(content, args.url)
    if linkedin_text:
        li_output = input_path.with_suffix('').with_suffix('.linkedin.txt')
        li_output.write_text(linkedin_text, encoding='utf-8')
        print(f"✅ LinkedIn text: {li_output}")

        # Copy to clipboard
        try:
            subprocess.run(['pbcopy'], input=linkedin_text.encode('utf-8'), check=True)
            print("✅ LinkedIn text copied to clipboard!")
            print("\n🚀 READY TO POST:")
            print("   1. Go to https://www.linkedin.com")
            print("   2. Click 'Start a post'")
            print("   3. Paste (Cmd+V)")
            print("   4. Review and post!")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("⚠️  Could not copy to clipboard (pbcopy not available)")
            print(f"\n📋 Manually copy from: {li_output}")
    else:
        print("⚠️  No LINKEDIN VERSION section found")

    print("\n" + "="*50)
    print("✅ PUBLISH COMPLETE")
    print("="*50)
    print(f"\n📝 WordPress: Paste {wp_output.name} into WordPress code editor")
    print(f"📱 LinkedIn: Already in clipboard - just paste!")


if __name__ == '__main__':
    main()
