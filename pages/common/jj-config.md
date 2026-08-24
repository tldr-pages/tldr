# jj config

> Manage config options.
> Some subcommands such as `edit`, `get`, `list`, `path`, `set`, `unset` have their own usage documentation.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config>.

- Start an editor on the user-level config file:

`jj config {{[e|edit]}} --user`

- Get the value of a config option:

`jj config {{[g|get]}} {{name}}`

- List all config variables and their values:

`jj config {{[l|list]}}`

- Print the path to the user-level config file:

`jj config {{[p|path]}} --user`

- Set a config option in the user-level config:

`jj config {{[s|set]}} --user {{name}} {{value}}`

- Unset a config option in the user-level config:

`jj config {{[u|unset]}} --user {{name}}`
