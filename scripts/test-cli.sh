#!/bin/env bash

set -euo pipefail

assert() {
  if [[ "${1}" == "${2}" ]]; then
    return
  fi

  echo "Expected \"${2}\" but got \"${1}\" 🔥"
  exit 1
}

assert "$(edition --version || true)" "${CIRCLE_TAG:-"-1.-1.-1"}"

edition docs/source.md docs/test.html --press html
cmp --silent docs/index.html docs/test.html

edition docs/source.md test.md --press markdown
cmp --silent README.md test.md
