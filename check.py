#!/usr/bin/env python3
"""Build check for exceptionalmedia.us. Exits non-zero on any failure.
Runs in CI before deploy — nothing ships that fails one of these."""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).parent
FILES = [f for f in sorted(ROOT.rglob("*.html"))
         if f.name != "preview.html" and "_site" not in f.parts]
fail = []

def check(name, bad, fmt=str):
    if bad:
        fail.append(name)
        print(f"  FAIL  {name}")
        for b in bad[:8]:
            print("         ", fmt(b))
    else:
        print(f"  ok    {name}")

# 1 · every internal link resolves
bad = [(f.name, m) for f in FILES for m in re.findall(r'href="(/[^"#]*)"', f.read_text())
       if not (ROOT / (m.lstrip("/") + ("index.html" if m.endswith("/") else ""))).exists()]
check("internal links resolve", bad)

# 2 · prohibited and superseded copy — Fact Ledger + Brand Standards v1.0
PROHIBITED = [
    r"mediocrity", r"reject mediocr", r"built on purpose", r"rockport", r"pegasus ranch",
    r"royalty acre", r"\$550", r"\bCEPA\b", r"\bMMP\b", r"legally blind", r"\$10T",
    r"#1 business podcast", r"hundreds of business exits", r"\bAllstate\b",
    r"132[,K]", r"212[,K]", r"\b58\+", r"\b85\+", r"prototype", r"lorem ipsum",
]
# A superseded figure may be QUOTED inside <span class="dead-figure"> so a press kit can
# tell a reporter which figure not to reprint. Everywhere else it is a failure.
DEAD = re.compile(r'<span class="dead-figure">.*?</span>', re.S)
bad = [(f.name, p) for f in FILES for p in PROHIBITED
       if re.search(p, DEAD.sub("", f.read_text()), re.I)]
check("no prohibited or superseded copy", bad)

# 3 · the email address never appears literally (see README, email obfuscation)
bad = [(f.name, m) for f in FILES
       for m in re.findall(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}|mailto:[a-zA-Z]", f.read_text(), re.I)]
check("no literal email address in source", bad)

# 4 · plural voice
bad = [(f.name, m) for f in FILES
       for m in re.findall(r'(?:^|[">.,;( ])(I am|I&rsquo;m|I&rsquo;ve|My mission)', f.read_text())]
check("plural voice — no first-person singular", bad)

# 5 · outbound links are safe and crawlable as citations
bad = [(f.name, t[:64]) for f in FILES
       for t in re.findall(r'<a [^>]*href="https?://[^"]+"[^>]*>', f.read_text())
       if 'rel="noopener"' not in t]
check("outbound links carry rel=noopener", bad)

# 6 · unique title and description per page
for label, pat in (("titles", r"<title>(.*?)</title>"),
                   ("descriptions", r'name="description" content="(.*?)"')):
    c = collections.Counter()
    for f in FILES:
        m = re.search(pat, f.read_text(), re.S)
        if not m:
            fail.append(f"missing {label}: {f.name}")
            print(f"  FAIL  {f.name} has no {label[:-1]}")
            continue
        c[m.group(1)] += 1
    check(f"unique {label}", [k for k, v in c.items() if v > 1])

# 7 · accessibility and semantics
bad = [f.name for f in FILES if '<main id="main">' not in f.read_text()]
check("every page has a <main> landmark", bad)
bad = [f.name for f in FILES if 'class="skip"' not in f.read_text()]
check("every page has a skip link", bad)
bad = [(f.name, n) for f in FILES
       for n in [len(re.findall(r"<h1[ >]", f.read_text()))] if n != 1]
check("exactly one <h1> per page", bad)
bad = [(f.name, t[:60]) for f in FILES
       for t in re.findall(r"<img [^>]*>", f.read_text()) if "alt=" not in t]
check("every <img> has alt text", bad)

bad = []
for f in FILES:
    lv = [int(m) for m in re.findall(r"<h([1-6])[ >]", f.read_text())]
    skips = [(lv[i - 1], lv[i]) for i in range(1, len(lv)) if lv[i] - lv[i - 1] > 1]
    if skips:
        bad.append((f.name, f"h{skips[0][0]} -> h{skips[0][1]}"))
check("no skipped heading levels", bad)

# 8 · social card + icons referenced everywhere
for label, needle in (("og:image", 'property="og:image"'),
                      ("favicon", 'rel="icon"'),
                      ("og:url", 'property="og:url"')):
    check(f"{label} on every page", [f.name for f in FILES if needle not in f.read_text()])

# 9 · structured data parses, where present
import json
bad = []
for f in FILES:
    for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', f.read_text(), re.S):
        try:
            json.loads(blob)
        except Exception as e:
            bad.append((f.name, str(e)[:60]))
check("JSON-LD parses", bad)

# 10 · no unevaluated f-string placeholder leaked into the output
bad = [(f.name, m) for f in FILES for m in re.findall(r"\{[a-z_]+\(.{0,60}", f.read_text())]
check("no unevaluated template placeholders", bad)

# 11 · publication status. Only Selling Main Street (2024) and Buying Main Street (2025) are
#      published. Multiple internal records wrongly say Exceptional by Design came out in
#      April 2026 — Chris confirmed 5 Sept 2026 that it is in production for Q1 2027.
#      This rule exists so that error cannot creep back in from those records.
UNPUBLISHED = ["exceptional-by-design", "exceptional-systems", "exceptional-stewardship"]
bad = []
for f in FILES:
    slug = f.parent.name
    if slug in UNPUBLISHED or (f.parent.parent.name in UNPUBLISHED):
        for m in re.findall(r'class="pill[^"]*">([^<]*)</span>', f.read_text()):
            if "Published" in m:
                bad.append((f.name, m))
check("no trilogy title is labelled Published", bad)

# 12 · canonical on every page
bad = [f.name for f in FILES if 'rel="canonical"' not in f.read_text()]
check("canonical on every page", bad)

print()
if fail:
    print(f"BUILD CHECK FAILED — {len(fail)} problem(s)")
    sys.exit(1)
print(f"BUILD CHECK PASSED — {len(FILES)} pages")
