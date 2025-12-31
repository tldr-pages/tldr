# gh alias

> Manage GitHub CLI command aliases.
> More information: <https://cli.github.com/manual/gh_alias>.

- List all the aliases `gh` is configured to use:

`gh alias {{[ls|list]}}`

- Create a `gh` subcommand alias:

`gh alias set {{pv}} '{{pr view}}'`

- Set a shell command as a `gh` subcommand:

`gh alias set {{[-s|--shell]}} {{alias_name}} {{command}}`

- Delete a command shortcut:

`gh alias delete {{alias_name}}`

- Display the subcommand help:

`gh alias`
