"""
Pelican plugin that adds target="_blank" and rel="noopener noreferrer"
to all external links in article and page content.
"""
import re
import urllib.parse
from pelican import signals


def process_external_links(content_object):
    if not content_object or not getattr(content_object, "_content", None):
        return

    siteurl = content_object.settings.get("SITEURL", "")
    site_domain = urllib.parse.urlparse(siteurl).netloc.lower() if siteurl else "ulfgj.github.io"

    def replacer(match):
        attrs = match.group(1)
        href_match = re.search(r'href=[\"\']([^\"\']+)[\"\']', attrs, flags=re.IGNORECASE)
        if not href_match:
            return match.group(0)

        href = href_match.group(1).strip()
        parsed = urllib.parse.urlparse(href)

        # Only process external http / https links
        if parsed.scheme.lower() not in ("http", "https"):
            return match.group(0)

        # Do not modify links pointing to our own domain
        if parsed.netloc.lower() in (site_domain, "localhost", "127.0.0.1"):
            return match.group(0)

        # If target is already defined, don't overwrite
        if re.search(r'\btarget=', attrs, flags=re.IGNORECASE):
            return match.group(0)

        # Add or update rel attribute with security best practices
        rel_match = re.search(r'\brel=[\"\']([^\"\']*)[\"\']', attrs, flags=re.IGNORECASE)
        if rel_match:
            existing_rels = rel_match.group(1).split()
            needed = [r for r in ("noopener", "noreferrer") if r not in existing_rels]
            if needed:
                new_rel = " ".join(existing_rels + needed)
                attrs = attrs[:rel_match.start(1)] + new_rel + attrs[rel_match.end(1):]
        else:
            attrs += ' rel="noopener noreferrer"'

        attrs += ' target="_blank"'
        return f'<a {attrs.strip()}>'

    content_object._content = re.sub(r'<a\s+([^>]+)>', replacer, content_object._content, flags=re.IGNORECASE)


def register():
    signals.content_object_init.connect(process_external_links)
