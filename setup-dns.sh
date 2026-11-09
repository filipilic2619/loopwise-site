#!/usr/bin/env bash
# Adds the GitHub Pages DNS records for loopwiselabs.app via the Cloudflare API.
# The API token is read from a hidden prompt and never saved or printed.
# Token needs: Zone → DNS → Edit, for zone loopwiselabs.app ("Edit zone DNS" template).
set -uo pipefail

DOMAIN="loopwiselabs.app"
API="https://api.cloudflare.com/client/v4"

read -rsp "Cloudflare API token (hidden): " CF_TOKEN; echo
CF_TOKEN=$(printf '%s' "$CF_TOKEN" | tr -d '[:space:]')
echo "Token length: ${#CF_TOKEN} characters (API tokens are 40+)."

call() { curl -sS -H "Authorization: Bearer ${CF_TOKEN}" -H "Content-Type: application/json" "$@"; }
ok_or_errors() { python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
except Exception:
    print("ERR not a JSON response"); sys.exit()
if d.get("success"):
    print("OK")
else:
    print("ERR " + "; ".join("%s: %s" % (e.get("code"), e.get("message")) for e in d.get("errors", [])))'; }

verify=$(call "$API/user/tokens/verify" | ok_or_errors)
if [[ $verify != OK ]]; then
  echo "Token check failed → ${verify#ERR }"
  echo "Make sure you copied the token value shown once after 'Create Token' (not the Token ID)."
  exit 1
fi
echo "Token is valid."

ZONE_ID=$(call "$API/zones?name=$DOMAIN" | python3 -c 'import sys,json; r=json.load(sys.stdin).get("result") or []; print(r[0]["id"] if r else "")')
[ -n "$ZONE_ID" ] || { echo "Zone $DOMAIN is not visible to this token. Give it access to that zone."; exit 1; }
echo "Zone: $DOMAIN"

add() { # type name content
  local body res
  body=$(printf '{"type":"%s","name":"%s","content":"%s","ttl":1,"proxied":false}' "$1" "$2" "$3")
  res=$(call -X POST "$API/zones/$ZONE_ID/dns_records" --data "$body" | ok_or_errors)
  if [[ $res == OK ]]; then echo "  ✔ $1 $2 → $3"; else echo "  ✖ $1 $2 → $3 (${res#ERR })"; fi
}

for ip in 185.199.108.153 185.199.109.153 185.199.110.153 185.199.111.153; do
  add A "$DOMAIN" "$ip"
done
add CNAME "www.$DOMAIN" "filipilic2619.github.io"

unset CF_TOKEN
echo "Done. Records are DNS only (not proxied), as GitHub Pages requires."
