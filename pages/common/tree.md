# tree

> Show the contents of the current directory as a tree.
> More information: <http://mama.indstate.edu/users/ice/tree/>.

- Print files and directories up to 'num' levels of depth (where 1 means the current directory):

`tree -L {{num}}`

- Print directories only:

`tree -d`

- Print hidden files too with colorization on:

`tree -a -C`

- Print the tree without indentation lines, showing the full path instead (use `-N` to not escape non-printable characters):

`tree -i -f`

- Print the size of each file and the cumulative size of each directory, in human-readable format:

`tree -s -h --du`

- Print files within the tree hierarchy, using a wildcard (glob) pattern, and pruning out directories that don't contain matching files:

`tree -P '{{*.txt}}' --prune`

- Print directories within the tree hierarchy, using the wildcard (glob) pattern, and pruning out directories that aren't ancestors of the wanted one:

`tree -P {{directory_name}} --matchdirs --prune`

- Print the tree ignoring the given directories:

`tree -I '{{directory_name1|directory_name2}}'`
