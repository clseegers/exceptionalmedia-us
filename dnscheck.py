#!/usr/bin/env python3
"""Go-live verifier for exceptionalmedia.us.
Checks DNS, HTTPS and the certificate on both hostnames. Run until everything is green.

Run it from a normal connection. On a corporate network that inspects TLS, the certificate
check sees the proxy's certificate rather than the site's; the script says so when it detects
one. The DNS checks are accurate anywhere.

    python3 dnscheck.py            # needs: pip install dnspython
"""
import socket, ssl, sys, urllib.request

DOMAIN = "exceptionalmedia.us"
ACCOUNT = "clseegers"
GH_A = {"185.199.108.153", "185.199.109.153", "185.199.110.153", "185.199.111.153"}
PARKED = {"76.223.105.230", "13.248.243.5"}

OK, BAD, WAIT = "  ok  ", " FAIL ", " wait "
issues = []

def line(state, label, detail=""):
    print(f"[{state}] {label}" + (f"  —  {detail}" if detail else ""))
    if state is BAD:
        issues.append(label)

def addrs(host):
    try:
        return {i[4][0] for i in socket.getaddrinfo(host, None, socket.AF_INET)}
    except Exception:
        return set()

print(f"\nGo-live check — {DOMAIN}\n" + "-" * 58)

# 1 · apex A records
a = addrs(DOMAIN)
if not a:
    line(BAD, "apex resolves", "no A record at all")
elif a & PARKED:
    line(BAD, "apex A records", f"still on GoDaddy parking: {', '.join(sorted(a & PARKED))}"
                                " — delete the old A record, and check Forwarding is off")
elif a == GH_A:
    line(OK, "apex A records", "all four GitHub Pages IPs")
elif a < GH_A:
    line(WAIT, "apex A records", f"only {len(a)} of 4 present: {', '.join(sorted(a))}")
else:
    line(BAD, "apex A records", f"unexpected: {', '.join(sorted(a))}")

# 2 · www
try:
    import dns.resolver
    r = dns.resolver.Resolver(); r.nameservers = ["8.8.8.8"]; r.lifetime = 10
    cn = [x.to_text().rstrip(".") for x in r.resolve("www." + DOMAIN, "CNAME")]
    if cn == [f"{ACCOUNT}.github.io"]:
        line(OK, "www CNAME", cn[0])
    elif cn == [DOMAIN]:
        line(BAD, "www CNAME", f"still points at the apex — set it to {ACCOUNT}.github.io")
    else:
        line(BAD, "www CNAME", f"unexpected: {', '.join(cn)}")
except ImportError:
    w = addrs("www." + DOMAIN)
    line(OK if w == GH_A else WAIT, "www resolves", ", ".join(sorted(w)) or "nothing")
    print("        (pip install dnspython for the exact CNAME check)")
except Exception as e:
    line(BAD, "www CNAME", f"no CNAME found ({type(e).__name__})")

# 3 · HTTPS + certificate on both hostnames.
#     A certificate alone proves nothing — GoDaddy's parking serves a valid one too. What
#     matters is who ISSUED it. GitHub Pages certificates come from Let's Encrypt.
dns_ready = (a == GH_A)
for host in (DOMAIN, "www." + DOMAIN):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ss:
                cert = ss.getpeercert()
        issuer = dict(x[0] for x in cert.get("issuer", ())).get("organizationName", "?")
        if issuer not in ("Let's Encrypt", "GoDaddy.com, Inc.", "Amazon", "DigiCert Inc", "?"):
            line(WAIT, f"certificate on {host}",
                 f"issued by {issuer} — that is a TLS-inspecting proxy on this network, "
                 "not the site's real certificate. Run this from an unfiltered connection.")
            continue
        if not dns_ready:
            line(WAIT, f"certificate on {host}",
                 f"issued by {issuer} — this is still the parking cert, not GitHub's")
        elif "Let's Encrypt" in issuer:
            line(OK, f"certificate on {host}", f"issued by {issuer}")
        else:
            line(WAIT, f"certificate on {host}",
                 f"issued by {issuer} — GitHub's has not replaced it yet")
    except ssl.SSLCertVerificationError as e:
        line(BAD, f"certificate on {host}",
             f"{e.verify_message} — wait, or remove and re-save the custom domain")
    except Exception as e:
        line(WAIT, f"https://{host}", f"not answering yet ({type(e).__name__})")

    try:
        req = urllib.request.Request(f"https://{host}", headers={"User-Agent": "dnscheck"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            body = resp.read(4000).decode("utf-8", "replace")
        if "Exceptional Media" in body:
            line(OK, f"{host} serves the site", f"HTTP {resp.status}")
        else:
            line(BAD, f"{host} serves the site", "responds, but this is not our page — parked?")
    except Exception as e:
        line(WAIT, f"{host} serves the site",
             f"{type(e).__name__} — no answer yet, or this network blocks outbound HTTPS")

print("-" * 58)
if issues:
    print(f"{len(issues)} thing(s) to fix. See DEPLOY.md.\n")
    sys.exit(1)
print("All green. Check 'Enforce HTTPS' is ticked in Settings > Pages, then ship the link.\n")
