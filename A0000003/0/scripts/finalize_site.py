#!/usr/bin/env python3
"""
Finalize the Great Calculator GitHub Pages site after the public base URL is known.

This renders docs/sitemap.xml and docs/robots.txt from templates and optionally
writes docs/CNAME for a custom domain.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
CONFIG = ROOT / 'site-config'
SITEMAP_TEMPLATE = CONFIG / 'sitemap.xml.template'
SITEMAP_OUTPUT = DOCS / 'sitemap.xml'
ROBOTS_TEMPLATE = CONFIG / 'robots.txt.template'
ROBOTS_OUTPUT = DOCS / 'robots.txt'
CNAME_OUTPUT = DOCS / 'CNAME'
BASE_TOKEN = '__BASE_URL__'


def normalize_base_url(raw: str) -> str:
    value = raw.strip().rstrip('/')
    parsed = urlparse(value)
    if parsed.scheme not in {'http', 'https'} or not parsed.netloc:
        raise ValueError(f'Base URL must be an absolute HTTP(S) URL, found: {raw}')
    return value


def render_template(template_path: Path, output_path: Path, *, base_url: str) -> None:
    if not template_path.exists():
        return
    content = template_path.read_text(encoding='utf-8')
    output_path.write_text(content.replace(BASE_TOKEN, base_url), encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base_url', help='Hosted public website base URL, e.g. https://example.github.io/greatcalculator-privacy')
    parser.add_argument('--cname', help='Optional custom-domain hostname to write to docs/CNAME')
    args = parser.parse_args()

    try:
        base_url = normalize_base_url(args.base_url)
    except ValueError as error:
        print(f'[FAIL] {error}')
        return 1

    render_template(SITEMAP_TEMPLATE, SITEMAP_OUTPUT, base_url=base_url)
    render_template(ROBOTS_TEMPLATE, ROBOTS_OUTPUT, base_url=base_url)

    if args.cname:
        hostname = args.cname.strip()
        if not hostname:
            print('[FAIL] --cname must not be blank when provided.')
            return 1
        CNAME_OUTPUT.write_text(hostname + '\n', encoding='utf-8')
        print(f'[PASS] Wrote {CNAME_OUTPUT.relative_to(ROOT)}')

    print(f'[PASS] Wrote {SITEMAP_OUTPUT.relative_to(ROOT)}')
    print(f'[PASS] Wrote {ROBOTS_OUTPUT.relative_to(ROOT)}')
    print('[PASS] Public URLs:')
    print(f'       Home:            {base_url}/')
    print(f'       Privacy Policy:  {base_url}/privacy/')
    print(f'       Privacy Choices: {base_url}/privacy-choices/')
    print(f'       Support:         {base_url}/support/')
    print(f'       Accessibility:   {base_url}/accessibility/')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
