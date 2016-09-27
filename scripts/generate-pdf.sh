#!/usr/bin/env sh

src=../pages
target=../tldr-book.pdf
template=template.tex

function getContent {

  cd $src

  pages=$(ls -d */  | # list directories
        tr -d '/' | # remove trailing slash
        tr '[:lower:]' '[:upper:]') # transform to uppercase

  for page in $pages; do

    echo "\n\n# $page" >&1 # add a new chapter

    for file in $(ls $page); do

      echo "\n\n"       | # add some line breaks for latex
      cat - $page/$file | # get the content of the tldr file
      sed 's/^#/##/g' >&1 # transform h1 (chapter) to h2 (section)

    done
  done
}

getContent | pandoc -o $target --template $template --latex-engine xelatex --listings
