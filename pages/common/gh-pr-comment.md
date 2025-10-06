# gh pr comment

> Add a comment to a GitHub pull request.
> Part of the GitHub CLI: `gh`.
> More information: <https://cli.github.com/manual/gh_pr_comment>.

- Comment on the pull request of the current branch:

`gh pr comment --body "{{LGTM}}"`

- Comment on a specific pull request:

`gh pr comment {{123}} --body "{{Thanks!}}"`

- Comment from a file:

`gh pr comment {{123}} --body-file "{{path/to/file.txt}}"`

- Open the editor to write a multi-line comment:

`gh pr comment {{123}}`
