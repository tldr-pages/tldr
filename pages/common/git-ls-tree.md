# git ls-tree

> List the contents of a tree object.
> More information: <https://git-scm.com/docs/git-ls-tree>.

- List the contents of the tree on a branch:

`git ls-tree {{master}}`

- List the contents of the tree on a commit, recurse into subtrees, and show only filenames:

`git ls-tree -r --name-only {{c39ab84d}}`
