#!/bin/env bash
set -euo pipefail

pytest -vv

if [ "${CI:=}" == "true" ]; then
  echo "Skipping documenation press in CI."
else
  python -m edition docs/src.md --press markdown > README.md
fi
