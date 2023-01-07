# glab alias

> Manage GitLab CLI command aliases from the command-line.
> More information: <https://glab.readthedocs.io/en/latest/alias>.

- Display the subcommand help:

`glab alias`

- List all the aliases `glab` is configured to use:

`glab alias list`

- Create a `glab` subcommand alias:

`glab alias set {{mrv}} '{{mr view}}'`

- Set a shell command as a `glab` subcommand:

`glab alias set --shell {{alias_name}} {{command}}`

- Delete a command shortcut:

`glab alias delete {{alias_name}}`
