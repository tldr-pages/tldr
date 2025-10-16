# gh pr merge

> Merge a GitHub pull request.
> More information: <https://cli.github.com/manual/gh_pr_merge>.

- Merge the pull request associated with the current branch interactively:

`gh pr merge`

- Merge the current branch into the specified pull request:

`gh pr merge {{pr_number}} {{[-m|--merge]}}`

- Squash and merge a pull request, then delete the branch:

`gh pr merge {{pr_number}} {{[-sd|--squash --delete-branch]}}`

- Rebase and merge:

`gh pr merge {{pr_number}} {{[-r|--rebase]}}`

- Enable auto-merge (squash):

`gh pr merge {{pr_number}} --auto {{[-s|--squash]}}`

- Merge with admin privileges (if allowed):

`gh pr merge {{pr_number}} --admin`
