#!/usr/bin/env python3
"""
Checks the shelf is still readable and the attribution still resolves.

A repository of binary files fails quietly. A truncated commit, a bad Git LFS
migration or a half-finished download leaves a file that is still present, still
roughly the right size in a listing, and no longer a document anything can open.
Nothing complains until someone clicks it.

    python scripts/check.py

Needs no third-party packages: the PDF header, trailer and page count are read
directly.

@module checks
"""

import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (compatible; resources-check)"

# Below this a PDF is a stub or a download that stopped early rather than a
# book. The smallest here is well over a megabyte.
MINIMUM_BYTES = 50_000


def pdfs():
    return sorted(p for p in ROOT.rglob("*.pdf") if ".git" not in p.parts)


def check_pdf(path):
    """Returns a list of problems with one file, empty when it is fine."""
    rel = path.relative_to(ROOT).as_posix()
    problems = []
    data = path.read_bytes()

    if len(data) < MINIMUM_BYTES:
        problems.append(f"{rel}: only {len(data)} bytes, too small to be a book")
    if not data.startswith(b"%PDF-"):
        problems.append(f"{rel}: does not start with a PDF header")
    # A complete PDF ends with %%EOF. A truncated download does not, and that is
    # the failure this whole script exists to catch.
    if b"%%EOF" not in data[-2048:]:
        problems.append(f"{rel}: no %%EOF near the end, so it looks truncated")

    pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
    if pages == 0:
        problems.append(f"{rel}: no page objects found")
    return problems, pages


def urls():
    found = set()
    for name in ("README.md", "NOTICE"):
        path = ROOT / name
        if path.exists():
            text = path.read_text(encoding="utf-8")
            found.update(re.findall(r'href="(https?://[^"]+)"', text))
            found.update(re.findall(r'\((https?://[^)]+)\)', text))
            found.update(re.findall(r'(?<![(<"])\bhttps?://[^\s<>)"]+', text))
    return sorted(u.rstrip(".,") for u in found)


def check_url(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return url, None if response.status < 400 else f"HTTP {response.status}"
    except urllib.error.HTTPError as error:
        return url, f"HTTP {error.code}"
    except Exception as error:
        return url, f"{type(error).__name__}: {error}"


def main():
    files = pdfs()
    if not files:
        print("No PDFs found, which cannot be right.", file=sys.stderr)
        return 1

    problems = []
    for path in files:
        found, pages = check_pdf(path)
        problems += found
        if not found:
            print(f"  ok  {path.relative_to(ROOT).as_posix()}  ({pages} pages, {path.stat().st_size // 1024} KB)")

    links = urls()
    print(f"checked {len(files)} PDFs and {len(links)} URLs")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for url, why in pool.map(check_url, links):
            if why:
                problems.append(f"dead link: {why}  {url}")

    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    print("all good")
    return 0


if __name__ == "__main__":
    sys.exit(main())
