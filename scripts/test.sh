#!/bin/env bash
set -euo pipefail

pytest -vv

if [[ "${CI:=}" == "true" ]]; then
  echo "Skipping documenation press in CI."
else
  python -m edition docs/source.md README.md       --press markdown --log-level warning
  python -m edition docs/source.md docs/index.html --press html     --log-level warning
fi
