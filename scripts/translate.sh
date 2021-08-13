#!/bin/bash

which aws shyaml &>/dev/null || { echo "no aws or shyaml tools, exiting"; exit 1; }

# default ro
lang=${1:-ro}
# default pages
path=${2:-pages}

echo "running $0 $lang $path"
echo "switching workdir to $path"

cd "$path"
mkdir -p ../"$path.$lang"/{common,linux}

# today/2021 they fit aws free tier
for file in {common,linux}/*.md; do
  name=$(basename "$file")
  echo -n "processing $name "
  [ -f "../$path.$lang/$file" ] && echo ok && continue

  while IFS= read -r line
  do
    # select lines to be translated
    if [[ "$line" =~ ^[-\>] ]]; then
      aws translate translate-text --source-language-code "en" --target-language-code "$lang" --text "$line" --output yaml | shyaml get-value TranslatedText >> "../$path.$lang/$file"
      echo >> "../$path.$lang/$file"
      echo -n .
    else
      # lines not meant for automated translation
      printf '%s\n' "$line" >> "../$path.$lang/$file"
    fi
  done <"$file"
  echo
done

# last minute fixes for ro
if [ "$lang" = "ro" ]; then
  sedfix=sed
  [ "$(uname -s)" = "Darwin" ] && brew install gsed && sedfix=gsed
  echo "fixing $lang translation artifacts"
  # sometimes <url> is translated before text
  $sedfix -E -i 's/(<.*>)(>.*:)$/\2\1/' ../"$path.$lang"/{common,linux}/*.md
  # if some <url> got translated into < url >
  $sedfix -E -i 's/< (.*) >/ <\1>/' ../"$path.$lang"/{common,linux}/*.md
  # strip extra spaces before <url>s
  $sedfix -E -i 's/:\s+(<http)/: \1/' ../"$path.$lang"/{common,linux}/*.md
fi

sync
echo done
