# jj config list

> List variables set in config files, along with their values.
> See also: `jj config get`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config-list>.

- List all config variables and their values:

`jj config {{[l|list]}}`

- List a specific config option:

`jj config {{[l|list]}} {{name}}`

- List user-level config variables:

`jj config {{[l|list]}} --user`

- List repo-level config variables:

`jj config {{[l|list]}} --repo`

- List config variables including built-in default values:

`jj config {{[l|list]}} --include-defaults`

- List config variables including overridden values:

`jj config {{[l|list]}} --include-overridden`

- List config variables with a custom template:

`jj config {{[l|list]}} {{[-T|--template]}} {{template}}`
