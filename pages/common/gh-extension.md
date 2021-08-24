# gh extension

> Manage extensions for the GitHub CLI.
> More information: <https://cli.github.com/manual/gh_extension>.

- Initialize a new GitHub CLI extension project in a directory of the same name:

`gh extension create {{name}}`

- Install an extension from a GitHub repository:

`gh extension install {{owner}}/{{repository}}`

- List installed extensions:

`gh extension list`

- Upgrade a specific extension:

`gh extension upgrade {{name}}`

- Upgrade all extensions:

`gh extension upgrade --all`
