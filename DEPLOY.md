# Taking exceptionalmedia.us live

GitHub Pages, same as chrisseegers.com. Free, no vendor, and the workflow you already know.
Fifteen minutes, most of it waiting on DNS.

**What I already did:** the repo is initialised and committed, `CNAME` holds the domain, a deploy
action is in `.github/workflows/deploy.yml`, and `check.py` runs in CI so nothing ships that fails
a check. **What I could not do:** push, or touch DNS. No credentials here, and I would not want them.

---

## 1 · Create the repo and push

```bash
cd exceptionalmedia
git remote add origin git@github.com:<your-account>/exceptionalmedia.git
git branch -M main
git push -u origin main
```

Make the repo **public** if the account is on a free plan — Pages needs public there. Private is
fine on Pro/Team/Enterprise.

## 2 · Turn Pages on

Repo → **Settings → Pages → Build and deployment → Source: GitHub Actions**.

That's the only setting. Don't pick "Deploy from a branch" — the action builds the site from
`build.py` first, so a branch deploy would ship whatever HTML happened to be committed instead of
what the generator produces.

Push once more (or **Actions → Deploy to GitHub Pages → Run workflow**) and it builds. Watch the
run; `check.py` fails the build loudly if anything is wrong.

## 3 · Point the DNS at Route 53

`exceptionalmedia.us` currently answers on `13.248.243.5` and `76.223.105.230` — AWS parking.
Those records go away.

In the Route 53 hosted zone for `exceptionalmedia.us`:

**Delete** the existing apex A record (the parking one).

**Create — apex, type A**, name blank, TTL 300, four values:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Create — apex, type AAAA**, name blank, TTL 300, four values:

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

**Create — www, type CNAME**, name `www`, TTL 300, value:

```
<your-account>.github.io
```

(The literal account name plus `.github.io`. Not the repo name, and no trailing path.)

## 4 · Finish in GitHub

Settings → Pages → **Custom domain**: `exceptionalmedia.us` → Save. It re-checks DNS; the green
tick can take up to an hour.

Then tick **Enforce HTTPS**. It greys out until the certificate issues — usually minutes, sometimes
a few hours. Don't skip it, and don't announce the site before it's on.

## 5 · Check both hostnames before you send the link anywhere

```
https://exceptionalmedia.us
https://www.exceptionalmedia.us
```

**Both.** A www variant that isn't covered by the certificate is the most common way a launch link
"doesn't work" for the one person you most wanted to see it.

---

## Afterwards

**To change anything**, edit `build.py` (or `assets/exco-media.css`), commit, push. The action
rebuilds and redeploys. Never edit the `.html` files — the next build overwrites them.

**To check locally before pushing:**

```bash
python3 build.py && python3 check.py && python3 -m http.server 8000
```

**To turn the magazine on** when EXCEPTIONAL clears its blockers: set `MAGAZINE_PROMOTED = True`
at the top of `build.py` and push. That one switch restores the nav item, the footer link, the
home call-to-action, the sitemap entry and indexing.

**To change the contact address:** `MAIL_U` / `MAIL_D` at the top of `build.py`.

**Once it's live**, submit `https://exceptionalmedia.us/sitemap.xml` in Google Search Console and
Bing Webmaster Tools, and add the domain to the Google Business Profile if it belongs there.
