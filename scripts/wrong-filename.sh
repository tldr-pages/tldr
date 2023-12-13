#!/bin/sh

set -e

for path in $(find pages -type f); do
  COMMAND_NAME_FILE=$(basename "$path" | head -c-4 | tr '-' ' ' | tr '[:upper:]' '[:lower:]')
  COMMAND_NAME_PAGE=$(head -n1 "$path" | tail -c+3 | tr '-' ' ' | tr '[:upper:]' '[:lower:]')
  if [ "$COMMAND_NAME_FILE" != "$COMMAND_NAME_PAGE" ]; then
    echo "$COMMAND_NAME_FILE"
    echo "$COMMAND_NAME_PAGE"
  fi
done
