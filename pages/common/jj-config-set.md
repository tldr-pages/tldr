# jj config set

> Update a config file to set an option to a given value.
> The value is specified as a TOML expression.
> See also: `jj config unset`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config-set>.

- Set the user name in the user-level config:

`jj config {{[s|set]}} --user user.name "{{name}}"`

- Set the user email in the user-level config:

`jj config {{[s|set]}} --user user.email "{{email}}"`

- Set a config option in the repo-level config:

`jj config {{[s|set]}} --repo {{name}} {{value}}`

- Set a config option in the workspace-level config:

`jj config {{[s|set]}} --workspace {{name}} {{value}}`

- Set a boolean config option:

`jj config {{[s|set]}} --user {{name}} {{true|false}}`
