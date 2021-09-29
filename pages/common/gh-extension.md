# gh extension

> Manage extensions for the GitHub CLI.
> More information: <https://cli.github.com/manual/gh_extension>.

- Initialize a new GitHub CLI extension project in a directory of the same name:

`gh extension create {{extension_name}}`

- Install an extension from a GitHub repository:

`gh extension install {{owner}}/{{repository}}`

- List installed extensions:

`gh extension list`

- Upgrade a specific extension:

`gh extension upgrade {{extension_name}}`

- Upgrade all extensions:

`gh extension upgrade --all`

- List installed extensions:

`gh extension list`

- Remove an extension:

`gh extension remove {{extension_name}}`

- Display help about a subcommand:

`gh extension {{subcommand}} --help`
