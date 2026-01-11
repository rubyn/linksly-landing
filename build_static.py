#!/usr/bin/env python3
"""Build static HTML from Flask templates for GitHub Pages."""

import os
import shutil
from jinja2 import Environment, FileSystemLoader

# Configuration
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = 'docs'
STATIC_DIR = 'static'

# Meta data (same as app.py)
META_DATA = {
    'title': 'Linksly - Save Links, Share Smarter',
    'description': 'Save links for later and share them with the right people at the perfect time. Smart link management for iOS with beautiful previews and group messaging.',
    'keywords': 'link sharing, save for later, iOS app, link management, group messaging, smart sharing',
    'og_image': '/static/images/og-image.png',
    'twitter_card': 'summary_large_image',
    'app_store_url': 'https://apps.apple.com/app/linksly',  # Update when live
    'domain': 'linksly.app'
}

def url_for(endpoint, **kwargs):
    """Mock Flask's url_for for static file references."""
    if endpoint == 'static':
        filename = kwargs.get('filename', '')
        return f'./static/{filename}'
    return '#'

def build():
    """Build static HTML files."""
    # Create output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    env.globals['url_for'] = url_for

    # Pages to build
    pages = [
        ('index.html', 'index.html'),
        ('privacy.html', 'privacy.html'),
        ('terms.html', 'terms.html'),
        ('support.html', 'support.html'),
    ]

    # Render each page
    for template_name, output_name in pages:
        try:
            template = env.get_template(template_name)
            html = template.render(meta=META_DATA)

            output_path = os.path.join(OUTPUT_DIR, output_name)
            with open(output_path, 'w') as f:
                f.write(html)
            print(f"  ✓ {output_name}")
        except Exception as e:
            print(f"  ✗ {template_name}: {e}")

    # Copy static files
    static_src = STATIC_DIR
    static_dst = os.path.join(OUTPUT_DIR, 'static')
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst)
        print(f"  ✓ static/ folder copied")

    # Create CNAME file for custom domain
    cname_path = os.path.join(OUTPUT_DIR, 'CNAME')
    with open(cname_path, 'w') as f:
        f.write('linksly.app')
    print(f"  ✓ CNAME (linksly.app)")

    # Create .nojekyll to disable Jekyll processing
    nojekyll_path = os.path.join(OUTPUT_DIR, '.nojekyll')
    with open(nojekyll_path, 'w') as f:
        pass
    print(f"  ✓ .nojekyll")

    print(f"\n✅ Built to ./{OUTPUT_DIR}/")
    print(f"\nNext steps:")
    print(f"  1. git init (if not already)")
    print(f"  2. git add .")
    print(f"  3. git commit -m 'Initial landing page'")
    print(f"  4. Create repo on GitHub and push")
    print(f"  5. Enable GitHub Pages from 'docs' folder")
    print(f"  6. Add custom domain in repo settings")

if __name__ == '__main__':
    print("Building static site...\n")
    build()
