#!/usr/bin/env bash
# Fetch the tools the skills need, on THIS machine (nothing heavy lives in the repo).
#   ./tools/install.sh                     # list everything in tools.json
#   ./tools/install.sh ffmpeg latentsync   # install those by name
#   ./tools/install.sh --category lipsync  # a whole category
#   ./tools/install.sh --all               # everything (big!)
# git tools are shallow-cloned into tools/_downloads/<name> (gitignored). Needs python3.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
DL="$HERE/_downloads"; mkdir -p "$DL"
PY=python3; command -v python3 >/dev/null 2>&1 || PY=python

"$PY" - "$HERE/tools.json" "$@" <<'EOF' | while IFS='|' read -r name kind id url note; do
import json, sys
sys.stdout.reconfigure(newline="\n")
m = json.load(open(sys.argv[1], encoding="utf-8"))["tools"]
args = sys.argv[2:]
if not args:
    for t in sorted(m, key=lambda t: (t["category"], t["name"])):
        print("LIST|%s|%s|%s|%s" % (t["category"], t["name"], t["kind"], t["url"]))
    sys.exit()
if args[0] == "--all": sel = m
elif args[0] == "--category": sel = [t for t in m if t["category"] == args[1]]
else: sel = [t for t in m if t["name"] in args]
for t in sel:
    print("|".join([t["name"], t["kind"], t.get("id", "-"), t["url"], t.get("note", "-").replace("|", "/")]))
EOF
  if [ "$name" = "LIST" ]; then printf '%-14s %-28s %-7s %s\n' "$kind" "$id" "$url" "$note"; continue; fi
  echo "==> $name [$kind]"
  if [ "$note" != "-" ]; then echo "    $note"; fi
  case "$kind" in
    git)
      dest="$DL/$name"
      if [ -d "$dest/.git" ]; then git -C "$dest" pull --ff-only
      elif [ -d "$dest" ]; then echo "    $dest exists (not a clone) - skipped"
      else git clone --depth 1 "$url" "$dest"; fi
      echo "    -> $dest (read its README for setup / model weights)";;
    pip)    "$PY" -m pip install -U "$id";;
    winget) echo "    Windows package ($id). On Linux/macOS use your package manager: $url";;
    npx)    echo "    Nothing to install: runs with 'npx $id' (needs node)";;
    manual) echo "    Download manually: $url";;
  esac
done
