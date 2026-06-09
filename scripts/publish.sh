#!/usr/bin/env bash
# Publish a draft post to _posts/.
#
# Usage: publish.sh <slug>
#   slug — bare slug without date prefix (e.g. led-controller-finding-the-gap)
#
# Moves _drafts/<slug>.md to _posts/YYYY-MM-DD-<slug>.md using today's date,
# updates the front matter date field, commits, and pushes.
#
# Prints the canonical post URL to stdout on success.
# Exits 1 on any error.

set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

if [[ $# -lt 1 ]]; then
  echo "usage: publish.sh <slug>" >&2
  exit 1
fi

SLUG="$1"
TODAY="$(date +%Y-%m-%d)"
DRAFT="$REPO/_drafts/${SLUG}.md"
POST="$REPO/_posts/${TODAY}-${SLUG}.md"

if [[ ! -f "$DRAFT" ]]; then
  echo "draft not found: $DRAFT" >&2
  exit 1
fi

# Update the date field in front matter to today
sed -i "s/^date:.*$/date: ${TODAY}/" "$DRAFT"

cp "$DRAFT" "$POST"
rm "$DRAFT"

git add "$POST" "$DRAFT" 2>/dev/null || git add "$POST"
git commit -m "post: ${SLUG}"
git push

# Derive URL: Jekyll uses the bare slug (no date) for the permalink
echo "https://irjudson.org/posts/${SLUG}/"
