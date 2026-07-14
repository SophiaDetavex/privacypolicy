#!/usr/bin/env python3
"""Validate local internal links and asset references for the Great Calculator public site."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
HTML_FILES = sorted(DOCS.rglob('*.html'))
SKIP_SCHEMES = {'http', 'https', 'mailto', 'tel', 'data'}


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if tag == 'a' and attr_map.get('href'):
            self.references.append(('href', attr_map['href']))
        elif tag in {'img', 'script'} and attr_map.get('src'):
            self.references.append(('src', attr_map['src']))
        elif tag == 'link' and attr_map.get('href'):
            self.references.append(('href', attr_map['href']))


def resolve_reference(source: Path, ref: str) -> Path | None:
    parsed = urlparse(ref)
    if parsed.scheme in SKIP_SCHEMES:
        return None
    if ref.startswith('#') or not ref:
        return None
    candidate = ref.split('#', 1)[0].split('?', 1)[0]
    if not candidate:
        return None
    if candidate.startswith('/'):
        path = DOCS / candidate.lstrip('/')
    else:
        path = (source.parent / candidate).resolve()
    return path


def main() -> int:
    missing: list[str] = []
    for html_path in HTML_FILES:
        parser = LinkCollector()
        parser.feed(html_path.read_text(encoding='utf-8'))
        for _, ref in parser.references:
            resolved = resolve_reference(html_path, ref)
            if resolved is None:
                continue
            if not resolved.exists():
                missing.append(f'{html_path.relative_to(DOCS)} -> {ref}')
    if missing:
        print('[FAIL] Missing internal references:')
        for item in missing:
            print(f'  - {item}')
        return 1
    print(f'[PASS] Validated {len(HTML_FILES)} HTML files. No broken internal relative references found.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
