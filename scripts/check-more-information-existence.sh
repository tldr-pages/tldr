#!/usr/bin/env bash

# Script to list pages without "More information" links.

check_directory() {
    directory="$1"
    mapfile files < <(sed -nsE 'n; n; :x /^>/ { h; n; bx; }; x; /^> More information/! F; :y { n; by; }' "$directory"/*.md)
    echo "${files[@]}"
    if (( ${#files[@]} > 0 )); then
        echo "There are files (${#files[@]}) without links to man pages in '$directory' directory:"
        for file in "${files[@]}"; do
            echo - $file
        done
        echo
    fi
}

for language in pages; do
    for type in general linux osx windows android; do
      [[ -d "$language/$type" ]] && check_directory "$language/$type"
    done
done
