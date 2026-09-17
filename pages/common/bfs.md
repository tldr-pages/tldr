# bfs

> Breadth-first search for your files.
> More information: <https://manned.org/bfs>.

- Find files by extension:

`bfs {{path/to/directory}} -name '{{*.ext}}'`

- Find files matching multiple path/name patterns:

`bfs {{path/to/directory}} -path '{{**/path/**/*.ext}}' -or -name '{{*pattern*}}'`

- Find directories matching a given name, in case-insensitive mode:

`bfs {{path/to/directory}} -type d -iname '{{*lib*}}'`

- Find files matching a given pattern, excluding specific paths:

`bfs {{path/to/directory}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Find files matching a given size range, limiting the recursive depth to "1":

`bfs {{path/to/directory}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Run a command for each file (use `{}` within the command to access the filename):

`bfs {{path/to/directory}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Find all files modified today and pass the results to a single command as arguments:

`bfs {{path/to/directory}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- Find empty files (0 byte) or directories and delete them verbosely:

`bfs {{path/to/directory}} -type {{f|d}} -empty -delete -print`
