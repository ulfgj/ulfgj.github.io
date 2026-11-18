import os
import re
import sys
import datetime

try:
    from invoke import task
except ImportError:
    # If invoke is not installed, tasks.py will not register tasks
    task = None

if task:
    SETTINGS_FILE_BASE = 'pelicanconf.py'
    SETTINGS_FILE_PUB = 'publishconf.py'

    @task
    def clean(c):
        """Remove generated files."""
        if os.path.isdir('output'):
            c.run('rm -rf output')
        if os.path.isdir('__pycache__'):
            c.run('rm -rf __pycache__')

    @task
    def build(c):
        """Build local version of site."""
        c.run(f'pelican content -s {SETTINGS_FILE_BASE}')

    @task
    def rebuild(c):
        """Clean and build local version of site."""
        clean(c)
        build(c)

    @task
    def publish(c):
        """Build production version of site."""
        c.run(f'pelican content -s {SETTINGS_FILE_PUB}')

    @task
    def serve(c, port=8000):
        """Serve site locally on given port (default 8000)."""
        c.run(f'pelican --listen --port {port}')

    @task
    def livereload(c, port=8000):
        """Automatically reload browser and rebuild site on change."""
        c.run(f'pelican --autoreload --listen --port {port} content -s {SETTINGS_FILE_BASE}')

    @task
    def new_post(c, title):
        """Create a new post in content/posts/ (replaces rake post['title'])."""
        from new_post import create_post
        create_post(title)
