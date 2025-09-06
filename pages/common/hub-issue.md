# hub issue

> Manage Github issues.
> More information: <https://hub.github.com/hub-issue.1.html>.

- List the last 10 issues with the `bug` label:

`hub issue list {{[-L|--limit]}} {{10}} {{[-l|--labels]}} "{{bug}}"`

- Display a specific issue:

`hub issue show {{issue_number}}`

- List 10 closed issues assigneed to a specific user:

`hub issue {{[-s|--state]}} {{closed}} {{[-a|--assignee]}} {{username}} --limit {{10}}`
