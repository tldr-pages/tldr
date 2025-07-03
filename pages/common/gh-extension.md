# gh extension

> Manage extensions for the GitHub CLI.
> More information: <https://cli.github.com/manual/gh_extension>.

- Initialize a new GitHub CLI extension project in a directory of the same name:

`gh {{[ext|extension]}} create {{extension_name}}`

- Install an extension from a GitHub repository:

`gh {{[ext|extension]}} install {{owner}}/{{repository}}`

- List installed extensions:

`gh {{[ext|extension]}} list`

- Upgrade a specific extension:

`gh {{[ext|extension]}} upgrade {{extension_name}}`

- Upgrade all extensions:

`gh {{[ext|extension]}} upgrade --all`

- List installed extensions:

`gh {{[ext|extension]}} list`

- Remove an extension:

`gh {{[ext|extension]}} remove {{extension_name}}`

- Display help about a subcommand:

`gh {{[ext|extension]}} {{subcommand}} --help`
