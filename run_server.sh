#!/usr/bin/env bash

set -euo pipefail

export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export PATH="/opt/homebrew/opt/ruby@3.3/bin:/opt/homebrew/bin:/usr/bin:/bin:${PATH}"

bundle exec jekyll serve --livereload --livereload-port 35730 --config _config.yml,_config_dev.yml "$@"
