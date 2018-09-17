# rdfind

> Finds duplicate files and gets rid of them.

- Identify all duplicates in a given directory and output summary:

`rdfind -dryrun true {{path/to/directory}}`

- Replace all duplicates with hardlinks:

`rdfind -makehardlinks true {{path/to/directory}}`

- Replace all duplicates with symlinks/soft links:

`rdfind -makesymlinks true {{path/to/directory}}`

- Delete all duplicates, do not ignore empty files:

`rdfind -deleteduplicates true -ignoreempty false {{/mnt/backup}}`
