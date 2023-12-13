#!/bin/sh
# SPDX-License-Identifier: MIT

set -e

for path in $(find . -name '*.md' -type f); do
  COMMAND_NAME_FILE=$(basename "$path" | head -c-4 | tr '-' ' ' | tr '[:upper:]' '[:lower:]')
  COMMAND_NAME_PAGE=$(head -n1 "$path" | tail -c+3 | tr '-' ' ' | tr '[:upper:]' '[:lower:]')
  if [ "$COMMAND_NAME_FILE" != "$COMMAND_NAME_PAGE" ]; then
    echo "$path"
    echo "$COMMAND_NAME_FILE"
    echo "$COMMAND_NAME_PAGE"
    echo "\n\n"
  fi
done
