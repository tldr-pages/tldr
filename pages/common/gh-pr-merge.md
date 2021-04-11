# gh pr merge

> Merge a pull request on GitHub.
> More information: <https://cli.github.com/manual/gh_pr_merge>.

- Merge the pull request associated with the current branch, using the default merge strategy:

`gh pr merge`

- Merge a specific pull request:

`gh pr merge {{pr_number}}`

- Merge the pull request, removing the branch on both the local and the remote:

`gh pr merge --delete-branch`

- Squash the commits into one commit and merge it, using the default body message:

`gh pr merge --squash`

- Squash the commits into one commit and merge it, using an empty body message:

`gh pr merge --squash --body=""`

- Rebase the commits onto the base branch:

`gh pr merge --rebase`

- Merge the pull request onto the base branch using a merge commit:

`gh pr merge --merge`
