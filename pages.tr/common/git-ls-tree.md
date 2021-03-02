# git ls-tree

> List the contents of a tree object.
> More information: <https://git-scm.com/docs/git-ls-tree>.

- List the contents of the tree on a branch:

`git ls-tree {{branch_name}}`

- List the contents of the tree on a commit, recursing into subtrees:

`git ls-tree -r {{commit_hash}}`

- List only the filenames of the tree on a commit:

`git ls-tree --name-only {{commit_hash}}`
