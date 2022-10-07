# dolt merge

> Join two or more development histories together.
> More information: <https://github.com/dolthub/dolt>.

- Incorporate changes from the named commits (since the time their histories diverged from the current branch) into the current branch:

`dolt merge {{branch_name}}`

- Incorporate changes from the named commits (since the time their histories diverged from the current branch) into the current branch without updating the commit history:

`dolt merge --squash {{branch_name}}`

- Create a merge commit even when the merge resolves as a fast-forward:

`dolt merge --no-ff {{branch_name}}`

- Use the given {{message}} as the commit message:

`dolt merge --no-ff -m {{message}} {{branch_name}}`

- Abort the current conflict resolution process, and try to reconstruct the pre-merge state:

`dolt merge --abort`
