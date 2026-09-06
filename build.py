#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exceptionalmedia.us — static site generator
Exceptional Companies Family Brand Standards v1.0 · parent treatment · Signature Gold
Run:  python3 build.py     (writes .html next to this file)
"""
import os, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://exceptionalmedia.us"
CAL  = ("https://calendar.google.com/calendar/u/0/appointments/schedules/"
        "AcZssZ0lRYzYVtOZlBxL8FrS3IrWsInoShILlJUsQWQpGrOSnfxXYEThZuUl8WbHbmAtXShNOvV_q5Lb")

FONTS = ("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300;400;600"
         "&family=Quattrocento:wght@400;700&family=Roboto:wght@300;400;500&display=swap")

# ══════════════════════════════════════════════════════════════════════════
# MAGAZINE PROMOTION SWITCH
# EXCEPTIONAL has five open blockers (see claude/EXCEPTIONAL_Session_Handoff.md) and
# Issues 02-04 have never been adversarially fact-checked. Chris ruled Sept 5: the page
# ships and stays reachable, but nothing points traffic at it yet.
# Flip this to True and rebuild to restore the nav item, the footer link, the home
# call-to-action, the sitemap entry, and indexing. One switch, five places.
MAGAZINE_PROMOTED = False

NAV = ([("/books/", "Books"), ("/podcasts/", "Podcasts")]
       + ([("/magazine/", "Magazine")] if MAGAZINE_PROMOTED else [])
       + [("/press/", "Press"), ("/about/", "About")])

MAG_FOOT = '<a href="/magazine/">EXCEPTIONAL magazine</a>' if MAGAZINE_PROMOTED else ""

def head(title, desc, path, depth, schema=None):
    a = "../" * depth if depth else ""
    ld = ""
    if schema:
        import json as _json
        ld = ('\n<script type="application/ld+json">'
              + _json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
              + "</script>")
    nav = "\n".join(
        '      <a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == path or (path.startswith(h) and h != "/") else "", t)
        for h, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Exceptional Media">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/assets/og-exceptional-media.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Exceptional Media — Designed for exceptional. Life. Business. Wealth.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/assets/og-exceptional-media.png">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#000000">{"" if (MAGAZINE_PROMOTED or path != "/magazine/") else chr(10) + "<!-- Unpromoted until the EXCEPTIONAL blockers clear. See MAGAZINE_PROMOTED in build.py. -->" + chr(10) + chr(60) + "meta name=" + chr(34) + "robots" + chr(34) + " content=" + chr(34) + "noindex, follow" + chr(34) + chr(62)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/assets/exco-media.css">{ld}
</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<header class="masthead">
  <div class="bar"></div>
  <div class="inner">
    <!-- Typographic lockup. No authored vector mark exists yet (README, open item 1).
         When the SVG arrives, replace this <a> block with an inline SVG at 0.5X clear space. -->
    <a class="lockup" href="/" aria-label="Exceptional Media — home">
      <span class="m1">EXCEPTIONAL</span>
      <span class="m2">MEDIA</span>
    </a>
    <nav class="nav" aria-label="Primary">
{nav}
    </nav>
  </div>
</header>

<main id="main">
"""

FOOT = f"""
</main>

<footer class="foot">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="tag">DESIGNED FOR EXCEPTIONAL.<i>LIFE. BUSINESS. WEALTH.</i></div>
        <p class="small mt3" style="color:rgba(255,255,255,.7);max-width:38ch">
          We are the publishing arm of Exceptional Companies &mdash; an innovation company that
          uses business as the platform to change the status quo. We are builders. Operators.
          Thought leaders. Integrating life, wealth, and business. We stress-test our knowledge
          across industries and asset classes &mdash; learning as we go, and sharing it with
          everyone who will listen.</p>
      </div>
      <div>
        <h2>Publications</h2>
        <a href="/books/">Books</a>
        <a href="/books/exceptional-by-design/excerpt/">Read chapter four</a>
        <a href="/podcasts/">Podcasts</a>
        {MAG_FOOT}
        <a href="/press/">Press &amp; rights</a>
      </div>
      <div>
        <h2>The family</h2>
        <a href="https://exceptionalcos.com" rel="noopener">Exceptional Companies</a>
        <a href="https://excoadvisors.com" rel="noopener">Exceptional Business Advisors</a>
        <a href="https://www.exceptionalwealth.us" rel="noopener">Exceptional Wealth &amp; Family Office</a>
        <a href="https://insureexceptional.com" rel="noopener">Exceptional Insurance</a>
        <a href="https://chrisseegers.com" rel="noopener">Chris Seegers</a>
        <a href="https://taraseegers.com" rel="noopener">Tara Seegers</a>
      </div>
      <div>
        <h2>Listen &amp; read</h2>
        <a href="https://www.youtube.com/@ExceptionalCompaniesPodcast" rel="noopener">Exceptional Companies Podcast</a>
        <a href="https://www.youtube.com/@ColoradoBusinessPodcast" rel="noopener">Colorado Business Podcast</a>
        <a href="https://exceptional-os.com" rel="noopener">Exceptional Life OS</a>
        <a href="https://townofhillside.com" rel="noopener">Town of Hillside</a>
        <a href="https://discoversoco.com" rel="noopener">Discover SoCo</a>
      </div>
    </div>
    <div class="rule"></div>
    <div class="fine">
      <span>&copy; 2026 Exceptional Companies. Colorado Springs &middot; Austin &middot; Midland.</span>
      <span><a class="mail" id="contact-email" data-u="info" data-d="exceptionalcos.com" data-show="1" href="#contact-email" style="display:inline">info [at] exceptionalcos [dot] com</a></span>
    </div>
  </div>
</footer>

<script>
/* Assembles every .mail address at runtime. The literal string never appears in
   the served HTML, so source scrapers and regex harvesters come up empty. */
(function () {{
  var n = document.getElementsByClassName('mail');
  for (var i = 0; i < n.length; i++) {{
    var e = n[i], u = e.getAttribute('data-u'), d = e.getAttribute('data-d');
    if (!u || !d) continue;
    var addr = u + String.fromCharCode(64) + d, sub = e.getAttribute('data-s');
    e.setAttribute('href', 'mailto:' + addr + (sub ? '?subject=' + sub : ''));
    if (e.getAttribute('data-show')) e.textContent = addr;
  }}
}})();
</script>

</body>
</html>
"""

# ══════════════════════════════════════════════════════════════════════════
# Email — never written literally into the HTML.
# The user and domain travel as separate data attributes; the footer script
# assembles them at runtime. Defeats source scrapers and regex harvesters, not
# a determined headless-browser harvester. See README, "Email obfuscation".
# ══════════════════════════════════════════════════════════════════════════
MAIL_U = "info"
MAIL_D = "exceptionalcos.com"
MAIL_PLAIN = "info [at] exceptionalcos [dot] com"   # no-JS fallback, human-readable

def mail(label=None, subject=None, cls=None, style=None):
    """A link that becomes mailto: on load. label=None shows the address itself.
    Without JS it jumps to the footer, where the address is printed in the [at] form."""
    a = ['class="mail%s"' % ((" " + cls) if cls else ""),
         'data-u="%s"' % MAIL_U, 'data-d="%s"' % MAIL_D,
         'href="#contact-email"']
    if subject: a.append('data-s="%s"' % subject)
    if label is None: a.append('data-show="1"')
    if style: a.append('style="%s"' % style)
    return '<a %s>%s</a>' % (" ".join(a), label if label else MAIL_PLAIN)


# ══════════════════════════════════════════════════════════════════════════
# Tables of contents — transcribed from the manuscripts, not summarised.
#   Exceptional by Design : Exceptional_by_Design_4-13-26.docx (final)
#   Exceptional Systems   : Exceptional_Systems_Redline_Spec.docx, "New Table of
#                           Contents (Locked)". The book is mid-revision — this
#                           structure is locked but the text is not. CLEARANCE
#                           REQUIRED before this page goes public. README item 11.
# ══════════════════════════════════════════════════════════════════════════

TOC_EBD = [
  ("Front matter", None, ["How This Book Maps to Your Life OS &mdash; The Four Phases",
                          "Introduction: The Day Everything Changed"]),
  ("Phase one", "Dream It", [
      "1 &middot; Getting Clear &mdash; You Must Be Clear to Get There",
      "2 &middot; Define Your Life Purpose",
      "3 &middot; Assess Your Current Reality",
      "4 &middot; Create Your Life Vision",
      "5 &middot; Set Your North Star Goals",
      "6 &middot; Turn Vision Into Strategy"]),
  ("Phase two", "Build It", [
      "7 &middot; Design Your Weekly Success Systems",
      "8 &middot; Build Your Daily Disciplines",
      "9 &middot; Master Your Time",
      "10 &middot; Create Financial Freedom",
      "11 &middot; Build Your Dream Team"]),
  ("Phase three", "Optimize It", [
      "12 &middot; Navigate Obstacles and Setbacks",
      "13 &middot; Measure What Matters",
      "14 &middot; The Art of Iteration"]),
  ("Phase four", "Live It", [
      "15 &middot; Cultivate Gratitude and Presence",
      "16 &middot; Serve Something Bigger",
      "17 &middot; Leave a Legacy, the Right Way"]),
  ("Back matter", None, ["Conclusion: Your Exceptional Life Awaits",
                         "Appendix: The Tools That Make It Real",
                         "Appendix C: The 30-Day Kickstart Guide"]),
]

TOC_SYS = [
  ("Front matter", None, ["Introduction",
                          "How This Book Connects to Exceptional by Design and Selling Main Street"]),
  ("Part one", "Dream It", [
      "1 &middot; Define Your Guiding Principles",
      "2 &middot; Craft Your Purpose Statement",
      "3 &middot; Tell Your Story",
      "4 &middot; Cast Your Vision"]),
  ("Part two", "Build It", [
      "5 &middot; Set Your Strategy",
      "6 &middot; Install Cadence and Scorecards",
      "7 &middot; Build Your Team"]),
  ("Part three", "Optimize It", [
      "8 &middot; Document Your Systems",
      "9 &middot; Solve Obstacles",
      "10 &middot; Capture and Score Opportunities",
      "11 &middot; Run the Exceptional Business Loop"]),
  ("Part four", "Monetize It", [
      "12 &middot; Know Your Business Exit Valuation",
      "13 &middot; Integrate Your Personal Plan",
      "14 &middot; Build Your Wealth Plan",
      "15 &middot; Plan Your Exit and Transition"]),
  ("Back matter", None, ["Conclusion: Your Business as Ministry",
                         "The 90-Day Challenge",
                         "Books That Shaped This System"]),
]

def toc(data):
    out = []
    for label, phase, items in data:
        head = ('<div class="tocphase"><span class="p">%s</span>%s</div>'
                % (label, ('<span class="n">%s</span>' % phase) if phase else ""))
        rows = "".join('<li>%s</li>' % i for i in items)
        out.append('<div class="tocgroup">%s<ul class="toclist">%s</ul></div>' % (head, rows))
    return '<div class="toc">%s</div>' % "".join(out)

# ── Endorsements. The component is built; no endorsement exists in any source yet,
#    and one is not inventable. Populate the list and it renders. README item 12.
ENDORSEMENTS = {}   # slug -> [(quote, name, title), ...]

def endorsements(slug):
    rows = ENDORSEMENTS.get(slug)
    if not rows: return ""
    cards = "".join(
      '<blockquote class="pull"%s>%s<cite>%s &mdash; %s</cite></blockquote>'
      % (' style="color:#fff"' if False else "", q, n, t) for q, n, t in rows)
    return ('<section class="section section--rule"><div class="wrap">'
            '<div class="eyebrow">Praise</div><div class="grid g2 mt4">%s</div></div></section>' % cards)

def bulk(title, kit=None):
    """Bulk / institutional order block, plus the route to the press desk — a reviewer
    landing straight on a book page should not have to go hunting for it.
    mail() is called here, not embedded as text: an f-string does not evaluate
    placeholders in a value it interpolates."""
    link = mail("Start a bulk order",
                subject="Bulk%20order%20%E2%80%94%20" + title.replace(" ", "%20"),
                cls="go")
    return f"""
<section class="section section--rule">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">For teams, cohorts and events</div>
        <h2 class="h2 mt2">Buying it by the case</h2>
        <hr class="accentrule mt3">
        <p class="mt3">We ship <i>{title}</i> in quantity for leadership teams, masterminds,
          conferences and client gifts, and we discount at volume. Tell us the count, the date you
          need them by, and where they are going.</p>
        <p>We also license the frameworks for cohort and classroom use, and we will send an
          examination copy to anyone teaching from it.</p>
      </div>
      <div>
        <div class="card">
          <div class="kicker">Direct</div>
          <div class="title">Bulk and institutional orders</div>
          <p>Twenty-five copies or two thousand. Same address either way.</p>
          {link}
        </div>
        <p class="small mt3">Writing about this book? The
          <a href="{kit or '/press/'}">{'press kit for this title' if kit else 'press desk'}</a>
          has descriptions at three lengths, the author bios, interview questions and asset
          requests.</p>
      </div>
    </div>
  </div>
</section>
"""


# ══════════════════════════════════════════════════════════════════════════
# Structured data. Search and answer engines cannot infer that five books, two
# shows and a magazine belong to one publisher from prose alone — the Sept audit's
# finding for EBA was "attribution, not effort," and this is the fix for it here.
# Only facts that already appear on the page go in. No figures, no counts.
# ══════════════════════════════════════════════════════════════════════════

ORG = {
  "@type": "Organization",
  "@id": SITE + "/#org",
  "name": "Exceptional Media",
  "url": SITE,
  "description": "The publishing arm of Exceptional Companies — books, podcasts and "
                 "EXCEPTIONAL magazine.",
  "parentOrganization": {"@type": "Organization", "name": "Exceptional Companies",
                         "url": "https://exceptionalcos.com"},
  "address": {"@type": "PostalAddress", "addressLocality": "Colorado Springs",
              "addressRegion": "CO", "addressCountry": "US"},
  "sameAs": ["https://exceptionalcos.com", "https://excoadvisors.com",
             "https://www.exceptionalwealth.us", "https://insureexceptional.com",
             "https://chrisseegers.com",
             "https://www.youtube.com/@ExceptionalCompaniesPodcast",
             "https://www.youtube.com/@ColoradoBusinessPodcast"],
}

CHRIS = {"@type": "Person", "name": "Chris Seegers", "url": "https://chrisseegers.com"}
TARA  = {"@type": "Person", "name": "Tara Seegers"}
MARCUS = {"@type": "Person", "name": "Marcus Seegers"}

def crumbs(*pairs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
        for i, (n, u) in enumerate(pairs)]}

def book_ld(name, authors, url, published=None, isbn=None, buy=None, about=None):
    b = {"@type": "Book", "name": name, "author": authors, "url": SITE + url,
         "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-US"}
    if published: b["datePublished"] = published
    if isbn: b["isbn"] = isbn
    if about: b["about"] = about
    if buy: b["workExample"] = {"@type": "Book", "bookFormat": "https://schema.org/Paperback",
                                "url": buy}
    return b

def graph(*nodes):
    return {"@context": "https://schema.org", "@graph": list(nodes)}


def write(path, title, desc, body, depth=0, schema=None):
    out = ROOT / (path.lstrip("/") + ("index.html" if path.endswith("/") else ""))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head(title, desc, path, depth, schema) + body + FOOT, encoding="utf-8")
    print("  wrote", out.relative_to(ROOT))

# ══════════════════════════════════════════════════════════════════════════
# Shared components
# ══════════════════════════════════════════════════════════════════════════

def pagehead(eyebrow, h1, lead, dark="pagehead"):
    return f"""
<section class="{dark}">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="eyebrow">{eyebrow}</div>
    <h1 class="display mt2">{h1}</h1>
    <hr class="accentrule wide mt3">
    <p class="lead mt3">{lead}</p>
  </div>
</section>
"""

def cover(title_lines, sub, gold=False):
    cls = "energy energy--gold" if gold else "energy"
    t = "<br>".join(title_lines)
    return f"""<div class="coverframe">
        <div class="{cls}" aria-hidden="true"></div>
        <!-- Drop the real jacket here when art exists:  <img src="/assets/covers/xxx.jpg" alt=""> -->
        <div class="cv"><div class="t">{t}</div><div class="s">{sub}</div></div>
      </div>"""

BOOKS = [
    dict(slug="exceptional-by-design", t="Exceptional by Design", os="Installs the Exceptional Life OS",
         authors="Chris Seegers and Tara Seegers", status="soon",
         statlbl="Q1 2027", yr="2027", when="Anticipated Q1 2027",
         blurb="The blueprint for designing a life on purpose &mdash; eight pillars, four phases, "
               "and the assessment that tells you where you actually stand.",
         cov=["EXCEPTIONAL","BY DESIGN"]),
    dict(slug="exceptional-systems", t="Exceptional Systems", os="Installs the Exceptional Business OS",
         authors="Chris Seegers and Marcus Seegers", status="soon", statlbl="Q4 2027",
         yr="2027", when="Anticipated Q4 2027",
         blurb="A business that runs on documentation and discipline instead of heroic effort "
               "and tribal knowledge. Dream it, build it, optimize it, monetize it.",
         cov=["EXCEPTIONAL","SYSTEMS"]),
    dict(slug="exceptional-stewardship", t="Exceptional Stewardship", os="Installs the Exceptional Wealth OS",
         authors="Tara Seegers and Chris Seegers", status="soon", statlbl="Q2 2028",
         yr="2028", when="Anticipated Q2 2028",
         blurb="The third book completes the trilogy: what happens to money once it arrives, "
               "how it works, and how to leave it well.",
         cov=["EXCEPTIONAL","STEWARDSHIP"]),
]

MAIN_STREET = [
    dict(t="Selling Main Street", yr="2024", author="Chris Seegers",
         d="The primer for owners preparing to sell &mdash; the philosophy of exit planning, the "
           "mistakes sellers make, and how to assemble a transition team.",
         url="https://www.amazon.com/dp/B0D2B72W18", cta="Amazon"),
    dict(t="Buying Main Street", yr="2025", author="Chris Seegers",
         d="The buy-side companion. Written for acquisition entrepreneurs &mdash; the capable "
           "buyers who can carry on what a retiring owner spent thirty years building.",
         url="https://www.amazon.com/dp/195787029X", cta="Amazon"),
]

def bookcard(b, base="/books/"):
    pill = {"out":'<span class="pill pill--out">%s</span>',
            "soon":'<span class="pill pill--soon">%s</span>'}[b["status"]] % b["statlbl"]
    return f"""<a class="card" href="{base}{b['slug']}/">
      <div class="kicker">{b['os']}</div>
      <div class="title">{b['t']}</div>
      <div class="meta">{b['authors']}</div>
      <p>{b['blurb']}</p>
      <div class="mt1">{pill}</div>
      <div class="meta">{b.get('when','')}</div>
      <span class="go">Read more &rsaquo;</span>
    </a>"""

# ══════════════════════════════════════════════════════════════════════════
# PER-BOOK PRESS KITS  —  /books/<slug>/press/
#
# The site already had a page per book. What it did not have is what a journalist
# does when they land on one. These pages carry the descriptions at three lengths
# for lifting verbatim, the ratified author bios, cold-read interview questions,
# and — critically — the live capital figure.
#
# That last one is the point. Chris_Seegers_Author_Bio_Standard.md (3 Sept) killed
# two figures still sitting in print: "over a Billion" in the Exceptional by Design
# manuscript and "over $550 million" in Selling Main Street. A reporter with no
# other source will reprint whichever they find. This page is where they find the
# right one first.
#
# Only two kits exist. Exceptional Stewardship has no manuscript, and a thin press
# page ranks worse than no page at all. It gets one when there is something in it.
# ══════════════════════════════════════════════════════════════════════════

BIO_CHRIS_LONG = """Chris Seegers is a business owner with a long track record of starting and
buying companies and building them into successful, self-governed entities. He founded
Exceptional Companies, an innovation company. He is an active owner in many different businesses,
and has served on leadership teams that have raised and deployed over $750 million in investor capital.
Chris is a &ldquo;capitalist missionary,&rdquo; and his heart is activating and equipping others
to live exceptional lives.</p><p>Chris is a follower of Jesus, husband to his best friend Tara,
and father to Jed, Chisum, and Lillian. He is a sibling to seven, and loves deep, authentic
friendships and old books. Chris and his family live in Colorado Springs surrounded by mountains
and amazing people."""

BIO_CHRIS_SHORT = """Chris Seegers founded Exceptional Companies, an innovation company, and has served
on leadership teams that raised and deployed over $750 million in investor capital. A
self-described &ldquo;capitalist missionary,&rdquo; he lives in Colorado Springs with his wife and
co-author Tara and their three children."""

BIO_TARA_LONG = """Tara Seegers is a nationally recognized wealth advisor and Certified Financial
Planner&trade; who serves multi-generational families and business owners across the United
States. Named to Forbes&rsquo; &ldquo;Top Women Wealth Advisors Best-In-State&rdquo; list, Tara
specializes in creating clarity from complexity and helping families build legacies that last for
generations.</p><p>Tara is a follower of Jesus, wife to Chris, and mother to Jed, Chisum, and
Lillian. She believes exceptional wealth planning starts with understanding what truly matters.
Tara and her family live in Colorado Springs, where they&rsquo;re designing an exceptional life
together."""

BIO_MARCUS = """Marcus Seegers is co-author of <i>Exceptional Systems</i> and co-leader of the
Exceptional Companies ecosystem. He is a Co-Founder of Exceptional Business Advisors, where he
owns operations and systems &mdash; running, in a real company with real people in it, the
operating system this book documents."""

def presskit(slug, title, subtitle, authors, when, d25, d50, d150, contains, questions,
             bios, prev_url, prev_label):
    # mail() is called here and its output interpolated. An f-string does not evaluate
    # placeholders inside a value it interpolates — this is the second time that bit.
    t_enc = title.replace(" ", "%20")
    cta_press = mail("Request assets or an interview",
                     subject="Press%20%E2%80%94%20" + t_enc, cls="btn")
    cta_assets = mail("Request assets",
                      subject="Asset%20request%20%E2%80%94%20" + t_enc, cls="btn")
    addr = mail()
    ask = "".join('<div class="factrow"><span class="k">%02d</span><span>%s</span></div>'
                  % (i + 1, q) for i, q in enumerate(questions))
    cont = "".join('<div class="factrow"><span class="k">%s</span><span>%s</span></div>' % (k, v)
                   for k, v in contains)
    biohtml = "".join(
        '<div class="mt4"><div class="eyebrow">%s &mdash; %s</div>'
        '<div class="body mt2"><p>%s</p></div></div>' % (n, l, t) for n, l, t in bios)
    return f"""
<section class="pagehead">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="eyebrow">Press kit</div>
    <h1 class="display mt2">{title}</h1>
    <hr class="accentrule wide mt3">
    <p class="lead mt3">Everything a writer, producer or bookseller needs, in a form you can lift
      without calling us first. If you need something that is not here, ask &mdash; we answer the
      same day.</p>
    <div class="btnrow mt4">
      {cta_press}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">At a glance</div>
        <h2 class="h2 mt2">The facts</h2>
        <hr class="accentrule mt3">
        <div class="mt3">
          <div class="factrow"><span class="k">Title</span><span>{title}</span></div>
          <div class="factrow"><span class="k">Subtitle</span><span>{subtitle}</span></div>
          <div class="factrow"><span class="k">Authors</span><span>{authors}</span></div>
          <div class="factrow"><span class="k">Publisher</span><span>Exceptional Media, Colorado Springs</span></div>
          <div class="factrow"><span class="k">Publication</span><span>{when}</span></div>
          <div class="factrow"><span class="k">ISBN</span><span>On request &mdash; assigned closer to publication</span></div>
          <div class="factrow"><span class="k">Formats</span><span>On request</span></div>
          <div class="factrow"><span class="k">Review copies</span><span>Available on request ahead of publication</span></div>
          <div class="factrow"><span class="k">Contact</span><span>{addr}</span></div>
        </div>
      </div>
      <div>
        <div class="card card--dark">
          <div class="kicker">Please read this before you write</div>
          <div class="title">One capital figure is live. Two are dead.</div>
          <p>The only figure to use is <b style="font-weight:500">over $750 million in investor
            capital</b>, raised and deployed by leadership teams Chris served on.</p>
          <p>Two older figures are still sitting in print and in retail listings and should not be
            repeated: <span class="dead-figure"><i>&ldquo;over a Billion dollars&rdquo;</i> and
            <i>&ldquo;over $550 million&rdquo;</i></span>. Both are superseded. We are correcting the
            listings; if you found one of them, it came from there.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="eyebrow">Lift these verbatim</div>
    <h2 class="h1 mt2">Descriptions,<br>three lengths.</h2>
    <hr class="accentrule mt3">
    <div class="grid g3 grid--top mt4">
      <div class="card card--dark"><div class="kicker">25 words</div><p>{d25}</p></div>
      <div class="card card--dark"><div class="kicker">50 words</div><p>{d50}</p></div>
      <div class="card card--dark"><div class="kicker">150 words</div><p>{d150}</p></div>
    </div>
    <p class="small mt3">No attribution needed. These are written to be used as they are.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Get it right</div>
        <h2 class="h2 mt2">What is actually in the book</h2>
        <hr class="accentrule mt3">
        <div class="mt3">{cont}</div>
        <p class="small mt3">The full table of contents is on the
          <a href="{prev_url}">{prev_label}</a>.</p>
      </div>
      <div>
        <div class="eyebrow">For hosts and interviewers</div>
        <h2 class="h2 mt2">Five questions you can ask cold</h2>
        <hr class="accentrule mt3">
        <div class="mt3">{ask}</div>
        <p class="small mt3">Use them, change them, ignore them. They are here so you do not have
          to read the book to run a good interview &mdash; though we hope you do.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--rule">
  <div class="wrap">
    <div class="eyebrow">Author biographies</div>
    <h2 class="h2 mt2">Set these as written</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">Ratified September 2026. They supersede the &ldquo;About the
      Authors&rdquo; copy in any earlier manuscript or retail listing.</p>
    {biohtml}
  </div>
</section>

<section class="section section--deep">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Assets</div>
        <h2 class="h2 mt2">Covers, photography, logos</h2>
        <hr class="accentrule mt3">
        <p class="mt3" style="color:rgba(255,255,255,.86)">Jacket art, author photography and the
          Exceptional wordmark are all available in print resolution on request. Marks are supplied
          as vector and used solid black or solid white only &mdash; never recoloured, boxed,
          stretched, or pulled from a web page.</p>
      </div>
      <div>
        <div class="btnrow">
          {cta_assets}
          <a class="btn btn--ghost" href="{prev_url}">The book page</a>
        </div>
        <p class="small mt3" style="color:rgba(255,255,255,.7)">Covering the trilogy as a whole?
          The <a href="/press/">press desk</a> handles rights, permissions and excerpts across
          every title.</p>
      </div>
    </div>
  </div>
</section>
"""


# ══════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════
home = f"""
<section class="hero">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="eyebrow">Exceptional Media &middot; Colorado Springs</div>
    <h1 class="display mt3">Published.</h1>
    <hr class="accentrule wide mt4">
    <p class="lead mt4">Books, tools, podcasts, and a quarterly magazine for people in pursuit of
      exceptional.</p>
    <div class="herotag mt3">Life. Business. Wealth.</div>
    <div class="btnrow mt4">
      <a class="btn" href="/books/">The books</a>
      <a class="btn btn--ghost" href="https://exceptional-os.com" rel="noopener" target="_blank">The tools</a>
      <a class="btn btn--ghost" href="/podcasts/">The shows</a>
    </div>
  </div>
</section>

<!-- Exceptional Insurance is named at the level its own site states: personal lines, and the
     key person and buy-sell cover that makes a business transferable. No product claim, no
     coverage advice. If a disclosure is required, it goes here. See README, open item 9. -->
<section class="section section--tight section--rule">
  <div class="wrap">
    <div class="eyebrow">Where the material comes from</div>
    <p class="lead mt2">Nothing here is theory. Every framework and tool we publish was designed
      and refined inside real businesses we grew before it was written down for you.</p>
    <div class="grid g4 mt4">
      <div>
        <div class="eyebrow"><a href="https://excoadvisors.com" rel="noopener" target="_blank" style="color:inherit;border-bottom-color:var(--rule)">Exceptional Business Advisors</a></div>
        <p class="small mt1" style="color:var(--ink)">Sell-side and buy-side transition work. The
          Main Street books came straight out of it.</p>
      </div>
      <div>
        <div class="eyebrow"><a href="https://www.exceptionalwealth.us" rel="noopener" target="_blank" style="color:inherit;border-bottom-color:var(--rule)">Exceptional Wealth &amp; Family Office</a></div>
        <p class="small mt1" style="color:var(--ink)">What happens to the family, the plan and the
          legacy after the wire hits &mdash; utilizing your resources to live the life you
          design.</p>
      </div>
      <div>
        <div class="eyebrow"><a href="https://insureexceptional.com" rel="noopener" target="_blank" style="color:inherit;border-bottom-color:var(--rule)">Exceptional Insurance</a></div>
        <p class="small mt1" style="color:var(--ink)">Protection for all of it &mdash; home, auto,
          umbrella. Plus the life, estate, key person and buy-sell coverage that can turn an
          exit into opportunity.</p>
      </div>
      <div>
        <div class="eyebrow"><a href="https://exceptionalcos.com" rel="noopener" target="_blank" style="color:inherit;border-bottom-color:var(--rule)">Exceptional Companies</a></div>
        <p class="small mt1" style="color:var(--ink)">An Innovation Company: the operating portfolio
          where the systems get stress-tested across industries and our own resources are
          deployed to live the life we designed.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">The trilogy</div>
    <h2 class="h1 mt2">Three operating systems.<br>One life.</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">Most owners define a plan for one of these and improvise the other
      two. The trilogy treats life, business, and wealth as a single design, because they
      move together whether you planned it or not.</p>
    <div class="grid g3 mt4">
      {bookcard(BOOKS[0])}
      {bookcard(BOOKS[1])}
      {bookcard(BOOKS[2])}
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Also from Exceptional Media</div>
        <h2 class="h2 mt2">The Main Street books</h2>
        <hr class="accentrule mt3">
        <p class="lead mt3">Two books about the single largest transaction most business owners
          will ever make &mdash; one written for the person selling, one for the person buying.</p>
      </div>
      <div class="grid">
        {"".join('''<div class="card card--dark">
          <div class="kicker">%s</div>
          <div class="title">%s</div>
          <div class="meta">%s</div>
          <p>%s</p>
          <a class="go" href="%s" rel="noopener" target="_blank">%s &rsaquo;</a>
        </div>''' % (b["yr"], b["t"], b["author"], b["d"], b["url"], b["cta"]) for b in MAIN_STREET)}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">On air</div>
        <h2 class="h1 mt2">Two shows,<br>every week.</h2>
        <hr class="accentrule mt3">
        <p class="lead mt3">One is about buying, selling, and optimizing companies. The other is
          about the people building them in Colorado. Both are conversations, not interviews.</p>
        <div class="btnrow mt4"><a class="btn btn--ghost" href="/podcasts/">All listening links</a></div>
      </div>
      <div class="grid">
        <div class="card">
          <div class="kicker">Host &middot; Chris Seegers</div>
          <div class="title">Exceptional Companies Podcast</div>
          <p>Buying, selling, and optimizing businesses &mdash; and what faith has to do with any of it.</p>
          <div class="chips">
            <a class="chip" href="https://podcasts.apple.com/us/podcast/exceptional-companies-podcast/id1765569160" rel="noopener" target="_blank">Apple</a>
            <a class="chip" href="https://open.spotify.com/show/5JzPgkrevSMZCFWsXkglJv" rel="noopener" target="_blank">Spotify</a>
            <a class="chip" href="https://www.youtube.com/@ExceptionalCompaniesPodcast" rel="noopener" target="_blank">YouTube</a>
          </div>
        </div>
        <div class="card">
          <div class="kicker">Colorado Springs &middot; weekly</div>
          <div class="title">Colorado Business Podcast</div>
          <p>The entrepreneurs, operators, and changemakers building the Colorado business community.</p>
          <div class="chips">
            <a class="chip" href="https://podcasts.apple.com/us/podcast/colorado-business-podcast/id1492740546" rel="noopener" target="_blank">Apple</a>
            <a class="chip" href="https://open.spotify.com/show/1jSQ8OQSi0rprCcxTGx0KB" rel="noopener" target="_blank">Spotify</a>
            <a class="chip" href="https://www.youtube.com/@ColoradoBusinessPodcast" rel="noopener" target="_blank">YouTube</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--deep">
    <div class="wrap" style="position:relative;z-index:2">
    <div class="split">
      <div>
        <div class="eyebrow">In print</div>
        <h2 class="h1 mt2">EXCEPTIONAL.</h2>
        <hr class="accentrule mt3">
        <p class="lead mt3">A quarterly magazine for Main Street owners and the advisors around
          them. One article per vertical, every issue: Life, Business, Wealth.</p>
        <p class="small mt3">Published by Exceptional Companies, jointly serving Exceptional Business
          Advisors, Exceptional Wealth &amp; Family Office, and Exceptional Insurance.</p>
        {'<div class="btnrow mt4"><a class="btn" href="/magazine/">Inside the magazine</a></div>'
          if MAGAZINE_PROMOTED else
          '<p class="small mt3" style="color:rgba(255,255,255,.6)">Issue 01, Fall 2026.</p>'}
      </div>
      <div>
        <blockquote class="pull" style="border-left-color:var(--accent);color:#fff">
          Making the complex simple. Every article provides clarity &mdash; and calls out
          conventional advice when it doesn&rsquo;t make sense.
          <cite>Editorial standard no. 4</cite>
        </blockquote>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">Elsewhere</div>
    <h2 class="h2 mt2">Where our work shows up</h2>
    <hr class="accentrule mt3">
    <div class="grid g4 mt4">
      <a class="card" href="/press/">
        <div class="kicker">This site</div>
        <div class="title">Press, rights &amp; permissions</div>
        <p>Review copies, excerpt and reprint requests, cover art, and author availability for
          the books and the magazine.</p>
        <span class="go">Press desk &rsaquo;</span>
      </a>
      <a class="card" href="https://chrisseegers.com/press" rel="noopener" target="_blank">
        <div class="kicker">chrisseegers.com</div>
        <div class="title">Press &amp; podcast kit</div>
        <p>For producers and bookers: headshots, the cold-read bio, topics, and past appearances.</p>
        <span class="go">Booking kit &rsaquo;</span>
      </a>
      <a class="card" href="https://excoadvisors.com" rel="noopener" target="_blank">
        <div class="kicker">excoadvisors.com</div>
        <div class="title">Exceptional Business Advisors</div>
        <p>The advisory firm the Main Street books came out of &mdash; guides, not brokers.</p>
        <span class="go">The firm &rsaquo;</span>
      </a>
      <a class="card" href="https://www.exceptionalwealth.us" rel="noopener" target="_blank">
        <div class="kicker">exceptionalwealth.us</div>
        <div class="title">Exceptional Wealth &amp; Family Office</div>
        <p>The wealth management firm that turns a transaction into a plan that fuels your
          passion and gives you the roadmap to live the life you want.</p>
        <span class="go">Visit &rsaquo;</span>
      </a>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Connect</div>
        <h2 class="h1 mt2">Talk to us.</h2>
        <hr class="accentrule mt3">
        <p class="lead mt3">Bulk orders, speaking, licensing one of our frameworks for your team, or
          a conversation about your own exit. Start with us here.</p>
      </div>
      <div>
        <div class="btnrow">
          <a class="btn" href="{CAL}" rel="noopener" target="_blank">Book a conversation</a>
          {mail("Email us", cls="btn btn--ghost")}
        </div>
        <p class="small mt3">Colorado Springs &middot; Austin &middot; Midland</p>
      </div>
    </div>
  </div>
</section>
"""
write("/", "Exceptional Media — Books, Podcasts &amp; the EXCEPTIONAL Magazine",
      "Exceptional Media is the publishing arm of Exceptional Companies: the Life, Business and "
      "Wealth OS trilogy launching 2027, the Main Street books, two weekly podcasts, and "
      "EXCEPTIONAL magazine.",
      home, schema=graph(
        ORG,
        {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE, "name": "Exceptional Media",
         "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-US"}))

# ══════════════════════════════════════════════════════════════════════════
# BOOKS INDEX
# ══════════════════════════════════════════════════════════════════════════
books = pagehead("Books", "The Library",
  "Five titles. Three of them focus on life, business, and wealth as a single design "
  "integration opportunity. Two of them are about the transaction at the end.") + f"""
<section class="section">
  <div class="wrap">
    <div class="eyebrow">The trilogy</div>
    <h2 class="h1 mt2">Life. Business. Wealth.</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">Nothing in these books is theory. Our team battle-tested every system in
      them &mdash; building an exceptional life, an exceptional business and exceptional wealth
      inside our own companies, on our own money, before a word of it went on a page.</p>
    <p class="lead mt2">The books are the introduction. The operating systems are what carry it
      through.</p>
    <p class="lead mt2">Anticipated: <i>Exceptional by Design</i> Q1 2027,
      <i>Exceptional Systems</i> Q4 2027, <i>Exceptional Stewardship</i> Q2 2028. Chapter four of
      the first is already <a href="/books/exceptional-by-design/excerpt/">up in full</a>.</p>
    <div class="grid g3 mt4">
      {"".join(bookcard(b) for b in BOOKS)}
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="eyebrow">The Main Street books</div>
    <h2 class="h1 mt2">Both sides of the table.</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">Written out of the advisory firm. One for the owner who is selling
      the thing they built. One for the buyer who intends to carry it on.</p>
    <div class="grid g2 mt4">
      {"".join('''<div class="card card--dark">
        <div class="kicker">Published &middot; %s</div>
        <div class="title">%s</div>
        <div class="meta">%s</div>
        <p>%s</p>
        <a class="go" href="%s" rel="noopener" target="_blank">Find it on %s &rsaquo;</a>
      </div>''' % (b["yr"], b["t"], b["author"], b["d"], b["url"], b["cta"]) for b in MAIN_STREET)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Try one first</div>
        <h2 class="h2 mt2">Read a chapter before you buy anything</h2>
        <hr class="accentrule mt3">
        <p class="mt3">Chapter four of <i>Exceptional by Design</i> is up in full &mdash; getting
          quiet enough to hear what you actually want, then the ten-year exercise that puts it on
          paper. Not a teaser. The whole chapter.</p>
        <div class="btnrow mt3">
          <a class="btn btn--ghost" href="/books/exceptional-by-design/excerpt/">Read chapter four</a>
        </div>
      </div>
      <div>
        <blockquote class="pull">We treat every client as a human being and a friend, not a
          transaction. We didn&rsquo;t start this business as a profit center.
          <cite>Selling Main Street</cite></blockquote>
      </div>
    </div>
    <div class="mt5">
      <div class="eyebrow">For booksellers, libraries and course adopters</div>
      <p class="body mt2">We handle bulk and institutional orders, examination copies, and
        licensing for cohort or classroom use directly &mdash; every title, any quantity.
        {mail()}</p>
    </div>
  </div>
</section>
"""
write("/books/", "Books — Exceptional Media",
      "The Exceptional trilogy — Exceptional by Design, Exceptional Systems and Exceptional "
      "Stewardship — plus the Main Street books on selling and buying a business.", books,
      schema=graph(crumbs(("Home", "/"), ("Books", "/books/")), {
        "@type": "CollectionPage", "name": "Books", "url": SITE + "/books/",
        "isPartOf": {"@id": SITE + "/#site"},
        "hasPart": [
          book_ld("Exceptional by Design", [CHRIS, TARA], "/books/exceptional-by-design/"),
          book_ld("Exceptional Systems", [CHRIS, MARCUS], "/books/exceptional-systems/"),
          book_ld("Exceptional Stewardship", [TARA, CHRIS], "/books/exceptional-stewardship/"),
          book_ld("Selling Main Street", [CHRIS], "/books/", "2024",
                  buy="https://www.amazon.com/dp/B0D2B72W18"),
          book_ld("Buying Main Street", [CHRIS], "/books/", "2025",
                  buy="https://www.amazon.com/dp/195787029X"),
        ]}))

# ══════════════════════════════════════════════════════════════════════════
# BOOK 1 — EXCEPTIONAL BY DESIGN
# ══════════════════════════════════════════════════════════════════════════
PILLARS = [("Faith","Relationship with God. Daily practice, not a category."),
           ("Family","Marriage first, then children, then the people you adopt in."),
           ("Fitness","Physical and mental margin. Health as a discipline."),
           ("Finances","Freedom and stewardship, not accumulation for its own sake."),
           ("Fulfillment","Purpose-driven work. Meaning and legacy."),
           ("Fun","Adventure, play, humor, the outdoors."),
           ("Freedom","Time, relationships, purpose &mdash; freedom in all three."),
           ("Business","Enterprise building. The Three P&rsquo;s.")]

PHASES = [("Dream It","Get clear. Define purpose, assess where you actually are, and write a vision in the present tense."),
          ("Build It","Weekly systems, daily disciplines, time mastery, financial freedom, and the team around you."),
          ("Optimize It","Navigate the obstacles, measure what matters, and iterate instead of restarting."),
          ("Live It","Gratitude, service, legacy. The part most plans never get to.")]

ebd = f"""
<section class="pagehead">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="eyebrow">Book one &middot; The Exceptional Life OS</div>
    <h1 class="display mt2">Exceptional<br>by Design</h1>
    <hr class="accentrule wide mt3">
    <p class="lead mt3"><b style="font-weight:400">Building Your Dream Life.</b> Chris Seegers
      and Tara Seegers on designing a life on purpose &mdash; eight pillars, four phases, and an
      assessment that tells you where you actually stand.</p>
    <div class="mt3"><span class="pill pill--soon">Anticipated Q1 2027</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">About the book</div>
        <h2 class="h2 mt2">Most people design their business and improvise their life.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">This book came out of a year Chris and Tara did not plan and would not
          repeat. What it produced was a framework: a way to look at a whole life the way an
          operator looks at a company &mdash; in pillars you can name, phases you can run, and
          disciplines you can measure.</p>
        <p>Seventeen chapters across four phases. We wrote it to be worked, not read. The exercises
          are the book; the prose is there to get you into them.</p>
        <p>Tara Seegers is co-author. The framework is the one the two of them used to move
          their family from Texas to Colorado, restructure the businesses, and build the life
          they had been describing to each other for a decade.</p>

        <div class="mt4">
          <div class="factrow"><span class="k">Authors</span><span>Chris Seegers and Tara Seegers</span></div>
          <div class="factrow"><span class="k">Position</span><span>Book one of three</span></div>
          <div class="factrow"><span class="k">System</span><span>The Exceptional Life OS</span></div>
          <div class="factrow"><span class="k">Publication</span><span>In production. Anticipated Q1 2027.</span></div>
          <div class="factrow"><span class="k">For media</span><span><a href="/books/exceptional-by-design/press/">Press kit</a> &mdash; descriptions, bios, interview questions</span></div>
          <div class="factrow"><span class="k">Structure</span><span>17 chapters &middot; 4 phases &middot; 8 pillars</span></div>
          <div class="factrow"><span class="k">Companion</span><span><a href="https://exceptional-os.com" rel="noopener" target="_blank">Exceptional Life OS</a> &mdash; the assessment and the digital platform</span></div>
          <div class="factrow"><span class="k">Publisher</span><span>Exceptional Media</span></div>
        </div>
      </div>
      <div>
        {cover(["EXCEPTIONAL","BY DESIGN"], "The Exceptional Life OS", gold=True)}
        <div class="btnrow mt3">
          {mail("Send me launch updates", subject="Exceptional%20by%20Design%20%E2%80%94%20launch%20updates", cls="btn")}
        </div>
        <div class="btnrow mt2">
          <a class="btn btn--ghost" href="https://exceptional-os.com" rel="noopener" target="_blank">Take the assessment</a>
        </div>
        <p class="small mt2">Retail links go live at launch.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="eyebrow">The framework</div>
    <h2 class="h1 mt2">Four phases.</h2>
    <hr class="accentrule mt3">
    <div class="steps mt4">
      {"".join('''<div class="step" style="background:rgba(255,255,255,.06);color:#fff">
        <span class="n" style="color:var(--accent)">0%d</span>
        <div class="t">%s</div><p style="color:rgba(255,255,255,.82)">%s</p></div>''' % (i+1, t, d)
        for i, (t, d) in enumerate(PHASES))}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">The framework</div>
    <h2 class="h1 mt2">Eight pillars.</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">Every one of them is assessed, and every one of them is designed. A life
      that is exceptional in six and neglected in two is not exceptional.</p>
    <div class="pillars mt4">
      {"".join('<div class="pillar"><div class="t">%s</div><p>%s</p></div>' % (t, d) for t, d in PILLARS)}
    </div>
  </div>
</section>

<section class="section section--deep">
    <div class="wrap" style="position:relative;z-index:2">
    <blockquote class="pull" style="color:#fff">We don&rsquo;t want you in the stands. We want you
      on the field. Your name on the jersey. Building your dream, not watching somebody else
      build theirs.<cite>Exceptional by Design</cite></blockquote>
    <div class="split mt5">
      <div class="body">
        <div class="eyebrow">Fence to the support post</div>
        <p class="mt2" style="color:rgba(255,255,255,.86)">At twenty-four, Chris and his brothers
          built two miles of fence around a hundred and sixty acres outside Las Vegas, New Mexico,
          with hand tools, to pay for business school. The only way they survived it was to stop
          measuring the two miles.</p>
        <p style="color:rgba(255,255,255,.86)">Not two miles. Not until sundown. Just fence to the
          next support post. Then the next one. It is the method the whole book runs on, we still use
          it, and the fence is still standing.</p>
      </div>
      <div class="body">
        <div class="eyebrow">The assessment</div>
        <p class="mt2" style="color:rgba(255,255,255,.86)">The Exceptional Design Assessment maps
          you across seven dimensions and ten archetypes, then generates a report against the
          eight pillars. It is the diagnostic the book&rsquo;s exercises are built on.</p>
        <div class="btnrow mt3"><a class="btn" href="https://exceptional-os.com" rel="noopener" target="_blank">Discover your design</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--rule">
  <div class="wrap">
    <div class="eyebrow">Contents</div>
    <h2 class="h1 mt2">Seventeen chapters.</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">Four phases, and a chapter you can open on its own when that is the part
      of your life that needs work this month.</p>
    <div class="mt4">{toc(TOC_EBD)}</div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Read it before it&rsquo;s out</div>
        <h2 class="h1 mt2">Chapter four,<br>in full.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">&ldquo;Create Your Life Vision&rdquo; is the chapter the rest of the book
          leans on &mdash; getting quiet enough to hear what you actually want, and then the
          ten-year exercise that puts it on paper in the present tense.</p>
        <p>It is the exercise Chris and Tara ran on themselves, in a lonely spot in rural
          Colorado, with a journal and no phone. We put the whole chapter up rather than a
          teaser, because a sample that stops at the interesting part is not a sample.</p>
        <p>The book is anticipated in the first quarter of 2027. This chapter is available now.</p>
        <div class="btnrow mt4">
          <a class="btn" href="/books/exceptional-by-design/excerpt/">Read chapter four</a>
        </div>
      </div>
      <div>
        <blockquote class="pull" style="color:#fff">You can&rsquo;t hear what you really want when
          there&rsquo;s noise all around you. You can&rsquo;t dream when you&rsquo;re distracted.
          <cite>Chapter 4 &middot; Create Your Life Vision</cite></blockquote>
      </div>
    </div>
  </div>
</section>

{endorsements("exceptional-by-design")}
{bulk("Exceptional by Design", kit="/books/exceptional-by-design/press/")}

<section class="section">
  <div class="wrap">
    <div class="eyebrow">Next in the trilogy</div>
    <h2 class="h2 mt2">Keep going</h2>
    <hr class="accentrule mt3">
    <div class="grid g2 mt4">
      {bookcard(BOOKS[1])}{bookcard(BOOKS[2])}
    </div>
  </div>
</section>
"""
write("/books/exceptional-by-design/", "Exceptional by Design — Book One of the Exceptional Trilogy",
      "Chris and Tara Seegers on designing a life on purpose: eight pillars, four phases, and the "
      "Exceptional Design Assessment. Book one of the trilogy, launching Q1 2027.", ebd, depth=2,
      schema=graph(
        crumbs(("Home", "/"), ("Books", "/books/"),
               ("Exceptional by Design", "/books/exceptional-by-design/")),
        book_ld("Exceptional by Design: Building Your Dream Life", [CHRIS, TARA],
                "/books/exceptional-by-design/",
                about=["Personal development", "Goal setting", "Life planning", "Faith and work"])))

# ══════════════════════════════════════════════════════════════════════════
# EXCERPT — Exceptional by Design, Chapter 4
# Transcribed verbatim from Exceptional_by_Design_4-13-26.docx. This is the
# BOOK's voice, which is first person singular. The site's plural-voice rule
# governs our own copy, not quoted book text — do not "fix" it here.
#
# Why chapter 4 and not the Introduction: the Introduction tells the story of
# Tara's April 2020 health emergency. That is the authors' story to place, not
# ours, and putting a family medical emergency on a marketing page is Chris and
# Tara's call to make. Chapter 4 is also the stronger sales excerpt. Say the
# word and the Introduction goes up instead. README item 13.
# ══════════════════════════════════════════════════════════════════════════
exc = f"""
<section class="pagehead">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="eyebrow">Exceptional by Design &middot; Chapter four</div>
    <h1 class="display mt2">Create Your<br>Life Vision</h1>
    <hr class="accentrule wide mt3">
    <p class="lead mt3">The whole chapter, not a teaser. A sample that stops at the interesting
      part is not a sample.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="excerpt">

      <div class="srcnote">From <i>Exceptional by Design: Building Your Dream Life</i> by Chris
        Seegers and Tara Seegers. Chapter four of seventeen. Reproduced in full, in the
        authors&rsquo; own voice.</div>

      <h2>In this chapter</h2>
      <ul class="bullets">
        <li>How to get quiet and hear what you really want</li>
        <li>The ten-year vision exercise that changes everything</li>
        <li>How to visualize your ideal life across all eight pillars</li>
        <li>Why you must dream bigger than you think possible</li>
        <li>How to make your vision so clear you can taste it</li>
      </ul>

      <h2>Getting Quiet</h2>
      <p class="drop">When we decided to create the design for our exceptional life after
        Tara&rsquo;s health event, the first thing we did was get quiet. Individually, and
        together as a couple.</p>
      <p>Not just turn off the phone. I mean really quiet. I drove to a lonely spot in rural
        Colorado with nothing but my journal and a few pens. No phone. No computer. Nothing
        digital that could break the quiet.</p>
      <p>I spent time connecting with my Creator, being quiet, allowing myself to release
        everything that had built up, and then I started writing.</p>
      <p>This is essential. You can&rsquo;t hear what you really want when there&rsquo;s noise all
        around you. You can&rsquo;t dream when you&rsquo;re distracted. You can&rsquo;t envision
        your future when you&rsquo;re drowning in the urgent demands of today.</p>
      <p>You need quiet. You need space. You need permission to dream without immediate practical
        concerns shutting down your imagination.</p>
      <p>So, before we go any further, I want you to plan your quiet time. Put it on your
        calendar. Block out at least half a day, ideally a full day. Go somewhere you won&rsquo;t
        be interrupted. Bring your journal. Bring these questions. Bring an openness to what might
        emerge.</p>

      <h2>The Ten-Year Vision Exercise</h2>
      <p>Here&rsquo;s the exercise that will change your life: imagine it&rsquo;s ten years from
        today. You&rsquo;re living your absolute dream life. Everything you&rsquo;ve worked toward
        has come to fruition. You&rsquo;re living at your highest potential.</p>
      <p>Now describe that life in vivid detail. Not just the highlights. The actual texture of
        your days.</p>
      <ul class="qlist">
        <li>What do you see when you wake up?</li>
        <li>Who&rsquo;s next to you?</li>
        <li>What does your morning routine look like?</li>
        <li>Where do you live? What does your house look like? Your property?</li>
        <li>What do you do for work? How do you spend your time?</li>
        <li>Who are your closest friends?</li>
        <li>What does your body look like? How do you feel physically?</li>
        <li>What are you creating? What impact are you having?</li>
        <li>How has your relationship with God grown?</li>
        <li>What adventures have you been on?</li>
        <li>What does a typical week look like?</li>
      </ul>
      <p>Write it all down. In present tense, as if you&rsquo;re living it right now.</p>

      <div class="srcnote mt5">End of excerpt. Chapter four continues in the book, which carries
        the exercise across all eight pillars and into the North Star Goals of chapter five.</div>

    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Do the exercise</div>
        <h2 class="h1 mt2">Bring a journal.<br>Or bring the OS.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">Everything built in Phase One lives in two modules of the Exceptional Life
          OS: <b style="font-weight:500">My Design</b>, where you document values, purpose,
          beliefs and current reality, and <b style="font-weight:500">My Vision</b>, where the
          ten-year picture and the North Star Goals go.</p>
        <p>Together they answer the two questions the rest of the book depends on: who am I, and
          where am I going?</p>
      </div>
      <div>
        <div class="btnrow">
          <a class="btn" href="https://exceptional-os.com" rel="noopener" target="_blank">Open the Life OS</a>
          {mail("Send me launch updates", subject="Exceptional%20by%20Design%20%E2%80%94%20launch%20updates", cls="btn btn--ghost")}
          <a class="btn btn--ghost" href="/books/exceptional-by-design/">Back to the book</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write("/books/exceptional-by-design/excerpt/",
      "Create Your Life Vision — Chapter Four, Read in Full",
      "The complete fourth chapter of Exceptional by Design by Chris and Tara Seegers: getting "
      "quiet, and the ten-year vision exercise, reproduced in full, ahead of the Q1 2027 launch.",
      exc, depth=3,
      schema=graph(
        crumbs(("Home", "/"), ("Books", "/books/"),
               ("Exceptional by Design", "/books/exceptional-by-design/"),
               ("Chapter four", "/books/exceptional-by-design/excerpt/")),
        {"@type": "Chapter", "name": "Create Your Life Vision", "position": 4,
         "author": [CHRIS, TARA], "inLanguage": "en-US",
         "url": SITE + "/books/exceptional-by-design/excerpt/",
         "isPartOf": {"@type": "Book", "name": "Exceptional by Design: Building Your Dream Life",
                      "url": SITE + "/books/exceptional-by-design/"},
         "publisher": {"@id": SITE + "/#org"}}))


# ══════════════════════════════════════════════════════════════════════════
# BOOK 2 — EXCEPTIONAL SYSTEMS
# ══════════════════════════════════════════════════════════════════════════
SYS_PHASES = [
 ("Dream It","Guiding Principles, a Purpose Statement, a Long-Term Goal, the 3-Year Picture and 1-Year Plan, and the Story you tell about all of it. This is the clarity most companies never get."),
 ("Build It","Hire for character with the Culture Scorecard. Train with the Two-Trainer System. Install a meeting rhythm that holds weekly, quarterly and annual alignment. Measure with a Weekly Scorecard of lead and lag measures across Impact, Growth and Operational."),
 ("Optimize It","The Action System for goals, tasks, issues and ideas. The Playbook that documents every critical process. A training pipeline that makes a new hire productive in sixty days."),
 ("Monetize It","Not a desperate exit when you are burned out &mdash; a deliberate harvest. Sell, transition, or restructure. The systems are what make the business worth something to somebody other than you."),
]

sysbk = f"""
<section class="pagehead">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="eyebrow">Book two &middot; The Exceptional Business OS</div>
    <h1 class="display mt2">Exceptional<br>Systems</h1>
    <hr class="accentrule wide mt3">
    <p class="lead mt3">Chris Seegers and Marcus Seegers on building a business that runs on
      documentation and discipline instead of heroic effort and tribal knowledge.</p>
    <div class="mt3"><span class="pill pill--soon">Anticipated Q4 2027</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">About the book</div>
        <h2 class="h2 mt2">Every owner deserves better than running out of time.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">The businesses that consume the very life they were supposed to fund all
          fail the same way: the owner is the system. Every decision routes through one person,
          every process lives in one head, and the company cannot be handed to anyone &mdash;
          not a buyer, not a successor, not a Tuesday off.</p>
        <p><em>Exceptional Systems</em> is our fix, written as a loop you run rather than a theory
          you agree with. Four phases, cycled quarterly and annually, each pass
          compounding on the last.</p>
        <p>It is also the book that makes
          <a href="https://www.amazon.com/dp/B0D2B72W18" rel="noopener" target="_blank"><em>Selling
          Main Street</em></a> worth reading. The work you do here is what makes the exit in that
          book possible at all &mdash; alongside the
          unglamorous instruments most owners put off, the funded buy-sell and the key person
          cover we write through
          <a href="https://insureexceptional.com" rel="noopener" target="_blank">Exceptional
          Insurance</a>. A business nobody can buy is not an asset.</p>

        <div class="mt4">
          <div class="factrow"><span class="k">Authors</span><span>Chris Seegers and Marcus Seegers</span></div>
          <div class="factrow"><span class="k">Position</span><span>Book two of three</span></div>
          <div class="factrow"><span class="k">System</span><span>The Exceptional Business OS</span></div>
          <div class="factrow"><span class="k">Structure</span><span>Four phases, run as a quarterly and annual loop</span></div>
          <div class="factrow"><span class="k">Publication</span><span>Manuscript complete, in edit. Anticipated Q4 2027.</span></div>
          <div class="factrow"><span class="k">For media</span><span><a href="/books/exceptional-systems/press/">Press kit</a> &mdash; descriptions, bios, interview questions</span></div>
          <div class="factrow"><span class="k">Publisher</span><span>Exceptional Media</span></div>
        </div>

        <div class="btnrow mt4">
          {mail("Send me launch updates", subject="Exceptional%20Systems%20%E2%80%94%20launch%20updates", cls="btn")}
        </div>
      </div>
      <div>
        {cover(["EXCEPTIONAL","SYSTEMS"], "The Exceptional Business OS")}
        <blockquote class="pull mt4" style="font-size:20px">A business that runs on documentation
          and discipline instead of heroic effort and tribal knowledge.
          <cite>Exceptional Systems</cite></blockquote>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="eyebrow">The loop</div>
    <h2 class="h1 mt2">Four phases,<br>run on repeat.</h2>
    <hr class="accentrule mt3">
    <div class="steps mt4">
      {"".join('''<div class="step" style="background:rgba(255,255,255,.06);color:#fff">
        <span class="n" style="color:var(--accent)">0%d</span>
        <div class="t">%s</div><p style="color:rgba(255,255,255,.82)">%s</p></div>''' % (i+1, t, d)
        for i, (t, d) in enumerate(SYS_PHASES))}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">People. Process. Profit.</div>
        <h2 class="h2 mt2">The order is the argument.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">Put People first &mdash; your team, your customers, your community &mdash;
          and build Processes that serve those people with excellence. Profit is what comes out
          the other end. It is an operating principle and a moral framework at the same time,
          and reversing the order breaks both.</p>
        <p>Not profit for profit&rsquo;s sake. Profit as fuel for mission.</p>
      </div>
      <div class="body">
        <div class="eyebrow">The 90-day challenge</div>
        <h2 class="h2 mt2">The book ends with homework.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">Within ninety days of finishing it, you run your first full quarterly loop
          &mdash; principles and purpose in weeks one and two, the 3-Year Picture and first
          quarterly goals in weeks three and four, and on from there.</p>
        <p>We think a book like this is worth nothing if you close it and run the company the same
          way you did before you opened it.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--deep">
    <div class="wrap" style="position:relative;z-index:2">
    <blockquote class="pull" style="color:#fff">Not ministry in spite of profit. Ministry through
      profit.<cite>Exceptional Systems &middot; Capitalist Missionaries</cite></blockquote>
  </div>
</section>

<section class="section section--rule">
  <div class="wrap">
    <div class="eyebrow">Contents</div>
    <h2 class="h1 mt2">Fifteen chapters,<br>four parts.</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">Part four is the one most operating systems leave out. A business you
      cannot sell, transition or restructure is not finished &mdash; it is just busy.</p>
    <div class="mt4">{toc(TOC_SYS)}</div>
  </div>
</section>

{endorsements("exceptional-systems")}
{bulk("Exceptional Systems", kit="/books/exceptional-systems/press/")}

<section class="section">
  <div class="wrap">
    <div class="eyebrow">Read alongside</div>
    <h2 class="h2 mt2">The rest of the shelf</h2>
    <hr class="accentrule mt3">
    <div class="grid g2 mt4">
      {bookcard(BOOKS[0])}{bookcard(BOOKS[2])}
    </div>
  </div>
</section>
"""
write("/books/exceptional-systems/", "Exceptional Systems — Book Two of the Exceptional Trilogy",
      "Chris and Marcus Seegers on building a business that runs on documentation and discipline "
      "instead of heroic effort. Book two — it installs the Exceptional Business OS.",
      sysbk, depth=2,
      schema=graph(
        crumbs(("Home", "/"), ("Books", "/books/"),
               ("Exceptional Systems", "/books/exceptional-systems/")),
        book_ld("Exceptional Systems", [CHRIS, MARCUS], "/books/exceptional-systems/",
                about=["Business operations", "Systems and processes", "Business exit planning"])))

# ══════════════════════════════════════════════════════════════════════════
# BOOK 3 — EXCEPTIONAL STEWARDSHIP
# ══════════════════════════════════════════════════════════════════════════
stw = f"""
<section class="pagehead">
  <div class="energy" aria-hidden="true"></div>
  <div class="wrap">
    <div class="eyebrow">Book three &middot; The Exceptional Wealth OS</div>
    <h1 class="display mt2">Exceptional<br>Stewardship</h1>
    <hr class="accentrule wide mt3">
    <p class="lead mt3">Tara Seegers and Chris Seegers on what happens to money once it arrives,
      how it works, and how to leave it well. The book that completes the trilogy.</p>
    <div class="mt3"><span class="pill pill--soon">Anticipated Q2 2028</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">About the book</div>
        <h2 class="h2 mt2">The wire hits. Then what?</h2>
        <hr class="accentrule mt3">
        <p class="mt3">Our <a href="/books/">first two books</a> get you to the transaction. This one
          starts the day after.</p>
        <p>An owner who has spent thirty years building a company has spent thirty years being
          good at exactly one thing that will no longer be true of them. The money is now the
          asset, the calendar is empty, and nobody prepared them for either.</p>
        <p>We are writing <em>Exceptional Stewardship</em> for that person &mdash; and for the
          family around them, who inherit a set of decisions nobody has ever discussed out loud.</p>
        <p>Protection sits inside this book rather than beside it. Stewardship is not only what you
          grow &mdash; it is what survives you being wrong, or unlucky, or gone. That is ground we
          work every day through
          <a href="https://insureexceptional.com" rel="noopener" target="_blank">Exceptional
          Insurance</a>, and it belongs in the Wealth OS, not in an appendix.</p>
        <p>The through-line of the trilogy holds, and we believe it: wealth is not a scoreboard. It
          is a thing you are responsible for on behalf of people who are not in the room.</p>

        <div class="mt4">
          <div class="factrow"><span class="k">Authors</span><span>Tara Seegers and Chris Seegers</span></div>
          <div class="factrow"><span class="k">Position</span><span>Book three of three</span></div>
          <div class="factrow"><span class="k">System</span><span>The Exceptional Wealth OS</span></div>
          <div class="factrow"><span class="k">Publication</span><span>In development. Anticipated Q2 2028.</span></div>
          <div class="factrow"><span class="k">Publisher</span><span>Exceptional Media</span></div>
        </div>

        <div class="btnrow mt4">
          {mail("Send me launch updates", subject="Exceptional%20Stewardship%20%E2%80%94%20launch%20updates", cls="btn")}
        </div>
      </div>
      <div>
        {cover(["EXCEPTIONAL","STEWARDSHIP"], "The Exceptional Wealth OS")}
        <blockquote class="pull mt4" style="font-size:20px">Business is ministry, fueled by
          sustainable cashflow.<cite>Chris Seegers</cite></blockquote>
      </div>
    </div>
  </div>
</section>

{bulk("Exceptional Stewardship")}

<section class="section section--navy">
  <div class="wrap">
    <div class="eyebrow">Where it sits</div>
    <h2 class="h1 mt2">One argument,<br>three books.</h2>
    <hr class="accentrule mt3">
    <div class="grid g3 mt4">
      <div class="card card--dark"><div class="kicker">Book one</div>
        <div class="title">Exceptional by Design</div>
        <p>Installs the Exceptional Life OS. Design the life first &mdash; everything else is built to serve it.</p>
        <a class="go" href="/books/exceptional-by-design/">Read more &rsaquo;</a></div>
      <div class="card card--dark"><div class="kicker">Book two</div>
        <div class="title">Exceptional Systems</div>
        <p>Installs the Exceptional Business OS. Build the company so it can run &mdash; and be handed on &mdash; without you.</p>
        <a class="go" href="/books/exceptional-systems/">Read more &rsaquo;</a></div>
      <div class="card card--dark" style="border-left-color:#fff"><div class="kicker">Book three &middot; Tara and Chris Seegers</div>
        <div class="title">Exceptional Stewardship</div>
        <p>Installs the Exceptional Wealth OS. Steward what the first two produced, and hand it off on purpose.</p>
        <span class="go" style="opacity:.7">In development</span></div>
    </div>
  </div>
</section>
"""
# ── COMPLIANCE STOP ────────────────────────────────────────────────────────
# Wealth-side content is governed by Brand Standards v1.0 §10 plus FINRA/SEC.
# Before this page publishes:
#   1. Compliance supplies disclosure text; set unaltered, Montserrat 400, 6-7pt, gray, at foot.
#   2. Confirm the title. The publisher packet (Sept 2026) lists this volume as "Wealth OS";
#      chrisseegers.com lists it as "Exceptional Stewardship". One of the two is wrong.
#   3. The winged-horse mark is prohibited on wealth-side pieces. This site is wordmark-only
#      throughout, so that stop is already satisfied.
write("/books/exceptional-stewardship/", "Exceptional Stewardship — Book Three of the Exceptional Trilogy",
      "The third book in the Exceptional trilogy: what happens to money once it arrives, how it "
      "works, and how to leave it well. Tara and Chris Seegers on the Exceptional Wealth OS, "
      "anticipated Q2 2028.", stw, depth=2,
      schema=graph(
        crumbs(("Home", "/"), ("Books", "/books/"),
               ("Exceptional Stewardship", "/books/exceptional-stewardship/")),
        book_ld("Exceptional Stewardship", [TARA, CHRIS], "/books/exceptional-stewardship/",
                about=["Wealth stewardship", "Family governance", "Legacy planning"])))

# ── Press kit · Exceptional by Design ────────────────────────────────────
write("/books/exceptional-by-design/press/",
      "Press Kit — Exceptional by Design",
      "Descriptions, author biographies, interview questions and asset requests for "
      "Exceptional by Design by Chris and Tara Seegers, anticipated Q1 2027.",
      presskit(
        slug="exceptional-by-design",
        title="Exceptional by Design",
        subtitle="Building Your Dream Life",
        authors="Chris Seegers and Tara Seegers",
        when="Anticipated Q1 2027",
        d25="Chris and Tara Seegers on designing a life on purpose &mdash; eight pillars, four "
            "phases, and an assessment that shows you where you actually stand.",
        d50="Most people design their business and improvise their life. <i>Exceptional by "
            "Design</i> treats a whole life the way an operator treats a company: in pillars you "
            "can name, phases you can run, and disciplines you can measure. Seventeen chapters, "
            "written to be worked rather than read.",
        d150="Most people design their business and improvise their life. In <i>Exceptional by "
             "Design</i>, Chris and Tara Seegers hand over the framework they built for "
             "themselves after a year they did not plan and would not repeat &mdash; and then "
             "used to move their family from Texas to Colorado, restructure their businesses, and "
             "build the life they had been describing to each other for a decade.<br><br>"
             "The book runs on eight pillars &mdash; Faith, Family, Fitness, Finances, "
             "Fulfillment, Fun, Freedom and Business &mdash; across four phases: Dream It, Build "
             "It, Optimize It, Live It. Seventeen chapters, each one an exercise rather than an "
             "argument. It is written to be worked, not read.<br><br>"
             "Chris Seegers founded Exceptional Companies, an innovation company. Tara Seegers is a "
             "Certified Financial Planner&trade; named to Forbes&rsquo; Top Women Wealth Advisors "
             "Best-In-State list. They live in Colorado Springs with their three children.",
        contains=[
          ("Eight pillars", "Faith &middot; Family &middot; Fitness &middot; Finances &middot; "
                            "Fulfillment &middot; Fun &middot; Freedom &middot; Business"),
          ("Four phases", "Dream It &middot; Build It &middot; Optimize It &middot; Live It"),
          ("Length", "Seventeen chapters, plus appendices"),
          ("Core exercises", "The ten-year vision exercise &middot; the 30-Day Kickstart Guide"),
          ("Signature idea", "&ldquo;Fence to the support post&rdquo; &mdash; break any "
                             "impossible task into the next immediate action"),
          ("Assessment", "The Exceptional Design Assessment, at exceptional-os.com"),
          ("Companion", "The Exceptional Life OS &mdash; the digital system the book maps to"),
        ],
        questions=[
          "The book opens with a year you did not plan. What did that year teach you that no "
          "business lesson had?",
          "You say most people design their business and improvise their life. Where does that "
          "usually show up first?",
          "Eight pillars is a lot to hold at once. What happens to someone who is exceptional in "
          "six and neglecting two?",
          "&ldquo;Fence to the support post&rdquo; came from building two miles of fence by hand "
          "at twenty-four. How does that translate for someone staring at a ten-year vision?",
          "You wrote this with your wife. What did the two of you disagree about?",
        ],
        bios=[("Chris Seegers", "long form, 124 words", BIO_CHRIS_LONG),
              ("Chris Seegers", "short form, 50 words", BIO_CHRIS_SHORT),
              ("Tara Seegers", "long form", BIO_TARA_LONG)],
        prev_url="/books/exceptional-by-design/", prev_label="book page"),
      depth=3,
      schema=graph(
        crumbs(("Home", "/"), ("Books", "/books/"),
               ("Exceptional by Design", "/books/exceptional-by-design/"),
               ("Press kit", "/books/exceptional-by-design/press/")),
        {"@type": "WebPage", "name": "Press Kit — Exceptional by Design",
         "url": SITE + "/books/exceptional-by-design/press/",
         "publisher": {"@id": SITE + "/#org"},
         "about": {"@type": "Book", "name": "Exceptional by Design: Building Your Dream Life",
                   "author": [CHRIS, TARA], "url": SITE + "/books/exceptional-by-design/"}}))

# ── Press kit · Exceptional Systems ──────────────────────────────────────
write("/books/exceptional-systems/press/",
      "Press Kit — Exceptional Systems",
      "Descriptions, author biographies, interview questions and asset requests for "
      "Exceptional Systems by Chris and Marcus Seegers, anticipated Q4 2027.",
      presskit(
        slug="exceptional-systems",
        title="Exceptional Systems",
        subtitle="The Business OS",
        authors="Chris Seegers and Marcus Seegers",
        when="Anticipated Q4 2027",
        d25="Chris and Marcus Seegers on building a business that runs on documentation and "
            "discipline instead of heroic effort and tribal knowledge.",
        d50="The businesses that consume the life they were supposed to fund all fail the same "
            "way: the owner is the system. <i>Exceptional Systems</i> is the fix &mdash; four "
            "phases run as a quarterly loop, ending in the one most operating systems leave out. "
            "Monetize It.",
        d150="Every business owner who builds something real with their hands, their talent and "
             "their years deserves better than running out of time holding it. The companies that "
             "consume the very life they were supposed to fund all fail the same way: the owner "
             "<i>is</i> the system. Every decision routes through one person, every process lives "
             "in one head, and the company cannot be handed to anyone &mdash; not a buyer, not a "
             "successor, not a Tuesday off.<br><br>"
             "<i>Exceptional Systems</i> is the fix, written as a loop you run rather than a "
             "theory you agree with: Dream It, Build It, Optimize It, Monetize It, cycled "
             "quarterly and annually, each pass compounding on the last. It ends with the phase "
             "most operating systems skip &mdash; the deliberate harvest, whether that is a sale, "
             "a transition or a restructure.<br><br>"
             "Chris Seegers founded Exceptional Companies, an innovation company. Marcus Seegers is a "
             "Co-Founder of Exceptional Business Advisors, where he owns operations and systems.",
        contains=[
          ("Four phases", "Dream It &middot; Build It &middot; Optimize It &middot; Monetize It"),
          ("Length", "Fifteen chapters across four parts"),
          ("Phase one", "Guiding Principles, Purpose Statement, Long-Term Goal, the Story"),
          ("Phase two", "Culture Scorecard, the Two-Trainer System, meeting rhythm, the Weekly "
                        "Scorecard across Impact, Growth and Operational"),
          ("Phase three", "The Action System, the Playbook, a sixty-day training pipeline"),
          ("Phase four", "Exit valuation, the personal plan, the wealth plan, exit and transition"),
          ("Core principle", "People, Process, Profit &mdash; in that order, always"),
          ("Closing challenge", "The 90-Day Challenge &mdash; one full quarterly loop"),
        ],
        questions=[
          "You say the owner <i>is</i> the system in most struggling companies. What is the first "
          "sign of that from the outside?",
          "People, Process, Profit. What actually breaks when someone reverses the order?",
          "Part four is Monetize It, and most operating systems stop before that. Why do they, and "
          "why did you not?",
          "You wrote this with your brother, who runs the operations side. What does he see that "
          "you do not?",
          "The book ends with homework, not inspiration. What happens in the first ninety days?",
        ],
        bios=[("Chris Seegers", "long form, 124 words", BIO_CHRIS_LONG),
              ("Chris Seegers", "short form, 50 words", BIO_CHRIS_SHORT),
              ("Marcus Seegers", "short form", BIO_MARCUS)],
        prev_url="/books/exceptional-systems/", prev_label="book page"),
      depth=3,
      schema=graph(
        crumbs(("Home", "/"), ("Books", "/books/"),
               ("Exceptional Systems", "/books/exceptional-systems/"),
               ("Press kit", "/books/exceptional-systems/press/")),
        {"@type": "WebPage", "name": "Press Kit — Exceptional Systems",
         "url": SITE + "/books/exceptional-systems/press/",
         "publisher": {"@id": SITE + "/#org"},
         "about": {"@type": "Book", "name": "Exceptional Systems",
                   "author": [CHRIS, MARCUS], "url": SITE + "/books/exceptional-systems/"}}))


# ══════════════════════════════════════════════════════════════════════════
# PODCASTS
# ══════════════════════════════════════════════════════════════════════════
pods = pagehead("On air", "The shows.",
  "Two weekly conversations &mdash; one about buying, selling and running companies, one about "
  "the people building them in Colorado.") + f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Host &middot; Chris Seegers</div>
        <h2 class="h1 mt2">Exceptional<br>Companies<br>Podcast</h2>
        <hr class="accentrule mt3">
        <p class="mt3">Buying, selling, and optimizing businesses &mdash; and what faith has to do
          with any of it. Owners who have been through the transaction, operators in the middle of
          it, and the advisors who work on both sides.</p>
        <p>Weekly. Chris hosts.</p>
      </div>
      <div>
        <div class="card">
          <div class="kicker">Listen</div>
          <div class="title">Everywhere you get podcasts</div>
          <div class="chips">
            <a class="chip" href="https://podcasts.apple.com/us/podcast/exceptional-companies-podcast/id1765569160" rel="noopener" target="_blank">Apple Podcasts</a>
            <a class="chip" href="https://open.spotify.com/show/5JzPgkrevSMZCFWsXkglJv" rel="noopener" target="_blank">Spotify</a>
            <a class="chip" href="https://www.youtube.com/@ExceptionalCompaniesPodcast" rel="noopener" target="_blank">YouTube</a>
            <a class="chip" href="https://exceptionalcompanies.captivate.fm" rel="noopener" target="_blank">Captivate</a>
            <a class="chip" href="https://www.amazon.com/Exceptional-Companies-Podcast/dp/B0DFMRW5KY" rel="noopener" target="_blank">Amazon &middot; Audible</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Colorado Springs &middot; weekly</div>
        <h2 class="h1 mt2">Colorado<br>Business<br>Podcast</h2>
        <hr class="accentrule mt3">
        <p class="mt3">The entrepreneurs, operators and changemakers building the Colorado
          business community &mdash; and the stories underneath the companies.</p>
        <p>A show we are part of and keep pointing people to. Three hundred-plus conversations
          deep into the Colorado business scene.</p>
      </div>
      <div>
        <div class="card card--dark">
          <div class="kicker">Listen</div>
          <div class="title">Everywhere you get podcasts</div>
          <div class="chips">
            <a class="chip" style="border-color:rgba(255,255,255,.4);color:#fff" href="https://podcasts.apple.com/us/podcast/colorado-business-podcast/id1492740546" rel="noopener" target="_blank">Apple Podcasts</a>
            <a class="chip" style="border-color:rgba(255,255,255,.4);color:#fff" href="https://open.spotify.com/show/1jSQ8OQSi0rprCcxTGx0KB" rel="noopener" target="_blank">Spotify</a>
            <a class="chip" style="border-color:rgba(255,255,255,.4);color:#fff" href="https://www.youtube.com/@ColoradoBusinessPodcast" rel="noopener" target="_blank">YouTube</a>
            <a class="chip" style="border-color:rgba(255,255,255,.4);color:#fff" href="https://coloradobusinesspodcast.com" rel="noopener" target="_blank">coloradobusinesspodcast.com</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Come on the show</div>
        <h2 class="h2 mt2">Guests</h2>
        <hr class="accentrule mt3">
        <p class="mt3">We book owners with a real story about building, running, or letting go of
          a company &mdash; including the parts that did not work.
          {mail("Pitch us", subject="Podcast%20guest%20pitch")}.</p>
      </div>
      <div class="body">
        <div class="eyebrow">Book Chris on your show</div>
        <h2 class="h2 mt2">Producers</h2>
        <hr class="accentrule mt3">
        <p class="mt3">We keep headshots, the cold-read bio, topics and past appearances in the
          press and podcast kit at
          <a href="https://chrisseegers.com/press" rel="noopener" target="_blank">chrisseegers.com/press</a>.</p>
      </div>
    </div>
  </div>
</section>
"""
write("/podcasts/", "Podcasts — Exceptional Media",
      "The Exceptional Companies Podcast and the Colorado Business Podcast, hosted and co-hosted "
      "by Chris Seegers. Listen on Apple, Spotify and YouTube.", pods, depth=1,
      schema=graph(
        crumbs(("Home", "/"), ("Podcasts", "/podcasts/")),
        {"@type": "PodcastSeries", "name": "Exceptional Companies Podcast",
         "url": SITE + "/podcasts/", "author": CHRIS, "publisher": {"@id": SITE + "/#org"},
         "description": "Buying, selling and optimizing businesses — and what faith has to do "
                        "with any of it.",
         "sameAs": ["https://podcasts.apple.com/us/podcast/exceptional-companies-podcast/id1765569160",
                    "https://open.spotify.com/show/5JzPgkrevSMZCFWsXkglJv",
                    "https://www.youtube.com/@ExceptionalCompaniesPodcast",
                    "https://exceptionalcompanies.captivate.fm"]},
        {"@type": "PodcastSeries", "name": "Colorado Business Podcast",
         "url": "https://coloradobusinesspodcast.com",
         "description": "The entrepreneurs, operators and changemakers building the Colorado "
                        "business community.",
         "sameAs": ["https://podcasts.apple.com/us/podcast/colorado-business-podcast/id1492740546",
                    "https://open.spotify.com/show/1jSQ8OQSi0rprCcxTGx0KB",
                    "https://www.youtube.com/@ColoradoBusinessPodcast"]}))

# ══════════════════════════════════════════════════════════════════════════
# MAGAZINE
# ══════════════════════════════════════════════════════════════════════════
ISSUES = [
  ("01","Fall 2026","Freedom Isn&rsquo;t a Number","The $14 Trillion Handoff","The Day After the Wire Hits"),
  ("02","Winter 2026&ndash;27","It&rsquo;s Tuesday Morning","Your Kid, Your Key Employee, or a Stranger","The Paycheck You Now Write Yourself"),
  ("03","Spring 2027","You&rsquo;ve Discussed the Will. You&rsquo;ve Avoided the Nursing Home.","Between the Handshake and the Wire","The $15 Million Question"),
  ("04","Summer 2027","Twenty More Years. How Many Can You Use?","The Number You Keep","How Much Do I Tell Them, and How Much Do I Leave?"),
]

mag = f"""
<section class="pagehead">
  <div class="energy energy--gold" aria-hidden="true" style="opacity:.35"></div>
  <div class="wrap">
    <div class="eyebrow">Quarterly &middot; print and digital</div>
    <h1 class="display mt2">EXCEPTIONAL.</h1>
    <hr class="accentrule wide mt3">
    <p class="lead mt3">A magazine for Main Street owners and the advisors around them. One
      article per vertical, every issue: Life, Business, Wealth.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">What it is</div>
        <h2 class="h2 mt2">Journalism, not a newsletter with a logo on it.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">The structure mirrors the tagline. Every issue runs one long article per
          vertical &mdash; Life, Business, Wealth &mdash; plus a publisher&rsquo;s letter and a
          standing data page.</p>
        <p>Written for owners with real companies and real decisions in front of them, in
          Colorado, Texas and the Mountain West.</p>
        <p>The verticals stay three, because the tagline is three. Protection runs underneath
          WEALTH rather than beside it &mdash; a buy-sell that is not funded is not a plan, and
          that is Exceptional Insurance&rsquo;s ground.</p>
        <p>Published by Exceptional Companies, jointly serving Exceptional Business Advisors,
          Exceptional Wealth &amp; Family Office, and Exceptional Insurance.</p>
      </div>
      <div>
        <div class="eyebrow">The rules it runs on</div>
        <div class="mt3">
          <div class="factrow"><span class="k">No. 1</span><span>No calls to action inside editorial. Editorial that pitches converts worse, not better.</span></div>
          <div class="factrow"><span class="k">No. 2</span><span>Credit the primary source, never the aggregator.</span></div>
          <div class="factrow"><span class="k">No. 4</span><span>Every article leads with a place the conventional advice is wrong.</span></div>
          <div class="factrow"><span class="k">No. 5</span><span>Publish the uncomfortable number, including our own limits.</span></div>
          <div class="factrow"><span class="k">No. 6</span><span>Date every estimate. Flag modelled projections as modelled.</span></div>
          <div class="factrow"><span class="k">No. 9</span><span>Advertisers never see or influence editorial.</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--deep">
    <div class="wrap" style="position:relative;z-index:2">
    <div class="eyebrow">The year ahead</div>
    <h2 class="h1 mt2">Four issues.</h2>
    <hr class="accentrule mt3">
    <div class="grid g2 mt4">
      {"".join('''<div class="card card--dark">
        <div class="kicker">Issue %s &middot; %s</div>
        <div class="title" style="font-family:var(--font-serif);font-weight:700">%s</div>
        <div class="meta">Life</div>
        <p><b style="font-weight:500">Business</b> &mdash; %s</p>
        <p><b style="font-weight:500">Wealth</b> &mdash; %s</p>
      </div>''' % (n, s, life, biz, wl) for n, s, life, biz, wl in ISSUES)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <blockquote class="pull">Issue 02 contains a section titled &ldquo;A statistic we will not
      print.&rdquo; The refusal is stronger than the statistic would have been.
      <cite>EXCEPTIONAL &middot; editorial standard no. 5</cite></blockquote>
    <div class="split mt5">
      <div class="body">
        <div class="eyebrow">Get it</div>
        <h2 class="h2 mt2">Request a copy</h2>
        <hr class="accentrule mt3">
        <p class="mt3">We send print and digital editions to owners, advisors and clients across
          Colorado, Texas and the Mountain West.</p>
        <div class="btnrow mt3">
          {mail("Request a copy", subject="EXCEPTIONAL%20magazine%20%E2%80%94%20request%20a%20copy", cls="btn")}
        </div>
      </div>
      <div class="body">
        <div class="eyebrow">Advertise</div>
        <h2 class="h2 mt2">Category exclusivity</h2>
        <hr class="accentrule mt3">
        <p class="mt3">We sell a limited number of placements per issue, with category exclusivity.
          Advertisers never see or influence editorial, and we label sponsored columns and edit
          them to the same standard as everything else.</p>
        <div class="btnrow mt3">
          {mail("Request the media kit", subject="EXCEPTIONAL%20magazine%20%E2%80%94%20advertising", cls="btn btn--ghost")}
        </div>
      </div>
    </div>
  </div>
</section>
"""
write("/magazine/", "EXCEPTIONAL Magazine — Exceptional Media",
      "EXCEPTIONAL is a quarterly magazine for Main Street business owners and their advisors. "
      "One article per vertical every issue: Life, Business, Wealth.", mag, depth=1,
      schema=graph({"@type": "Periodical", "name": "EXCEPTIONAL",
                    "url": SITE + "/magazine/", "publisher": {"@id": SITE + "/#org"},
                    "inLanguage": "en-US"}) if MAGAZINE_PROMOTED else None)

# ══════════════════════════════════════════════════════════════════════════
# PRESS — rights, permissions, review copies (NOT a duplicate of the other two)
# ══════════════════════════════════════════════════════════════════════════
FEATURES = [
 ("Voyage Denver","Hidden Gems: Meet Chris Seegers of Exceptional Business Advisors","August 2026",
  "https://voyagedenver.com/interview/hidden-gems-meet-chris-seegers-of-exceptional-business-advisors/"),
 ("Voyage Denver","Building to Let Go &mdash; on ownership, identity, and the art of the exit","March 2026",
  "https://voyagedenver.com/building-to-let-go-chris-seegers-on-ownership-identity-and-the-art-of-the-exit"),
 ("National Christian Foundation","Chris and Tara Seegers on faith, wealth and generosity","2026",
  "https://www.ncfgiving.com/stories/chris-and-tara-seegers/"),
 ("Shoutout Colorado","Meet Chris Seegers &mdash; entrepreneur and capitalist missionary","2021",
  "https://shoutoutcolorado.com/meet-chris-seegers-entrepreneur-and-capitalist-missionary/"),
 ("5280 Magazine","Not Another Ghost Town &mdash; Hillside as a Dark Sky destination","2017",
  "https://5280.com/not-another-ghost-town/"),
 # The dated URL that has been in circulation since 2015 returns a redirect loop — flagged in
 # EBA_Media_Page_Link_Inventory.md in August and never fixed. This /life/ path loads.
 ("Colorado Springs Gazette","Hillside, Colorado: New life for a tiny town","2015",
  "https://gazette.com/life/hillside-colorado-new-life-for-a-tiny-town/article_bd710771-0164-51a7-8022-1b551ffb1709.html"),
]

press = pagehead("Press desk", "Rights &amp;<br>permissions.",
  "For journalists, producers, booksellers and course adopters working with what we publish.") + f"""
<section class="section">
  <div class="wrap">
    <div class="eyebrow">Start here</div>
    <h2 class="h2 mt2">Three desks, three jobs</h2>
    <hr class="accentrule mt3">
    <p class="lead mt3">We keep these separate on purpose, so you land on the one that can
      actually help you.</p>
    <div class="grid g3 mt4">
      <div class="card">
        <div class="kicker">You are here</div>
        <div class="title">The publications</div>
        <p>Come to us for review and examination copies, excerpt and reprint permissions, cover art
          and author photography, bulk and institutional orders, and interviews about the books or
          the magazine &mdash; exits, succession, family governance, or how a buy-sell actually
          gets funded.</p>
        <p><b style="font-weight:500">Working on one title?</b> Go straight to its kit:
          <a href="/books/exceptional-by-design/press/">Exceptional by Design</a> &middot;
          <a href="/books/exceptional-systems/press/">Exceptional Systems</a>.</p>
        {mail("Email the press desk &rsaquo;", subject="Press%20%E2%80%94%20Exceptional%20Media", cls="go")}
      </div>
      <a class="card" href="https://chrisseegers.com/press" rel="noopener" target="_blank">
        <div class="kicker">chrisseegers.com/press</div>
        <div class="title">Booking a guest</div>
        <p>The press and podcast kit &mdash; downloadable headshots, a bio a host can read cold on
          air, topics, and past appearances.</p>
        <span class="go">Press &amp; podcast kit &rsaquo;</span>
      </a>
      <a class="card" href="https://excoadvisors.com" rel="noopener" target="_blank">
        <div class="kicker">excoadvisors.com</div>
        <div class="title">The advisory firm</div>
        <p>Writing about business exits, valuations, or the wealth transfer? The firm&rsquo;s media
          page carries the firm&rsquo;s own coverage and data.</p>
        <span class="go">Exceptional Business Advisors &rsaquo;</span>
      </a>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="eyebrow">Selected coverage</div>
    <h2 class="h1 mt2">In the press.</h2>
    <hr class="accentrule mt3">
    <div class="linklist mt4">
      {"".join('''<div class="linkrow" style="border-color:rgba(255,255,255,.22)">
        <div><div class="n"><a href="%s" rel="noopener" target="_blank">%s</a></div>
        <div class="d" style="color:rgba(255,255,255,.78)">%s</div></div>
        <div class="y" style="color:rgba(255,255,255,.65)">%s</div>
      </div>''' % (u, o, h, d) for o, h, d, u in FEATURES)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <div class="eyebrow">Permissions</div>
        <h2 class="h2 mt2">Quoting or excerpting</h2>
        <hr class="accentrule mt3">
        <p class="mt3">Short quotations for review or comment need no permission from us &mdash; a
          citation to the title and author is enough. Anything longer, any reproduction of a
          framework, worksheet or assessment, and any use in a course, cohort or corporate
          training needs our written permission. We answer quickly and we are not precious
          about it.</p>
        <p>{mail("Permissions requests", subject="Permissions%20request")}</p>
      </div>
      <div class="body">
        <div class="eyebrow">Assets</div>
        <h2 class="h2 mt2">Covers, logos, photography</h2>
        <hr class="accentrule mt3">
        <p class="mt3">We supply jacket art, author photography and the Exceptional wordmark on
          request in print resolution. We send marks as vector, and they are used solid black or
          solid white only &mdash; never recoloured, boxed, stretched, or pulled from a web page.</p>
        <p>{mail("Request assets", subject="Asset%20request%20%E2%80%94%20Exceptional%20Media")}</p>
      </div>
    </div>
  </div>
</section>
"""
write("/press/", "Press, Rights &amp; Permissions — Exceptional Media",
      "Review copies, excerpt and reprint permissions, cover art and interview requests for the "
      "books, podcasts and EXCEPTIONAL magazine published by Exceptional Media.", press, depth=1,
      schema=graph(crumbs(("Home", "/"), ("Press", "/press/")), ORG))

# ══════════════════════════════════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════════════════════════════════
about = pagehead("About", "Why we<br>publish.",
  "We are the publishing arm of Exceptional Companies &mdash; where our frameworks go once "
  "they have survived contact with a real business.") + f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="body">
        <h2 class="h2">Everything here was used before it was written down.</h2>
        <hr class="accentrule mt3">
        <p class="mt3">We are an innovation company in Colorado Springs, and we buy, build and operate
          businesses across advisory, energy, insurance, wealth and media. Every framework we
          publish was installed in one of our own companies first, and most of them broke at
          least once before they worked.</p>
        <p>That is our whole editorial standard. We publish what we run on. When a number is
          uncertain we date it and say so, and when we cannot source a statistic we leave it out
          rather than repeat it.</p>
        <p>We write for the owner who built something real with their hands, their talent and their
          years &mdash; and who intends to hand it off well rather than run out of time holding
          it.</p>
      </div>
      <div>
        <blockquote class="pull">A stranger should be able to see the piece with the logo cropped
          off and still tell it came from an Exceptional company.
          <cite>Family Brand Standards</cite></blockquote>
        <div class="mt5">
          <div class="factrow"><span class="k">Imprint</span><span>Exceptional Media</span></div>
          <div class="factrow"><span class="k">Parent</span><span>Exceptional Companies</span></div>
          <div class="factrow"><span class="k">Offices</span><span>Colorado Springs &middot; Austin &middot; Midland</span></div>
          <div class="factrow"><span class="k">Contact</span><span>{mail()}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="wrap">
    <div class="eyebrow">Our authors</div>
    <h2 class="h1 mt2">Who writes here.</h2>
    <hr class="accentrule mt3">
    <div class="grid g3 mt4">
      <div class="card card--dark">
        <div class="kicker">Founder &middot; Exceptional Companies</div>
        <div class="title">Chris Seegers</div>
        <p>Chris guides Main Street owners through the biggest transaction of their lives. He has
          been the seller, the buyer and the advisor on both sides of the table. He runs a family
          office of operating businesses, wrote <i>Selling Main Street</i> and <i>Buying Main
          Street</i>, co-wrote <i>Exceptional by Design</i> with his wife Tara, and in 2015 he and
          Tara bought the town of Hillside, Colorado.</p>
        <a class="go" href="https://chrisseegers.com" rel="noopener" target="_blank">chrisseegers.com &rsaquo;</a>
      </div>
      <div class="card card--dark">
        <div class="kicker">Co-author &middot; Exceptional Systems</div>
        <div class="title">Marcus Seegers</div>
        <p>Marcus is co-author of <i>Exceptional Systems</i> and co-leader of the ecosystem. He is
          a Co-Founder of Exceptional Business Advisors, where he owns operations and systems
          &mdash; which is to say he runs, in a real company with real people in it, the operating
          system that book documents.</p>
        <!-- Marcus has no personal paragraph in any source. Brand Standards v1.0 requires he is
             never framed as staff. Chris to supply; do not invent one. See README, open item 4. -->
      </div>
      <div class="card card--dark">
        <div class="kicker">Co-author &middot; Exceptional by Design</div>
        <div class="title">Tara Seegers</div>
        <p>Tara co-wrote <i>Exceptional by Design</i> and is co-writing <i>Exceptional
          Stewardship</i>, the Wealth OS &mdash; she is a Certified Financial Planner&trade; named
          to Forbes&rsquo; Top Women Wealth Advisors Best-In-State list. She co-leads the
          ecosystem. She
          had the vision for Hillside and ran it &mdash; within three years the town was
          immaculate, profitable and growing, with people driving in from all over for events,
          milestones and the stargazing.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--rule">
  <div class="wrap">
    <div class="eyebrow">What we publish</div>
    <h2 class="h2 mt2">Everything, in one place</h2>
    <hr class="accentrule mt3">
    <div class="grid g3 mt4">
      <a class="card" href="/books/">
        <div class="kicker">Five titles</div>
        <div class="title">The books</div>
        <p>The Life, Business and Wealth OS trilogy, and the two Main Street books on selling and
          buying a company.</p>
        <span class="go">The library &rsaquo;</span></a>
      <a class="card" href="/podcasts/">
        <div class="kicker">Two shows</div>
        <div class="title">The podcasts</div>
        <p>Conversations with owners who have built, run, or let go of a company &mdash; including
          the parts that did not work.</p>
        <span class="go">Every listening link &rsaquo;</span></a>
      <a class="card" href="/books/exceptional-by-design/excerpt/">
        <div class="kicker">Read it now</div>
        <div class="title">Chapter four, in full</div>
        <p>&ldquo;Create Your Life Vision&rdquo; from <i>Exceptional by Design</i> &mdash; getting
          quiet, and the ten-year exercise.</p>
        <span class="go">Read the chapter &rsaquo;</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">The ecosystem</div>
    <h2 class="h2 mt2">Where the material comes from</h2>
    <hr class="accentrule mt3">
    <div class="grid g4 mt4">
      <a class="card" href="https://excoadvisors.com" rel="noopener" target="_blank">
        <div class="title">Exceptional Business Advisors</div>
        <p>Sell-side and buy-side transition work. The Main Street books came straight out of it.</p>
        <span class="go">Visit &rsaquo;</span></a>
      <a class="card" href="https://www.exceptionalwealth.us" rel="noopener" target="_blank">
        <div class="title">Exceptional Wealth &amp; Family Office</div>
        <p>What happens to the family, the plan and the legacy after the wire hits &mdash; utilizing
          your resources to live the life you design.</p>
        <span class="go">Visit &rsaquo;</span></a>
      <a class="card" href="https://insureexceptional.com" rel="noopener" target="_blank">
        <div class="title">Exceptional Insurance</div>
        <p>Protection for all of it &mdash; home, auto, umbrella. Plus the life, estate, key person
          and buy-sell coverage that can turn an exit into opportunity.</p>
        <span class="go">Visit &rsaquo;</span></a>
      <a class="card" href="https://exceptionalcos.com" rel="noopener" target="_blank">
        <div class="title">Exceptional Companies</div>
        <p>An Innovation Company: the operating portfolio where the systems get stress-tested across
          industries and our own resources are deployed to live the life we designed.</p>
        <span class="go">Visit &rsaquo;</span></a>
    </div>
  </div>
</section>
"""
write("/about/", "About — Exceptional Media",
      "Exceptional Media is the publishing arm of Exceptional Companies, an innovation company in "
      "Colorado Springs. We publish what we run on.", about, depth=1,
      schema=graph(crumbs(("Home", "/"), ("About", "/about/")), ORG,
        {"@type": "AboutPage", "url": SITE + "/about/", "name": "About Exceptional Media",
         "isPartOf": {"@id": SITE + "/#site"}}))

# ══════════════════════════════════════════════════════════════════════════
# 404 + robots + sitemap
# ══════════════════════════════════════════════════════════════════════════
nf = pagehead("404", "Not here.",
  "That page has moved or never existed. Start from the library, or tell us what you were "
  "looking for.") + f"""
<section class="section">
  <div class="wrap">
    <div class="btnrow">
      <a class="btn" href="/books/">The books</a>
      <a class="btn btn--ghost" href="/">Home</a>
      {mail("Email us", cls="btn btn--ghost")}
    </div>
    <div class="mt5">
      <div class="eyebrow">Everything on this site</div>
      <div class="linklist mt3">
        <div class="linkrow"><div><div class="n"><a href="/books/">Books</a></div>
          <div class="d">Five titles &mdash; the trilogy and the Main Street books</div></div></div>
        <div class="linkrow"><div><div class="n"><a href="/books/exceptional-by-design/excerpt/">Chapter four, in full</a></div>
          <div class="d">&ldquo;Create Your Life Vision&rdquo; from <i>Exceptional by Design</i></div></div></div>
        <div class="linkrow"><div><div class="n"><a href="/podcasts/">Podcasts</a></div>
          <div class="d">Both shows, every listening link</div></div></div>
        <div class="linkrow"><div><div class="n"><a href="/press/">Press, rights and permissions</a></div>
          <div class="d">Review copies, excerpts, cover art</div></div></div>
        <div class="linkrow"><div><div class="n"><a href="/about/">About</a></div>
          <div class="d">The imprint and the authors</div></div></div>
      </div>
    </div>
  </div>
</section>
"""
(ROOT / "404.html").write_text(head("Page not found — Exceptional Media",
  "That page has moved or never existed.", "/404", 0) + nf + FOOT, encoding="utf-8")
print("  wrote 404.html")

PAGES = (["/", "/books/", "/books/exceptional-by-design/",
          "/books/exceptional-by-design/excerpt/",
          "/books/exceptional-by-design/press/", "/books/exceptional-systems/",
          "/books/exceptional-systems/press/",
          "/books/exceptional-stewardship/", "/podcasts/"]
         + (["/magazine/"] if MAGAZINE_PROMOTED else [])
         + ["/press/", "/about/"])
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in PAGES:
    pri = "1.0" if p == "/" else ("0.9" if p.startswith("/books") else "0.7")
    sm.append(f"  <url><loc>{SITE}{p}</loc><changefreq>monthly</changefreq><priority>{pri}</priority></url>")
sm.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
print("  wrote sitemap.xml, robots.txt")
print("done.")
