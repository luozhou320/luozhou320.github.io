#!/bin/bash
# Local preview server for this site.
#
# Two things to know:
#  1. We pin the Homebrew Ruby's bundler explicitly. With a conda env
#     activated, `bundle` resolves to conda's Ruby, which does not have
#     this project's gems installed ("Could not find base64-0.3.0 ...").
#  2. `jekyll serve`/`liveserve` is broken with Jekyll 3.10 + WEBrick >= 1.8
#     (HTTP 500 "undefined method `key?' for nil" on every page), so we
#     build with Jekyll and serve _site with Python's static server instead.

cd "$(dirname "$0")"

BUNDLE=/opt/homebrew/bin/bundle
if [ ! -x "$BUNDLE" ]; then
  BUNDLE=$(command -v bundle)
fi

"$BUNDLE" exec jekyll build --watch &
WATCH_PID=$!
trap 'kill $WATCH_PID 2>/dev/null' EXIT

sleep 4
echo ""
echo "  Preview: http://127.0.0.1:4000/"
echo "  (files rebuild automatically; refresh the browser to see changes)"
echo ""
python3 -m http.server 4000 --bind 127.0.0.1 --directory _site
