# tree

> Show the contents of the current directory as a tree.

- Show files and directories up to 'num' levels of depth (where 1 means the current directory):

`tree -L {{num}}`

- Show directories only:

`tree -d`

- Show hidden files too:

`tree -a`

- Print the tree without indentation lines, showing the full path instead (use `-N` to not escape whitespace and special characters):

`tree -i -f`

- Print the size of each node next to it, in human-readable format, with directories displaying their cumulative size (as in the `du` command):

`tree -s -h --du`

- Find files within the tree hierarchy, using a wildcard (glob) pattern, and pruning out directories that don't contain matching files:

`tree -P '{{*.txt}}' --prune`

- Find directories within the tree hierarchy, pruning out directories that aren't ancestors of the wanted one:

`tree -P {{directory_name}} --matchdirs --prune`
