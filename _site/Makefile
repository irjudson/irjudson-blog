BUNDLE := $(HOME)/.local/share/gem/ruby/3.2.0/bin/bundle

.PHONY: serve drafts install clean

# Preview published posts only
serve:
	$(BUNDLE) exec jekyll serve --port 4000

# Preview including drafts and future-dated posts
drafts:
	$(BUNDLE) exec jekyll serve --drafts --future --port 4000

# Install dependencies (run once after cloning)
install:
	$(BUNDLE) install

# Remove generated site
clean:
	rm -rf _site .jekyll-cache
