# gh issue

> Manage GitHub issues from the command-line.
> More information: <https://cli.github.com/manual/gh_issue>.

- Display a specific issue:

`gh issue view {{issue_number}}`

- Display a specific issue in the default web browser:

`gh issue view {{issue_number}} --web`

- Create a new issue in the default web browser:

`gh issue create --web`

- List the last 10 issues with the `bug` label:

`gh issue list --limit {{10}} --label "{{bug}}"`

- List closed issues made by a specific user:

`gh issue list --state closed --author {{username}}`

- Display the status of issues relevant to the user, in a specific repository:

`gh issue status --repo {{owner}}/{{repository}}`

- Reopen a specific issue:

`gh issue reopen {{issue_number}}`
