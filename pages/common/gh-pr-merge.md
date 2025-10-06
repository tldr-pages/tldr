# gh pr merge

> Merge a GitHub pull request.
> Part of the GitHub CLI: `gh`.
> More information: <https://cli.github.com/manual/gh_pr_merge>.

- Merge with a merge commit:

`gh pr merge {{123}} --merge`

- Squash and merge, then delete the branch:

`gh pr merge {{123}} --squash --delete-branch`

- Rebase and merge:

`gh pr merge {{123}} --rebase`

- Enable auto-merge (squash):

`gh pr merge {{123}} --auto --squash`

- Merge with admin privileges (if allowed):

`gh pr merge {{123}} --admin`
