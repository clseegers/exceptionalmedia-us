#!/usr/bin/env bash
#
#  autopush.sh — start this once, leave it running, and edits ship themselves.
#
#      cd ~/Projects/exceptionalmedia-us && ./autopush.sh
#
#  Why this exists: Claude can write files and make commits in this folder, but the
#  sandbox it works in has no network and no access to your SSH key. It cannot push.
#  This script runs on YOUR machine with YOUR key, so nothing has to hand a credential
#  to anything. It watches for work landing in the repo and pushes it.
#
#  It will NOT push a broken build. check.py runs first; if it fails, the script says
#  so and waits rather than shipping it.
#
#  Ctrl-C to stop. Safe to start and stop whenever.
#
set -uo pipefail
cd "$(dirname "$0")" || exit 1

INTERVAL="${1:-20}"          # seconds between checks
B=$'\033[1m'; D=$'\033[2m'; G=$'\033[32m'; Y=$'\033[33m'; R=$'\033[31m'; N=$'\033[0m'

ts() { date "+%H:%M:%S"; }
say() { printf '%s %s\n' "${D}$(ts)${N}" "$1"; }

command -v git >/dev/null || { echo "git not found"; exit 1; }
git rev-parse --git-dir >/dev/null 2>&1 || { echo "not a git repo"; exit 1; }

printf '\n%s\n' "${B}exceptionalmedia.us — autopush${N}"
printf '%s\n' "${D}watching $(pwd)${N}"
printf '%s\n' "${D}checking every ${INTERVAL}s · ctrl-c to stop${N}"
printf '%s\n\n' "${D}a failing build check stops the push, it does not ship${N}"

idle_note_shown=0

while true; do

  # 1 · uncommitted work left in the tree — build, gate, commit it
  if [ -n "$(git status --porcelain)" ]; then
    idle_note_shown=0
    say "${Y}changes detected${N} — rebuilding"

    if ! python3 build.py >/dev/null 2>&1; then
      say "${R}build.py failed${N} — not committing. Fix it, or ask Claude."
      sleep "$INTERVAL"; continue
    fi
    if ! python3 check.py >/dev/null 2>&1; then
      say "${R}check.py failed${N} — not committing. Run: python3 check.py"
      sleep "$INTERVAL"; continue
    fi

    git add -A
    git commit -q -m "Site update $(date '+%Y-%m-%d %H:%M')" \
      -m "Committed by autopush.sh after build.py and check.py passed." \
      && say "${G}committed${N}"
  fi

  # 2 · anything ahead of the remote — push it
  ahead=$(git rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)
  if [ "${ahead:-0}" -gt 0 ]; then
    idle_note_shown=0
    say "pushing ${B}${ahead}${N} commit(s)…"
    if git push --quiet; then
      say "${G}pushed${N} — GitHub Actions is deploying"
      say "${D}  https://github.com/clseegers/exceptionalmedia-us/actions${N}"
    else
      say "${R}push failed${N} — check your connection, then it will retry"
    fi
  elif [ "$idle_note_shown" -eq 0 ]; then
    say "${D}up to date${N}"
    idle_note_shown=1
  fi

  sleep "$INTERVAL"
done
