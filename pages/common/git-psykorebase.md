# git psykorebase

> Rebase a branch on top of another using a merge commit and only one conflict handling.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-psykorebase>.

- Rebase the current branch on top of another using a merge commit and only one conflict handling:

`git psykorebase {{upstream_branch}}`

- Continue after conflicts have been handled:

`git psykorebase --continue`

- Specify the branch to rebase:

`git psykorebase {{upstream_branch}} {{target_branch}}`
