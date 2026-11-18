# ulfgj.github.io

Personal website and blog for [ulf.gjerdingen](https://ulfgj.github.io), migrated from Jekyll to [Pelican](https://getpelican.com/) with a custom ported Lanyon theme.

## Requirements

- Python 3.10+
- Dependencies in `requirements.txt`

```bash
pip install -r requirements.txt
```

## Local Development

### Build local site
```bash
make html
# or
inv build
# or
pelican content -s pelicanconf.py
```

### Live reload & local preview
```bash
make devserver
# or
inv livereload
# opens http://localhost:8000 with auto-reload on file edits
```

## Creating New Posts

Use the new post task (replaces the old `rake post` command):

```bash
inv new-post --title "Your Post Title"
# or
make newpost TITLE="Your Post Title"
```

This creates a new dated Markdown file in `content/posts/` with pre-filled metadata.

## Production Build

```bash
make publish
# or
inv publish
# or
pelican content -o output -s publishconf.py
```

## Deployment

The site is automatically built and deployed to GitHub Pages via GitHub Actions upon pushing to the `master` branch (defined in `.github/workflows/deploy.yml`).

> **Note for GitHub Settings**:
> In repository **Settings** &rarr; **Pages** &rarr; **Build and deployment**, ensure **Source** is set to **GitHub Actions**.
