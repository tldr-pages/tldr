# dolt merge

> Join two or more development histories together.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-merge>.

- Incorporate changes from the named commits into the current branch:

`dolt merge {{branch_name}}`

- Incorporate changes from the named commits into the current branch without updating the commit history:

`dolt merge --squash {{branch_name}}`

- Merge a branch and create a merge commit even when the merge resolves as a fast-forward:

`dolt merge --no-ff {{branch_name}}`

- Merge a branch and create a merge commit with a specific commit message:

`dolt merge --no-ff -m "{{message}}" {{branch_name}}`

- Abort the current conflict resolution process:

`dolt merge --abort`
