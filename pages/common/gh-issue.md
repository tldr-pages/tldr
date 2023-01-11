# gh issue

> Manage GitHub issues from the command-line.
> More information: <https://cli.github.com/manual/gh_issue>.

- Display an issue with a specific number:

`gh issue view {{1..n}}`

- Display an issue with a specific number in the default web browser:

`gh issue view {{1..n}} --web`

- Create a new issue in the default web browser:

`gh issue create --web`

- List the last issues with a specific label:

`gh issue list --limit {{1..n}} --label "{{string}}"`

- List opened, closed, or all issues made by a specific user:

`gh issue list --state {{open|closed|all}} --author {{username}}`

- Display the status of issues relevant to the user, in a specific [repo]sitory:

`gh issue status --repo {{owner}}/{{repository}}`

- Reopen an issue with a specific number:

`gh issue reopen {{1..n}}`
