# gh issue

> Manage GitHub issues.
> More information: <https://cli.github.com/manual/gh_issue>.

- Display a specific issue:

`gh issue view {{issue_number}}`

- Display a specific issue in the default web browser:

`gh issue view {{issue_number}} {{[-w|--web]}}`

- Create a new issue in the default web browser:

`gh issue {{[new|create]}} {{[-w|--web]}}`

- List the last 10 issues with the `bug` label:

`gh issue {{[ls|list]}} {{[-L|--limit]}} 10 {{[-l|--label]}} "bug"`

- List closed issues made by a specific user:

`gh issue {{[ls|list]}} {{[-s|--state]}} closed {{[-A|--author]}} {{username}}`

- Display the status of issues relevant to the user, in a specific repository:

`gh issue status {{[-R|--repo]}} {{owner}}/{{repository}}`

- Reopen a specific issue:

`gh issue reopen {{issue_number}}`
