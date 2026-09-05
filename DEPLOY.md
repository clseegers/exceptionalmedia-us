# Taking exceptionalmedia.us live

GitHub Pages, DNS at GoDaddy — **the identical setup chrisseegers.com already runs on.** You have
done this before; this is the same three moves.

## What's already true

| | |
|---|---|
| Registrar / DNS | **GoDaddy** — nameservers `ns53.domaincontrol.com`, `ns54.domaincontrol.com` |
| GitHub account | **`clseegers`** |
| Domain today | Parked. Apex A → `76.223.105.230`, `13.248.243.5` (GoDaddy parking). `www` is a CNAME to the apex, so it parks too. |
| Target | Apex A → GitHub's four IPs · `www` CNAME → `clseegers.github.io` — **exactly what chrisseegers.com has** |

Repo is initialised and committed. `CNAME` holds the domain. `.github/workflows/deploy.yml`
rebuilds from `build.py` and runs `check.py` before every deploy.

---

## 1 · Push the repo

```bash
cd exceptionalmedia
git remote add origin https://github.com/clseegers/exceptionalmedia-us.git
git push -u origin main
```

Create the repo first at **github.com/new** — owner `clseegers`, name `exceptionalmedia-us`, and
**do not** add a README, .gitignore, or licence. This repo already has all three, and GitHub's
starter files would collide on the first push.

Make it **public** unless the account is on a paid plan. Pages needs public on Free.

> `clseegers.github.io` is your *user site* — almost certainly chrisseegers.com. You can only have
> one of those, but unlimited **project sites**, each with its own domain. This is a project site.
> That changes nothing below.

## 2 · Turn Pages on

Repo → **Settings → Pages → Build and deployment → Source: GitHub Actions**.

That is the only setting on this screen. **Do not pick "Deploy from a branch."** A branch deploy
ships whatever HTML is sitting in the repo instead of what `build.py` produces, which quietly
defeats the whole build.

Then **Actions → Deploy to GitHub Pages → Run workflow**. Watch it. `check.py` fails the build
loudly rather than shipping something broken.

## 3 · Repoint DNS at GoDaddy

**GoDaddy → My Products → Domains → `exceptionalmedia.us` → DNS → DNS Records.**

### Delete these two

| Type | Name | Value |
|---|---|---|
| A | `@` | `76.223.105.230` *(and/or `13.248.243.5` — parking)* |
| CNAME | `www` | `@` *(GoDaddy's default; it inherits the parking)* |

### Add these five

| Type | Name | Value | TTL |
|---|---|---|---|
| A | `@` | `185.199.108.153` | 600 |
| A | `@` | `185.199.109.153` | 600 |
| A | `@` | `185.199.110.153` | 600 |
| A | `@` | `185.199.111.153` | 600 |
| CNAME | `www` | `clseegers.github.io` | 600 |

Four separate A records, all named `@`. GoDaddy allows that — add them one at a time. Set TTL to
**600 seconds** (Custom) while you're switching, so a mistake costs ten minutes instead of an hour.
Raise it to an hour once it's working.

Optional, and worth doing — **AAAA on `@`**, same four-record pattern, for IPv6 visitors:
`2606:50c0:8000::153` · `2606:50c0:8001::153` · `2606:50c0:8002::153` · `2606:50c0:8003::153`.
(chrisseegers.com doesn't have these and works fine. It's an improvement, not a requirement.)

### ⚠ Then check Forwarding is OFF

**Domain Settings → Forwarding.** If domain forwarding or a parked page is on, GoDaddy silently
re-inserts its own A record and overrides everything you just did. This is the single most common
way a GoDaddy → GitHub move looks like it worked and then doesn't. Turn it off before you leave
the page.

Same for **Websites + Marketing / Airo** — if either has claimed this domain, detach it.

## 4 · Finish in GitHub

Settings → Pages → **Custom domain** → `exceptionalmedia.us` → Save.

GitHub re-checks DNS and shows a green tick. Then tick **Enforce HTTPS** — it stays greyed out
until the certificate issues, usually minutes, occasionally a few hours. Don't announce the site
before that tick is on.

## 5 · Verify both hostnames

```bash
python3 dnscheck.py
```

That script (in the repo) checks the apex, `www`, HTTPS on both, and the certificate. Run it until
everything is green.

**Both hostnames.** A `www` that isn't covered by the certificate is the most common way a launch
link fails for exactly the person you most wanted to see it.

---

## Autopush — start it once, leave it running

```bash
cd ~/Projects/exceptionalmedia-us && ./autopush.sh
```

Leave that Terminal window open. It checks every twenty seconds, and when work lands in the repo
it rebuilds, runs the gate, commits anything loose, and pushes. GitHub Actions takes it from there.

**It will not push a broken build.** `check.py` runs first; a failure stops the push and says so
rather than shipping it.

**Why this exists.** Claude can write files and make commits in this folder through the desktop
bridge, but the sandbox it works in has no network and no access to your SSH key — it can see the
connected folder and nothing else in your home directory. It physically cannot push. This script
runs on your machine with your key, so no credential ever has to be handed to anything.

Ctrl-C stops it. Safe to start and stop whenever. `./autopush.sh 60` to check every minute instead.

---

## Afterwards

**To change anything:** edit `build.py` or `assets/exco-media.css`, commit, push. The action
rebuilds and redeploys. Never edit the `.html` files — the next build overwrites them.

**Locally:** `python3 build.py && python3 check.py && python3 -m http.server 8000`

**Turn the magazine on** when EXCEPTIONAL clears its blockers: `MAGAZINE_PROMOTED = True` at the
top of `build.py`, then push. One switch restores the nav item, footer link, home CTA, sitemap
entry and indexing.

**Change the contact address:** `MAIL_U` / `MAIL_D` at the top of `build.py`.

**Once live:** submit `https://exceptionalmedia.us/sitemap.xml` to Google Search Console and Bing
Webmaster Tools. While you're in Search Console, note that chrisseegers.com carries a
`google-site-verification` TXT record — you'll want the equivalent here.

---

## If something goes wrong

| Symptom | Cause |
|---|---|
| Still shows the parked page after an hour | Forwarding is still on, or the old A record wasn't deleted. Check step 3's warning. |
| GitHub says "domain does not resolve to the GitHub Pages server" | DNS hasn't propagated, or an A record has a typo. Run `dnscheck.py`. |
| "Enforce HTTPS" stays greyed out | Certificate hasn't issued. It needs correct DNS first. Wait, then remove and re-save the custom domain to retrigger. |
| `www` works, apex doesn't (or vice versa) | You have one half of step 3. Both the A records and the `www` CNAME are needed. |
| Site is live but stale | You edited `.html` instead of `build.py`, and the action regenerated over it. |
