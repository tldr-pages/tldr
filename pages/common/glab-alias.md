# glab alias

> Manage GitLab CLI command aliases.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/alias/index.md>.

- List all the aliases `glab` is configured to use:

`glab alias list`

- Create a `glab` subcommand alias:

`glab alias set {{mrv}} '{{mr view}}'`

- Set a shell command as a `glab` subcommand:

`glab alias set {{[-s|--shell]}} {{alias_name}} {{command}}`

- Delete a command shortcut:

`glab alias delete {{alias_name}}`

- Display the subcommand help:

`glab alias`
