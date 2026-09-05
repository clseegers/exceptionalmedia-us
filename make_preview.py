#!/usr/bin/env python3
"""Bundles the built site into one self-contained preview.html (hash routing).
For sharing a link before DNS exists. Not the deploy artifact — that is the folder itself."""
import re, pathlib
root = pathlib.Path(__file__).parent
css = (root/'assets/exco-media.css').read_text()
PAGES = [("/", "home"), ("/books/", "books"),
         ("/books/exceptional-by-design/", "books-exceptional-by-design"),
         ("/books/exceptional-by-design/excerpt/", "books-exceptional-by-design-excerpt"),
         ("/books/exceptional-by-design/press/", "books-exceptional-by-design-press"),
         ("/books/exceptional-systems/", "books-exceptional-systems"),
         ("/books/exceptional-systems/press/", "books-exceptional-systems-press"),
         ("/books/exceptional-stewardship/", "books-exceptional-stewardship"),
         ("/podcasts/", "podcasts"), ("/magazine/", "magazine"),
         ("/press/", "press"), ("/about/", "about")]
# magazine stays in the preview so Chris can see it, even though the live nav omits it
if "/magazine/" not in dict(PAGES).keys(): pass
SLUG = dict(PAGES)
src = (root/'index.html').read_text()
header = re.search(r'(<header class="masthead">.*?</header>)', src, re.S).group(1)
footer = re.search(r'(<footer class="foot">.*?</footer>)', src, re.S).group(1)
def rewrite(h):
    return re.sub(r'href="(/[^"]*)"',
                  lambda m: 'href="#%s"' % SLUG[m.group(1)] if m.group(1) in SLUG else m.group(0), h)
sections = []
for path, slug in PAGES:
    body = (root/(path.lstrip('/')+'index.html')).read_text()
    inner = body.split('</header>',1)[1].split('<footer class="foot">',1)[0]
    sections.append('<section class="vpage" id="%s"%s>\n%s</section>' %
                    (slug, '' if slug=='home' else ' hidden', rewrite(inner)))
out = f"""<title>Exceptional Media</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300;400;600&family=Quattrocento:wght@400;700&family=Roboto:wght@300;400;500&display=swap">
<style>
{css}
.previewbar{{background:#1E2E45;color:rgba(255,255,255,.82);font-family:var(--font-primary);
  font-weight:600;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;
  text-align:center;padding:9px 16px}}
.previewbar b{{color:var(--accent);font-weight:600}}
.vpage[hidden]{{display:none!important}}
html{{scroll-behavior:smooth}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}*{{animation:none!important;transition:none!important}}}}
</style>

<div class="previewbar">Design preview <b>&middot;</b> exceptionalmedia.us <b>&middot;</b> not yet live</div>
{rewrite(header)}
<main>
{chr(10).join(sections)}
</main>
{rewrite(footer)}

<script>
(function () {{
  var ids = {[s for _, s in PAGES]!r};
  function show(id) {{
    if (ids.indexOf(id) === -1) id = 'home';
    ids.forEach(function (i) {{ var el = document.getElementById(i); if (el) el.hidden = (i !== id); }});
    document.querySelectorAll('.nav a').forEach(function (a) {{
      var t = (a.getAttribute('href') || '').replace('#', '');
      if (t === id || id.indexOf(t + '-') === 0) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    }});
    window.scrollTo({{ top: 0, behavior: 'auto' }});
  }}
  window.addEventListener('hashchange', function () {{ show((location.hash || '#home').slice(1)); }});
  show((location.hash || '#home').slice(1));
}})();
</script>
"""
(root/'preview.html').write_text(out)
print("preview.html", len(out), "bytes")
