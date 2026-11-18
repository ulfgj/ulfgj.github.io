#!/usr/bin/env python3
"""Helper script to create a new post (replaces legacy rake post['title'])."""
import argparse
import datetime
import os
import re
import sys

def create_post(title):
    now = datetime.datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%Y-%m-%d %H:%M:%S')

    slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title).strip().lower()
    slug = re.sub(r'[\s]+', '-', slug)

    filename = f"{date_str}-{slug}.md"
    posts_dir = os.path.join(os.path.dirname(__file__), 'content', 'posts')
    os.makedirs(posts_dir, exist_ok=True)
    filepath = os.path.join(posts_dir, filename)

    if os.path.exists(filepath):
        print(f"Error: {filepath} already exists!", file=sys.stderr)
        sys.exit(1)

    template = f"""Title: {title}
Date: {time_str}
Slug: {slug}
Category: blog
Tags: 

Write your post content here...
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"Created new post: {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Create a new blog post.")
    parser.add_argument("title", nargs="?", default="New Post", help="Title of the new post")
    args = parser.parse_args()
    create_post(args.title)

if __name__ == "__main__":
    main()
