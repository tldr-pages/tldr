# gh pr merge

> Merge a GitHub pull request.
> More information: <https://cli.github.com/manual/gh_pr_merge>.

- Merge the pull request associated with the current branch interactively:

`gh pr merge`

- Merge the current branch into the specified pull request:

`gh pr merge {{pr_number}} {{[-m|--merge]}}`

- Squash and merge, then delete the branch:

`gh pr merge {{123}} {{[-sd|--squash --delete-branch]}}`

- Rebase and merge:

`gh pr merge {{123}} {{[-r|--rebase]}}`

- Enable auto-merge (squash):

`gh pr merge {{123}} --auto {{[-s|--squash]}}`

- Merge with admin privileges (if allowed):

`gh pr merge {{123}} --admin`
