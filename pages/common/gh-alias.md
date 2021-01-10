# gh alias

> Manage GitHub command shortcuts from the command line.
> More information: <https://cli.github.com/manual/gh_alias>.

- Display the subcommand help:

`gh alias`

- List all of the aliases gh is configured to use:

`gh alias list`

- Set a command shortcut:

`gh alias set {{pv}} '{{pr view}}`

- Set a shell command as a command shortcut:

`gh alias set --shell {{alias_name}} {{command}}`

- Delete a command shortcut:

`gh alias delete {{alias_name}}`
