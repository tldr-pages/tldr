# gh-pr

> Manage GitHub issues from the command line.
> More information: <https://cli.github.com/manual/gh_issue>.

- Print out the issue:
`gh issue view {{ issue_number }}`

- Create a new issue in the web browser:

`gh issue create --web`

- List 10 issues with "bug" label:

`gh issue list -L 10 -l "bug"`

- List closed issues made by given user:

`gh issue list -s closed -A {{ github_nickname }}`

