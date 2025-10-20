# git merge-one-file

> Resolve a single file merge after a trivial merge.
> More information: <https://git-scm.com/docs/git-merge-one-file>.

- Resolve a simple merge conflict for a file:

`git merge-one-file {{path/to/file}}`

- Use as a helper in merge-index for a file:

`git merge-index git-merge-one-file {{path/to/file}}`

- Handle a binary file merge:

`git merge-one-file -p {{path/to/file}}`

- Apply after read-tree in a scripted merge:

`git read-tree -m {{branch1}} {{branch2}} && git merge-index git-merge-one-file {{path/to/file}}`
