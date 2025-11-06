#!/usr/bin/env python3
"""
Convert markdown blog posts to LinkedIn with Unicode formatting.

LinkedIn requires Unicode characters for bold/italic, not markdown.
"""

import sys
import re
from pathlib import Path
import argparse


# Unicode character mappings
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


def convert_to_linkedin_unicode(content):
    """Convert markdown to LinkedIn format with Unicode formatting."""

    # Find LINKEDIN VERSION section
    linkedin_section_match = re.search(r'# LINKEDIN VERSION\s*\n+', content)
    if linkedin_section_match:
        content = content[linkedin_section_match.end():]
    else:
        print("Error: Could not find # LINKEDIN VERSION section", file=sys.stderr)
        return None

    # Stop at next major section
    next_section_match = re.search(r'\n+---+\s*\n+#', content)
    if next_section_match:
        content = content[:next_section_match.start()]

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

    # Convert links to plain format
    content = re.sub(r'\[(.+?)\]\((.+?)\)', r'\2', content)

    # Strategic emoji placement
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

    # Add emphasis to opening quote
    content = re.sub(
        r'^(Seneca: ".+?")',
        r'💡 \1\n\n▶ I call it serendipity.',
        content,
        flags=re.MULTILINE
    )

    # Remove redundant line
    content = re.sub(r'\n\nI call it serendipity\. And I built.*?\n\n---', '\n\n---', content)

    # Format section headers
    content = re.sub(r'\n([✅🛠️📊🚀⏰📈] .+?:)\n', r'\n\n\1\n', content)

    # Make ending stand out
    content = re.sub(
        r"That's not luck\. That's preparation\.",
        r"━━━━━━━━━━━━━━━\n\nThat's not luck.\nThat's PREPARATION.\n\n━━━━━━━━━━━━━━━",
        content
    )

    # Clean up excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    # Ensure proper spacing around horizontal rules
    content = re.sub(r'\n*---+\n*', '\n\n---\n\n', content)

    return content.strip()


def add_blog_url(content, blog_url):
    """Add blog URL after repository link."""
    repo_pattern = r'(🔗 Repository: https://[^\n]+)'
    replacement = f'\\1\n📝 Full post: {blog_url}'

    if re.search(repo_pattern, content):
        content = re.sub(repo_pattern, replacement, content)
    else:
        # Add before hashtags
        hashtag_match = re.search(r'\n\n(#[A-Za-z]+)', content)
        if hashtag_match:
            insert_pos = hashtag_match.start()
            content = content[:insert_pos] + f'\n\n📝 Full post: {blog_url}\n' + content[insert_pos:]

    return content


def optimize_for_linkedin(content):
    """Apply LinkedIn-specific optimizations."""

    # Break up long paragraphs
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

    # Ensure hashtags are on their own line
    content = re.sub(r'\n(#[A-Za-z])', r'\n\n\1', content)

    return content


def main():
    parser = argparse.ArgumentParser(
        description='Convert blog post to LinkedIn format with Unicode bold/italic'
    )
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-u', '--url', help='Blog post URL')
    parser.add_argument('-o', '--output', help='Output file (default: .linkedin.txt)')

    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Read and convert
    content = input_path.read_text(encoding='utf-8')
    linkedin_content = convert_to_linkedin_unicode(content)

    if linkedin_content is None:
        sys.exit(1)

    # Add blog URL
    if args.url:
        linkedin_content = add_blog_url(linkedin_content, args.url)

    # Optimize for LinkedIn
    linkedin_content = optimize_for_linkedin(linkedin_content)

    # Write output
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix('').with_suffix('.linkedin.md')

    output_path.write_text(linkedin_content, encoding='utf-8')

    print(f"✓ Converted to LinkedIn format with Unicode formatting: {output_path}")
    print(f"\n✓ Ready to paste into LinkedIn!")
    print(f"  1. Copy: {output_path}")
    print(f"  2. Go to: https://www.linkedin.com")
    print(f"  3. Click 'Start a post'")
    print(f"  4. Paste and post")
    print(f"\n💡 LinkedIn formatting includes:")
    print(f"  - Unicode bold for emphasis (𝗯𝗼𝗹𝗱)")
    print(f"  - Unicode italic for quotes (𝘪𝘵𝘢𝘭𝘪𝘤)")
    print(f"  - Emojis for visual anchors")
    print(f"  - Mobile-friendly spacing")


if __name__ == '__main__':
    main()
