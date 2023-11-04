# git diff-tree

> Compares the content and mode of blobs found via two tree objects.
> More information: <https://git-scm.com/docs/git-diff-tree>.

- Compare two tree objects:

`git diff-tree {{tree-ish1}} {{tree-ish2}}`

- Show changes between two specific commits:

`git diff-tree -r {{commit1}} {{commit2}}`

- Display changes in patch format:

`git diff-tree -p {{tree-ish1}} {{tree-ish2}}`

- Filter changes by a specific path:

`git diff-tree {{tree-ish1}} {{tree-ish2}} -- {{path/to/file_or_directory}}`
