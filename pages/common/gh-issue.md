# gh issue

> Manage GitHub issues from the command-line.
> More information: <https://cli.github.com/manual/gh_issue>.

- Display a specific issue:

`gh issue view {{1..infinity}}`

- Display a specific issue in the default web browser:

`gh issue view {{1..infinity}} --web`

- Create a new issue in the default web browser:

`gh issue create --web`

- List the last issues with a specific label:

`gh issue list --limit {{1..infinity}} --label "{{string}}"`

- List opened, closed, or all issues made by a specific user:

`gh issue list --state {{open|closed|all}} --author {{username}}`

- Display the status of issues relevant to the user, in a specific [repo]sitory:

`gh issue status --repo {{owner}}/{{repository}}`

- Reopen a specific issue:

`gh issue reopen {{1..infinity}}`
