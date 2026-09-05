# exceptionalmedia.us

The media house of Exceptional Companies. Static site — no build step required to deploy,
no framework, no JavaScript.

Built to **Exceptional Companies Family Brand Standards v1.0**, parent treatment with the
Signature Gold accent — the same resolution the EXCEPTIONAL magazine landed on, because a
cross-family piece cannot wear one entity's accent.

---

## What's here

```
/                                   Home — the whole catalogue in one scroll
/books/                             Five titles: the trilogy + the Main Street books
/books/exceptional-by-design/       Book one · the Life OS · published
/books/exceptional-systems/         Book two · the Business OS · forthcoming 2027
/books/exceptional-stewardship/     Book three · the Wealth OS · in development
/podcasts/                          Both shows, every listening link
/magazine/                          EXCEPTIONAL quarterly — the four-issue pipeline
/press/                             Rights, permissions, review copies, coverage
/about/                             The imprint and the authors
404.html · robots.txt · sitemap.xml
assets/exco-media.css               One stylesheet, ~260 lines, all tokens at the top
build.py                            Regenerates every page. Edit here, not the HTML.
check.py                            Build gate — runs in CI, fails the deploy on any problem
make_preview.py                     Bundles the site into one shareable preview.html
DEPLOY.md                           Go-live steps and the exact GoDaddy DNS records
dnscheck.py                         Verifies DNS, HTTPS and the certificate after the switch
.github/workflows/deploy.yml        Build, check, deploy on push to main
CNAME · .nojekyll · .gitignore
books/exceptional-by-design/excerpt/   Chapter four, in full
```

**Edit `build.py`, not the `.html` files.** Every page shares one header, one footer, and one
set of components. Run `python3 build.py` to regenerate. Change the design once for every page
by editing `assets/exco-media.css`.

## Deploy

**See `DEPLOY.md`** — step by step, with the exact GoDaddy records.

Short version: GitHub Pages under the `clseegers` account, DNS at GoDaddy — the identical setup
chrisseegers.com already runs on. The repo is initialised and committed, `CNAME` holds the domain,
and `.github/workflows/deploy.yml` regenerates from `build.py` and runs `check.py` before every
deploy. Push, set Pages source to **GitHub Actions**, replace GoDaddy's parking A record with
GitHub's four IPs, point `www` at `clseegers.github.io`, turn GoDaddy Forwarding **off**, and
enforce HTTPS. `python3 dnscheck.py` verifies the whole thing.

Local: `python3 build.py && python3 check.py && python3 -m http.server 8000`

---

## Open items — settle these before launch

**1 · No vector logo exists.** Every lockup on this site is typographic (Bebas Neue + Montserrat),
which is the same call the magazine made and for the same reason. When a real SVG arrives, swap
the `<a class="lockup">` block in `build.py`'s `head()` for an inline SVG at 0.5× clear space.
Standards require SVG in the header, never a PNG.

**2 · ~~The third book's title~~ — RULED, Sept 5.** *Exceptional Stewardship* is the **book**.
*Exceptional Wealth OS* is the **system it installs**. The two are not alternative names for the
same thing, and the publisher packet's "Wealth OS" entry is the system, not the title. The site
now carries the distinction on every book: each title has a `System` row in its fact table, and
the trilogy reads *Exceptional Life OS · Exceptional Business OS · Exceptional Wealth OS*.
**Correct the publisher packet to match.**

**3 · Compliance stop on the Stewardship page.** Wealth-side content is governed by the brand
standard **plus FINRA/SEC**. Before that page publishes, compliance supplies disclosure language
to be set unaltered — Montserrat 400, 6–7pt, gray, at the foot. The winged-horse mark is
prohibited on wealth-side pieces; this site is wordmark-only throughout, so that part is clear.

**4 · ~~The author line on *Exceptional Systems*~~ — RULED, Sept 5.** Marcus Seegers is
**co-author**. The book page, the catalogue cards, the meta description and the About page all
name him. He appears on About as a co-author and co-leader, never as staff, per Brand Standards
v1.0. **Still open:** Marcus has no personal paragraph in any source — the EBA bio standard flags
the same gap. His card carries only what is sourced. Chris supplies the paragraph; do not invent
one. The same gap exists for Caleb.

**4b · Who writes *Exceptional Stewardship*?** With Tara co-authoring book one and Marcus book
two, the byline on book three is a fair question. The page currently reads "Chris Seegers."

**5 · The magazine page runs ahead of the magazine.** The handoff lists five blockers on
EXCEPTIONAL, and Issues 02–04 have not been adversarially fact-checked. This page carries no
prototype language, no rate card and no issue-level article claims beyond the editorial calendar
— but do not drive traffic to it until Blockers 1–5 clear.

**6 · Book covers are placeholder fields.** The `.coverframe` blocks render the energy device in
Signature Gold with a dark scrim for the type. Each has a commented `<img>` slot — drop jacket
art at `/assets/covers/` and the placeholder disappears.

**7 · Retail links.** Selling Main Street and Buying Main Street link to Amazon. The trilogy pages
carry "notify me" mailtos instead, because no retail listing has been confirmed for
*Exceptional by Design*. Add real buy links as they go live.

---

## Deliberate decisions worth knowing

**This is not a third press page.** `chrisseegers.com/press` is the booking kit for producers.
`excoadvisors.com/media` is the proof page for sellers. Those two were kept apart on purpose so
they don't cannibalize each other. `/press/` here is the **rights and permissions desk** for the
publications — review copies, excerpts, cover art — and it links out to the other two rather than
repeating them. Keep it that way.

**No disputed figures appear anywhere on this site.** Subscriber counts (212,000 vs 132K),
episode counts (61 vs 85+) and the business count (ten vs eleven) are all unresolved in the
record, so none of them are printed. Nothing here goes stale while the counts get settled.

**Nothing from the prohibited list appears.** No royalty acreage, no $100M energy deals, no $550M,
no CEPA, no "legally blind," no "#1 business podcast," no "Built on purpose.", and no variation on
rejecting mediocrity. A scan is part of the build check.

**Fonts.** Bebas Neue · Montserrat · Quattrocento · Roboto, from Google Fonts, with real fallback
stacks on every family. That is four families where the standard says three maximum — the same
judgment call the magazine made, and Outfit was dropped here to get closer to it. If Google Fonts
is ever blocked on the host, self-host the four files and swap the `<link>`; the fallbacks mean the
page degrades legibly rather than breaking.

**Energy lines never sit behind body copy.** The device runs as a right-edge band on dark headers
and a top band in the footer, both bleeding off at least one edge at a fixed 30°, one color. It is
hidden below 820px, where copy would run under it.

**Square corners, everywhere.** `--radius: 0`. Signature Gold is a rule and a fill only — it fails
contrast as type at 1.74:1 and is never used for text or a button label.


**9 · Which insurance entity is this, and does it need a disclosure?** Brand Standards v1.0 lists
two: **Exceptional Insurance Group** (Allstate Blue, and *Allstate brand standards govern —
where Allstate and our standard disagree, Allstate wins*) and **Exceptional. Insurance ·
Protection** (Shelter Sage, wordmark only, wealth-side compliance stop). `insureexceptional.com`
brands itself simply "Exceptional Insurance" and does not mention Allstate anywhere on the page.
The site uses "Exceptional Insurance," matching both that site and chrisseegers.com. **Rule which
entity this is before launch** — it decides whether Allstate's standards apply to how the name and
mark are presented, and whether the insurance mentions need disclosure text. The site makes no
coverage claim and gives no advice; it names lines the agency's own site states. A commented
disclosure slot sits above the home practices strip in `build.py`.

---

## VOICE — plural, ruled Sept 5

The site speaks as **we**, not I. Every line that speaks for the house is first-person plural:
"We are a family office…", "We publish what we run on", "We handle bulk orders directly",
"We supply jacket art…".

Two consequences worth knowing:

- **The *Selling Main Street* pull quote changed.** It was *"I am in the people business. My
  mission is…"* — the only literal "I" on the site. Rather than misquote the book, the page now
  runs the plural half of the same passage: *"We treat every client as a human being and a friend,
  not a transaction. We didn't start this business as a profit center."*
- **Author bios stay in the third person.** A bio of one named person reads wrong in "we" — Chris,
  Marcus and Tara each get he/she on the About page. Say the word and they convert, but the
  recommendation is to leave them.

The one place "me" survives is the launch-notification button, where the visitor is the one
speaking: *"Send me launch updates."* That is the reader's voice, not ours.


---

## EXCEPTIONAL INSURANCE — threaded, Sept 5

Chris ruled that Insurance runs through the site, not just the footer. It is placed where it does
real work rather than sprinkled:

- **Home** — a practices strip directly under the hero: four practices, each named and linked,
  each with one line on what it contributes. Insurance carries the concrete one: *"home, auto,
  life and umbrella, plus the key person and buy-sell cover that makes a business transferable at
  all."* This strip is also the fix for the ecosystem having been footer-only.
- **Magazine** — the publisher line now reads *"jointly serving Exceptional Business Advisors,
  Exceptional. Wealth · Family Office, and Exceptional Insurance."* A second line says where
  protection sits without breaking the tagline: the verticals stay three, and protection runs
  **underneath WEALTH rather than beside it** — a buy-sell that is not funded is not a plan.
- **Exceptional Stewardship** — protection is written into the Wealth OS, not an appendix.
  Stewardship is what survives you being wrong, or unlucky, or gone.
- **Exceptional Systems** — the funded buy-sell and key person cover are named as part of what
  makes an exit possible. *A business nobody can buy is not an asset.*
- **About** — the ecosystem card carries the real lines instead of a generic sentence.
- **Press** — added to the subjects a journalist would call about: *how a buy-sell actually gets
  funded.*

**Why buy-sell is the hinge.** It is the one insurance product that is squarely a business-exit
instrument, which makes it the honest bridge between Insurance and a publisher of exit books.
Every mention on the site routes through it rather than through generic "protection" language.


---

## EMAIL — info@exceptionalcos.com, obfuscated

Every contact point on the site is **info@exceptionalcos.com**. The address is **never written
literally into the served HTML.**

**How it works.** Each contact link is `<a class="mail" data-u="info" data-d="exceptionalcos.com"
data-s="<subject>" href="#contact-email">`. A ten-line script in the shared footer joins the user
and domain with `String.fromCharCode(64)` at load and writes the real `mailto:`. Nothing in the
source contains an `@` next to a domain, so `grep`, `curl`, and every regex harvester come up
empty. Verified: a scan of all ten built pages for `[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}` and
for `mailto:` returns zero hits.

**How it degrades.** With JavaScript off, contact links jump to the footer, where the address is
printed as `info [at] exceptionalcos [dot] com` — readable by a person, not by a scraper. Nothing
is broken, nothing is hidden.

**Be honest about the limit.** This defeats source scrapers and regex harvesters, which is the
overwhelming majority of address harvesting. It does **not** defeat a harvester that runs a real
browser and executes the page, because at that point the address exists in the DOM. There is no
client-side technique that does. If the volume ever justifies more, the next step is a server-side
contact form with a spam filter, which needs a backend this site deliberately does not have.

**One tradeoff worth stating.** The site previously had zero JavaScript. It now has ten lines,
inline in the footer, running on every page. That is the price of the obfuscation. Subject lines
are preserved on all eleven links — the press desk, permissions, asset requests, the two launch
notifications, the magazine copy request and media kit, and the podcast guest pitch all still
arrive pre-labelled.

**To change the address**, edit `MAIL_U` and `MAIL_D` at the top of `build.py` and rebuild. It is
in one place.


---

## BUILT OUT — Sept 5, deeper book pages

**Real tables of contents.** *Exceptional by Design* carries its full seventeen chapters across
four phases, transcribed from `Exceptional_by_Design_4-13-26.docx`. *Exceptional Systems* carries
the fifteen-chapter structure from the redline spec's "New Table of Contents (Locked)."

**Chapter four, in full, at `/books/exceptional-by-design/excerpt/`.** "Create Your Life Vision" —
Getting Quiet and the ten-year vision exercise, reproduced verbatim. Not a teaser; a sample that
stops at the interesting part is not a sample. Linked from the book page and the catalogue.

**Bulk and institutional orders** on every book page and on `/books/` — volume, licensing for
cohort or classroom use, and examination copies, each with a pre-labelled email subject.

**Note on the excerpt's voice.** The chapter is first-person singular because that is the
*authors'* voice in the book. The site's plural rule governs our own copy, not quoted book text.
`check.py` passes it; do not "fix" it.

---

## MORE OPEN ITEMS FROM THE BUILD-OUT

**10 · Clear the *Exceptional Systems* table of contents.** It comes from a redline spec, an
internal working document. The structure is marked locked, but publishing it commits you publicly
to that structure while the text is still in edit. Chris signs off or it comes down.

**11 · Clear the excerpt.** Publishing chapter four pre-launch is a real decision, not a formatting
one. Confirm before the site goes public.

**12 · Which excerpt?** I used chapter four rather than the Introduction. The Introduction tells
the story of Tara's April 2020 health emergency — that is the authors' story to place, and putting
a family medical emergency on a marketing page is Chris and Tara's call, not mine. Chapter four is
also the stronger sales excerpt. Say the word and the Introduction goes up instead.

**13 · Endorsements.** The component is built and renders the moment it has data —
`ENDORSEMENTS[slug] = [(quote, name, title), ...]` at the top of `build.py`. It is empty because no
endorsement exists in any source, and one is not inventable. A book page without praise at launch
is a soft spot worth closing.

**14 · No excerpt for *Exceptional Systems* or *Exceptional Stewardship*.** Systems is mid-revision
per the redline; Stewardship has no manuscript. Both would need clearance and text.
