# glab issue

> Manage GitLab issues.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/issue/index.md>.

- Display a specific issue:

`glab issue view {{issue_number}}`

- Display a specific issue in the default web browser:

`glab issue view {{issue_number}} {{[-w|--web]}}`

- Create a new issue in the default web browser:

`glab issue create --web`

- List the last 10 issues with the `bug` label:

`glab issue list {{[-P|--per-page]}} {{10}} {{[-l|--label]}} "{{bug}}"`

- List closed issues made by a specific user:

`glab issue list {{[-c|--closed]}} --author {{username}}`

- Reopen a specific issue:

`glab issue reopen {{issue_number}}`
