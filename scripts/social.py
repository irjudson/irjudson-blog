#!/usr/bin/env python3
"""Generate platform-optimized social copy for a blog post.

Usage: social.py <slug> <platform>
  slug     — post slug (with or without YYYY-MM-DD prefix)
  platform — linkedin | twitter

Finds the post in _posts/ or _drafts/, calls Claude to generate
optimized social copy, and prints it to stdout.

Exit 0 on success, 1 on failure.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

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
    '8': '𝟴', '9': '𝟵',
}

ITALIC_MAP = {
    'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧', 'g': '𝘨', 'h': '𝘩',
    'i': '𝘪', 'j': '𝘫', 'k': '𝘬', 'l': '𝘭', 'm': '𝘮', 'n': '𝘯', 'o': '𝘰', 'p': '𝘱',
    'q': '𝘲', 'r': '𝘳', 's': '𝘴', 't': '𝘵', 'u': '𝘶', 'v': '𝘷', 'w': '𝘸', 'x': '𝘹',
    'y': '𝘺', 'z': '𝘻',
    'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍', 'G': '𝘎', 'H': '𝘏',
    'I': '𝘐', 'J': '𝘑', 'K': '𝘒', 'L': '𝘓', 'M': '𝘔', 'N': '𝘕', 'O': '𝘖', 'P': '𝘗',
    'Q': '𝘘', 'R': '𝘙', 'S': '𝘚', 'T': '𝘛', 'U': '𝘜', 'V': '𝘝', 'W': '𝘞', 'X': '𝘟',
    'Y': '𝘠', 'Z': '𝘡',
}


def to_bold(text: str) -> str:
    return ''.join(BOLD_MAP.get(c, c) for c in text)


def to_italic(text: str) -> str:
    return ''.join(ITALIC_MAP.get(c, c) for c in text)


def apply_unicode_formatting(text: str) -> str:
    """Convert **bold** and *italic* markdown to Unicode equivalents."""
    text = re.sub(r'\*\*(.+?)\*\*', lambda m: to_bold(m.group(1)), text)
    text = re.sub(r'\*([^*\n]+?)\*', lambda m: to_italic(m.group(1)), text)
    return text


def find_post(slug: str) -> Path | None:
    """Find a post file by slug, checking _posts then _drafts."""
    # Strip any date prefix the caller may have included
    bare = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', slug)

    for post in sorted((REPO_ROOT / "_posts").glob("*.md"), reverse=True):
        if bare in post.stem:
            return post

    draft = REPO_ROOT / "_drafts" / f"{bare}.md"
    if draft.exists():
        return draft

    return None


def strip_front_matter(content: str) -> str:
    if content.startswith('---'):
        end = content.find('\n---', 3)
        if end != -1:
            return content[end + 4:].lstrip()
    return content


def get_post_url(slug: str, post_path: Path) -> str:
    """Derive the canonical blog URL from the post filename."""
    stem = post_path.stem  # YYYY-MM-DD-slug
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.*)', stem)
    if m:
        year, month, day, bare = m.groups()
        return f"https://irjudson.org/posts/{bare}/"
    return f"https://irjudson.org/posts/{slug}/"


_LINKEDIN_SYSTEM = """\
You write LinkedIn posts for Ivan Judson — technologist, hardware builder, and founder of Buffalo Jump Forge.
Ivan's voice: direct, concrete, confident without bragging. Writes like someone who builds things and has
opinions earned from doing the work, not from watching others do it.

LinkedIn rules (non-negotiable):
- NO links anywhere in the post body. The blog URL goes in the FIRST COMMENT, not the post.
- Short paragraphs — 1-3 sentences max. Mobile readers scan, not read.
- Strong hook in the first 2 lines — must work before the "see more" cutoff.
- Use **bold** for key phrases (will be converted to Unicode bold).
- Use *italic* sparingly for emphasis (will be converted to Unicode italic).
- 5-8 hashtags at the very end on their own line.
- End with a single genuine engagement question — something the audience actually knows about.
- No "excited to share" or "thrilled to announce" language.
- No links, no @mentions, no URLs of any kind in the body.

Output ONLY the post text — no explanation, no metadata, no preamble."""

_LINKEDIN_PROMPT = """\
Write a LinkedIn post for this blog article. The post should drive readers to the blog (URL posted in comments).

Blog post content:
---
{body}
---

Post URL (goes in first comment, NOT in the post body): {url}
"""


def generate_linkedin(body: str, url: str) -> str:
    import subprocess as _sp
    prompt = _LINKEDIN_PROMPT.format(body=body[:6000], url=url)
    result = _sp.run(
        ["claude", "--print", "--system-prompt", _LINKEDIN_SYSTEM, "-p", prompt],
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude --print failed: {result.stderr.strip()}")
    return apply_unicode_formatting(result.stdout.strip())


def main() -> None:
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} <slug> <platform>", file=sys.stderr)
        sys.exit(1)

    slug, platform = sys.argv[1], sys.argv[2].lower()

    if platform not in ("linkedin",):
        print(f"unsupported platform: {platform} (supported: linkedin)", file=sys.stderr)
        sys.exit(1)

    post = find_post(slug)
    if not post:
        print(f"post not found for slug: {slug}", file=sys.stderr)
        sys.exit(1)

    content = post.read_text(encoding="utf-8")
    body = strip_front_matter(content)
    url = get_post_url(slug, post)

    if platform == "linkedin":
        copy = generate_linkedin(body, url)

    print(copy)


if __name__ == "__main__":
    main()
