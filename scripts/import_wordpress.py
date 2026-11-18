#!/usr/bin/env python3
"""
Import posts and media from ulfgj.wordpress.com into Pelican content directory.
"""
import datetime
import html
import json
import os
import re
import urllib.request
from html.parser import HTMLParser

API_URL = "https://public-api.wordpress.com/rest/v1.1/sites/ulfgj.wordpress.com/posts?number=100"
POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "posts")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "images", "wp")


class WordPressHTMLToMarkdown(HTMLParser):
    def __init__(self, image_map):
        super().__init__()
        self.image_map = image_map
        self.result = []
        self.current_link = None
        self.skip_data = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        tag = tag.lower()

        if tag == "p":
            if self.result and not self.result[-1].endswith("\n\n"):
                self.result.append("\n\n")
        elif tag == "br":
            self.result.append("\n")
        elif tag in ("b", "strong"):
            self.result.append("**")
        elif tag in ("i", "em"):
            self.result.append("*")
        elif tag == "a":
            href = attrs_dict.get("href", "")
            # If link is wrapping an image pointing to the same image, don't nest redundantly
            self.current_link = href
            self.result.append("[")
        elif tag == "img":
            src = attrs_dict.get("src", "")
            alt = attrs_dict.get("alt", "")
            # Check if this image was downloaded locally
            local_path = self.image_map.get(src, src)
            self.result.append(f"![{alt}]({local_path})")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in ("b", "strong"):
            self.result.append("**")
        elif tag in ("i", "em"):
            self.result.append("*")
        elif tag == "a":
            href = self.current_link or ""
            # If the anchor only wrapped an image with the same URL, clean it up
            self.result.append(f"]({href})")
            self.current_link = None
        elif tag == "p":
            if self.result and not self.result[-1].endswith("\n\n"):
                self.result.append("\n\n")

    def handle_data(self, data):
        self.result.append(data)

    def get_markdown(self):
        text = "".join(self.result).strip()
        # Clean up links wrapping images like [![alt](img)](img) -> ![alt](img)
        text = re.sub(
            r'\[!\[([^\]]*)\]\(([^)]+)\)\]\(\2\)',
            r'![\1](\2)',
            text
        )
        # Normalize excessive newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()


def download_image(url, target_dir):
    filename = os.path.basename(url.split("?")[0])
    target_path = os.path.join(target_dir, filename)

    if not os.path.exists(target_path):
        print(f"Downloading image: {url} -> {target_path}")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp, open(target_path, "wb") as f:
            f.write(resp.read())
    else:
        print(f"Image already exists: {target_path}")

    # Return local path formatted for Pelican static assets
    return f"{{static}}/images/wp/{filename}"


def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)

    print("Fetching posts from WordPress API...")
    req = urllib.request.Request(API_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    posts = data.get("posts", [])
    print(f"Retrieved {len(posts)} posts.")

    # Step 1: Detect and download images
    image_map = {}
    for post in posts:
        content_html = post.get("content", "")
        img_urls = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content_html)
        for img_url in img_urls:
            if img_url not in image_map:
                local_asset_path = download_image(img_url, IMAGES_DIR)
                image_map[img_url] = local_asset_path
                # Also handle link url if link points to full image
                image_map[img_url.split("?")[0]] = local_asset_path

    # Step 2: Convert posts
    imported_files = []
    for post in posts:
        # Title
        raw_title = post.get("title", "").strip()
        title = html.unescape(raw_title)

        # Date
        # ISO string: 2013-09-25T20:45:05+00:00
        raw_date = post.get("date", "")
        dt = datetime.datetime.fromisoformat(raw_date)
        date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        file_date_prefix = dt.strftime("%Y-%m-%d")

        # Slug
        slug = post.get("slug", "").strip()

        # Category
        raw_cats = [c for c in post.get("categories", {}).keys() if c != "Uncategorized"]
        if raw_cats:
            category = raw_cats[0].lower()
        else:
            category = "blog"

        # Tags
        tags = list(post.get("tags", {}).keys())
        tags_line = f"Tags: {', '.join(tags)}" if tags else "Tags:"

        # Convert Content
        raw_content = post.get("content", "")
        parser = WordPressHTMLToMarkdown(image_map)
        parser.feed(raw_content)
        markdown_body = parser.get_markdown()
        # Decode any remaining entities in markdown body
        markdown_body = html.unescape(markdown_body)

        # Build Markdown File
        file_content = f"""Title: {title}
Date: {date_str}
Slug: {slug}
Category: {category}
{tags_line}

{markdown_body}
"""

        filename = f"{file_date_prefix}-{slug}.md"
        filepath = os.path.join(POSTS_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(file_content)

        print(f"Created post: {filename} ({title})")
        imported_files.append(filename)

    print(f"\nSuccessfully imported {len(imported_files)} posts into {POSTS_DIR}!")


if __name__ == "__main__":
    main()
