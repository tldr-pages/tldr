# git diff-tree

> Compares the content and mode of blobs found via two tree objects.
> More information: <https://git-scm.com/docs/git-diff-tree>.

- Compare two tree objects:

`git diff-tree <tree-ish> <tree-ish>`

- Show changes between two specific commits:

`git diff-tree -r <commit> <commit>`

- Display changes in patch format:

`git diff-tree -p <tree-ish> <tree-ish>`

- Filter changes by a specific path:

`git diff-tree <tree-ish> <tree-ish> -- <path/to/file-or-directory>`
