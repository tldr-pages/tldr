# git delete-squashed-branches

> Delete branches that have been "squashed-merged" into a specified branch and checkout. If no branch is specified, default to the currently checked out branch.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-delete-squashed-branches>.

- Delete all branches that were "squash-merged" into the current checked out branch:

`git delete-squashed-branches`

- Delete all branches that were "squash-merged" into a specific branch:

`git delete-squashed-branches {{branch_name}}`
