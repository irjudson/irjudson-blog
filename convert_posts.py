#!/usr/bin/env python3
"""Convert existing blog posts to Jekyll/Chirpy format."""

import os
import re
import json
import urllib.request

LEGACY_DIR = "posts/legacy"
PUBLISHED_DIR = "posts/published"
OUTPUT_DIR = "_posts"

# Fetch authoritative dates from WordPress REST API
def fetch_wp_dates():
    url = "https://irjudson.org/wp-json/wp/v2/posts?per_page=100"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            posts = json.loads(r.read())
        return {p["slug"]: p["date"] for p in posts}
    except Exception as e:
        print(f"Warning: could not fetch WP dates: {e}")
        return {}

# Map legacy filename stems to WP slugs
SLUG_MAP = {
    "2014-08-hdinsight-emulator-tip-1": "hdinsight-emulator-tip-1",
    "2014-08-new-adventure": "new-adventure",
    "2014-09-codalab": "codalab",
    "2014-09-getting-started-with-nitrogen": "getting-started-with-nitrogen",
    "2014-09-nitrogen-helloworld": "nitrogen-helloworld",
    "2014-09-startup-weekend-win": "startup-weekend-win",
    "2014-10-blogging-at-30k-iot-2014": "blogging-at-30k-iot-2014",
    "2014-10-building-alljoyn-js": "building-alljoyn-js",
    "2014-10-iot2014-recap": "iot2014-recap",
    "2014-10-moodcloud": "moodcloud",
    "2015-02-b-24-crew-remembers-the-fear-and-the-closeness": "b-24-crew-remembers-the-fear-and-the-closeness",
    "2015-02-building-iot-products": "building-iot-products",
    "2015-02-connected-things-2015": "connected-things-2015",
    "2015-02-hackster-io-hardware-hackfest": "hackster-io-hardware-hackfest",
    "2015-03-alljoyn-101-getting-started-with-alljoyn": "alljoyn-101-getting-started-with-alljoyn",
    "2015-03-open-source-user-experience-for-the-iot": "open-source-user-experience-for-the-iot",
    "2015-03-this-is-not-your-dads-powerpoint": "this-is-not-your-dads-powerpoint",
    "2015-04-kiva-why-i-only-lend-to-women-outside-the-us": "kiva-why-i-only-lend-to-women-outside-the-us",
    "2015-05-build-2015-my-first-build": "build-2015-my-first-build",
    "2015-06-serendipity-geek-culture": "serendipity-geek-culture",
    "2015-08-summer-to-fall-turning-the-page": "summer-to-fall-turning-the-page",
    "2015-11-hacking-esp8266s": "hacking-esp8266s",
    "2015-11-thingsexpo-2015": "thingsexpo-2015",
    "2018-04-24-months": "24-months",
    "2023-02-welcome-back": "welcome-back",
    "2024-01-new-year-same-you": "new-year-same-you",
    "2025-10-hack-your-car-with-nitrogen": "hack-your-car-with-nitrogen",
    "2025-10-adding-face-detection-to-your-pi-powered-motion-detector-2": "adding-face-detection-to-your-pi-powered-motion-detector-2",
}


def slugify(title):
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def parse_tags(raw):
    tags = [t.strip().lower() for t in raw.split(",") if t.strip()]
    # remove duplicates preserving order
    seen = set()
    out = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def parse_categories(raw):
    return [c.strip() for c in raw.split(",") if c.strip()]


def strip_boilerplate(text):
    """Remove copyright block and SEO metadata section."""
    # Remove copyright block (between --- markers)
    text = re.sub(
        r"\*\*Copyright ©.*?See \[COPYRIGHT\.md\].*?\n\n---\n",
        "",
        text,
        flags=re.DOTALL,
    )
    # Remove SEO metadata section (## SEO Metadata ... up to # BLOG POST VERSION or end)
    text = re.sub(
        r"## SEO Metadata\n.*?(?=\n# BLOG POST VERSION|\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    # Remove "# BLOG POST VERSION" header
    text = re.sub(r"^# BLOG POST VERSION\s*\n", "", text, flags=re.MULTILINE)
    return text.strip()


def convert_legacy(filepath, wp_dates):
    with open(filepath) as f:
        raw = f.read()

    lines = raw.split("\n")

    # Extract title from first # heading
    title = ""
    for line in lines:
        m = re.match(r"^#\s+(.+)", line)
        if m:
            title = m.group(1).strip()
            break

    # Extract metadata lines
    published_raw = ""
    categories_raw = ""
    tags_raw = ""
    for line in lines:
        m = re.match(r"\*\*Published:\*\*\s*(.+)", line)
        if m:
            published_raw = m.group(1).strip()
        m = re.match(r"\*\*Categories:\*\*\s*(.+)", line)
        if m:
            categories_raw = m.group(1).strip()
        m = re.match(r"\*\*Tags:\*\*\s*(.+)", line)
        if m:
            tags_raw = m.group(1).strip()

    # Determine slug and date
    stem = os.path.splitext(os.path.basename(filepath))[0]
    wp_slug = SLUG_MAP.get(stem)
    if wp_slug and wp_slug in wp_dates:
        date_str = wp_dates[wp_slug]  # e.g. "2014-08-08T18:38:25"
        date_iso = date_str.replace("T", " ") + " +0000"
        date_prefix = date_str[:10]
    else:
        # Fall back to parsing "Month Year" from **Published:**
        date_prefix = stem[:7].replace("-", "-") + "-01"
        date_iso = date_prefix + " 00:00:00 +0000"
        print(f"  Warning: no WP date for {stem}, using {date_prefix}")

    categories = parse_categories(categories_raw) if categories_raw else []
    tags = parse_tags(tags_raw) if tags_raw else []

    # Strip title line, metadata block, copyright, and boilerplate
    content = re.sub(r"^#\s+.+\n", "", raw, count=1)
    content = re.sub(r"\*\*(Published|Categories|Tags|LinkedIn):\*\*.*\n", "", content)
    content = strip_boilerplate(content)
    # Remove leading horizontal rules
    content = re.sub(r"^---\s*\n", "", content, count=2)
    content = content.strip()

    # Build frontmatter
    cats_yaml = "[" + ", ".join(categories) + "]" if categories else "[]"
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in tags) + "]" if tags else "[]"

    output = f"""---
title: "{title.replace('"', "'")}"
date: {date_iso}
categories: {cats_yaml}
tags: {tags_yaml}
---

{content}
"""

    out_slug = slugify(title)
    out_filename = f"{date_prefix}-{out_slug}.md"
    return out_filename, output


def convert_published(filepath, wp_dates):
    """Published posts have an SEO metadata section — strip it and grab content after BLOG POST VERSION."""
    with open(filepath) as f:
        raw = f.read()

    # Only handle .md files
    if not filepath.endswith(".md"):
        return None, None

    # Skip non-blog files
    if any(x in filepath for x in [".linkedin.", ".wordpress."]):
        return None, None

    lines = raw.split("\n")

    title = ""
    for line in lines:
        m = re.match(r"^#\s+(.+)", line)
        if m:
            title = m.group(1).strip()
            break

    categories_raw = ""
    tags_raw = ""
    published_raw = ""
    for line in lines:
        m = re.match(r"\*\*Published:\*\*\s*(.+)", line)
        if m:
            published_raw = m.group(1).strip()
        m = re.match(r"\*\*Categories:\*\*\s*(.+)", line)
        if m:
            categories_raw = m.group(1).strip()
        m = re.match(r"\*\*Tags:\*\*\s*(.+)", line)
        if m:
            tags_raw = m.group(1).strip()

    # Find slug from WP API
    stem = os.path.splitext(os.path.basename(filepath))[0]
    # strip date prefix like "2024-11-"
    name_part = re.sub(r"^\d{4}-\d{2}-", "", stem)

    # Try to find matching WP slug
    wp_slug = None
    for slug in wp_dates:
        if slug.startswith(name_part) or name_part in slug:
            wp_slug = slug
            break

    if wp_slug and wp_slug in wp_dates:
        date_str = wp_dates[wp_slug]
        date_iso = date_str.replace("T", " ") + " +0000"
        date_prefix = date_str[:10]
    else:
        date_prefix = stem[:10] if re.match(r"\d{4}-\d{2}-\d{2}", stem) else "2024-11-04"
        date_iso = date_prefix + " 00:00:00 +0000"

    categories = parse_categories(categories_raw) if categories_raw else []
    tags = parse_tags(tags_raw) if tags_raw else []

    # Extract content after "# BLOG POST VERSION" if present, else strip headers
    if "# BLOG POST VERSION" in raw:
        content = raw.split("# BLOG POST VERSION", 1)[1].strip()
    else:
        content = re.sub(r"^#\s+.+\n", "", raw, count=1)
        content = re.sub(r"\*\*(Published|Categories|Tags|LinkedIn):\*\*.*\n", "", content)
        content = strip_boilerplate(content)
        content = re.sub(r"^---\s*\n", "", content, count=2)

    content = content.strip()

    cats_yaml = "[" + ", ".join(categories) + "]" if categories else "[]"
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in tags) + "]" if tags else "[]"

    out_slug = slugify(title)
    out_filename = f"{date_prefix}-{out_slug}.md"

    output = f"""---
title: "{title.replace('"', "'")}"
date: {date_iso}
categories: {cats_yaml}
tags: {tags_yaml}
---

{content}
"""
    return out_filename, output


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Fetching WordPress dates...")
    wp_dates = fetch_wp_dates()
    print(f"  Got {len(wp_dates)} post dates from WP API")

    converted = set()

    print("\nConverting legacy posts...")
    for fname in sorted(os.listdir(LEGACY_DIR)):
        if not fname.endswith(".md") or fname.upper().startswith("README"):
            continue
        fpath = os.path.join(LEGACY_DIR, fname)
        out_fname, content = convert_legacy(fpath, wp_dates)
        if out_fname in converted:
            print(f"  SKIP duplicate: {out_fname}")
            continue
        out_path = os.path.join(OUTPUT_DIR, out_fname)
        with open(out_path, "w") as f:
            f.write(content)
        converted.add(out_fname)
        print(f"  {fname} -> {out_fname}")

    print("\nConverting published posts...")
    for fname in sorted(os.listdir(PUBLISHED_DIR)):
        if not fname.endswith(".md"):
            continue
        if any(x in fname for x in [".linkedin.", ".wordpress."]):
            continue
        fpath = os.path.join(PUBLISHED_DIR, fname)
        out_fname, content = convert_published(fpath, wp_dates)
        if out_fname is None:
            continue
        if out_fname in converted:
            print(f"  SKIP duplicate: {out_fname}")
            continue
        out_path = os.path.join(OUTPUT_DIR, out_fname)
        with open(out_path, "w") as f:
            f.write(content)
        converted.add(out_fname)
        print(f"  {fname} -> {out_fname}")

    print(f"\nDone. {len(converted)} posts written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
