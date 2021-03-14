# gh alias

> Manage GitHub CLI command aliases from the command line.
> More information: <https://cli.github.com/manual/gh_alias>.

- Display the subcommand help:

`gh alias`

- List all of the aliases `gh` is configured to use:

`gh alias list`

- Create a `gh` subcommand alias:

`gh alias set {{pv}} '{{pr view}}'`

- Set a shell command as a `gh` subcommand:

`gh alias set --shell {{alias_name}} {{command}}`

- Delete a command shortcut:

`gh alias delete {{alias_name}}`

- Set a shell command to search an open pull request using `fzf` and checkout it:

`gh alias set --shell {{switch}} '{{id="$(gh pr list --limit 1000 | fzf | cut -f1)"; [ -n "$id" ] && gh pr checkout "$id"}}'`
