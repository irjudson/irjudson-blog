#!/usr/bin/env python3
"""
Convert markdown blog posts to effective LinkedIn posts.

LinkedIn formatting that works:
- Line breaks (important for scanability)
- Emojis (draw attention)
- Bullet points with → or •
- ALL CAPS for emphasis (sparingly)
- Parentheses for asides
- Dashes for lists
- Numbers for ordered lists

What LinkedIn does NOT support:
- Markdown bold/italic
- HTML tags
- Formatted code blocks
"""

import sys
import re
from pathlib import Path
import argparse


def convert_to_effective_linkedin(content):
    """Convert markdown to effective LinkedIn post format."""

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

    # Remove all markdown formatting (LinkedIn doesn't support it)
    # Remove bold
    content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
    # Remove italic
    content = re.sub(r'\*([^*\n]+?)\*', r'\1', content)
    # Remove inline code
    content = re.sub(r'`(.+?)`', r'\1', content)

    # Convert links to plain format
    content = re.sub(r'\[(.+?)\]\((.+?)\)', r'\2', content)

    # Strategic emoji placement for visual scanning
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

    # Make key phrases stand out with line breaks and spacing
    # LinkedIn algorithms favor posts with good whitespace

    # Add emphasis to opening quote (LinkedIn loves quotes)
    content = re.sub(
        r'^(Seneca: ".+?")',
        r'💡 \1\n\n▶ I call it serendipity.',
        content,
        flags=re.MULTILINE
    )

    # Remove the redundant "I call it serendipity" line if it appears twice
    content = re.sub(r'\n\nI call it serendipity\. And I built.*?\n\n---', '\n\n---', content)

    # Format section headers to stand out
    # Use line breaks before/after for emphasis
    content = re.sub(r'\n([✅🛠️📊🚀⏰📈] .+?:)\n', r'\n\n\1\n', content)

    # Convert bullet arrows to more visible format
    content = re.sub(r'^→ ', '→ ', content, flags=re.MULTILINE)

    # Make "That's not luck. That's preparation." stand out at the end
    content = re.sub(
        r"That's not luck\. That's preparation\.",
        r"━━━━━━━━━━━━━━━\n\nThat's not luck.\nThat's PREPARATION.\n\n━━━━━━━━━━━━━━━",
        content
    )

    # Clean up excessive blank lines but keep intentional spacing
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

    # Add strategic line breaks for mobile readability
    # LinkedIn mobile app favors shorter paragraphs

    # Break up long paragraphs (more than 3 lines)
    lines = content.split('\n')
    optimized = []
    paragraph_lines = []

    for line in lines:
        if line.strip() == '':
            if paragraph_lines:
                # If paragraph is more than 3 lines, add extra break
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

    # Ensure hashtags are on their own line at the end
    content = re.sub(r'\n(#[A-Za-z])', r'\n\n\1', content)

    return content


def main():
    parser = argparse.ArgumentParser(
        description='Convert blog post to effective LinkedIn format'
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
    linkedin_content = convert_to_effective_linkedin(content)

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
        output_path = input_path.with_suffix('').with_suffix('.linkedin.txt')

    output_path.write_text(linkedin_content, encoding='utf-8')

    print(f"✓ Converted to LinkedIn format: {output_path}")
    print(f"\n✓ Ready to paste into LinkedIn!")
    print(f"  1. Copy: {output_path}")
    print(f"  2. Go to: https://www.linkedin.com")
    print(f"  3. Click 'Start a post'")
    print(f"  4. Paste and post")
    print(f"\n💡 LinkedIn formatting optimized for:")
    print(f"  - Mobile readability")
    print(f"  - Visual scanning with emojis")
    print(f"  - Algorithm-friendly spacing")
    print(f"  - Professional impact")


if __name__ == '__main__':
    main()
