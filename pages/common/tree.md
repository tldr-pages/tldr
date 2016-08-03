# tree

> Show the contents of the current directory as a tree.

- Show files and directories with a depth of 'num' (where 1 means the current directory):

`tree -L {{num}}`

- Show directories only:

`tree -d`

- Show hidden files too:

`tree -a`

- Print the tree without indentation lines, showing the full path instead:

`tree -i -f`

- Print the size of each node next to it, in human-readable format, with folders displaying their cumulative size (as in the `du` command):

`tree -s -h --du`

- Filter the tree using a wildcard (glob) pattern, showing only the hierarchies leading to the matching entries:

`tree -P {{*.txt}} --prune`
