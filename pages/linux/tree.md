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

- Print the size of each node next to it, in human-readable format:

`tree -s -h`

- Filter the tree using a wildcard (glob) pattern:

`tree -P {{*.txt}}`

- Ignore entries that match a wildcard (glob) pattern:

`tree -I {{*.txt}}`
