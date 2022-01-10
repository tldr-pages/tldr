# glab issue

> Manage Gitlab issues from the command-line.
> More information: <https://glab.readthedocs.io/en/latest/issue/>.

- Print out the issue:

`glab issue view {{issue_number}}`

- Create a new issue in the default web browser:

`glab issue create --web`

- List the last 10 issues with the `bug` label:

`glab issue list --per-page {{10}} --label "{{bug}}"`

- List closed issues made by a specific user:

`glab issue list --closed --author {{username}}`

- Reopen an issue:

`glab issue reopen {{issue_number}}`
