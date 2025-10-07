# gh pr checks

> View CI checks for a GitHub pull request.
> More information: <https://cli.github.com/manual/gh_pr_checks>.

- Show checks for the pull request of the current branch:

`gh pr checks`

- Show checks for a specific pull request:

`gh pr checks {{123}}`

- Watch checks and update in real time until completion:

`gh pr checks {{123}} --watch`

- Show only required checks:

`gh pr checks {{123}} --required`
