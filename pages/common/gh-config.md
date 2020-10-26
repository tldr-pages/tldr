# gh config

> Change configuration for GitHub cli.
> More information: <https://cli.github.com/manual/gh_config>.

- Display what Git protocol is being used:

`gh config get git_protocol`

- Set protocol to SSH:

`gh config set git_protocol {{ssh}}`

- Set text editor to Vim:

`gh config set editor {{vim}}`

- Reset to default text editor:

`gh config set editor {{""}}`

- Disable interactive prompts:

`gh config set prompt {{disabled}}`

- Set a specific configuration value:

`gh config set {{key}} {{value}}`
