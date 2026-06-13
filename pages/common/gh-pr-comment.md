# gh pr comment

> Add a comment to a GitHub pull request.
> More information: <https://cli.github.com/manual/gh_pr_comment>.

- Comment on the pull request of the current branch:

`gh pr comment {{[-b|--body]}} "{{LGTM}}"`

- Comment on a specific pull request:

`gh pr comment {{123}} {{[-b|--body]}} "{{Thanks!}}"`

- Comment from a file:

`gh pr comment {{123}} {{[-F|--body-file]}} {{path/to/file.txt}}`

- Open the editor to write a multi-line comment:

`gh pr comment {{123}}`
