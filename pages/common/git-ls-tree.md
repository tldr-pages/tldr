# git ls-tree

> List the contents of a tree object.
> More information: <https://git-scm.com/docs/git-ls-tree>.

- List the contents of the tree on a branch:

`git ls-tree {{branch_name}}`

- List the contents of the tree on a commit and recurse into subtrees:

`git ls-tree -r {{commit_hash}}`

- List the contents of the tree on a commit and show only filenames:

`git ls-tree --name-only {{HEAD~3}}`
