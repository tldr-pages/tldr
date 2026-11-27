# sbx

> Create and manage isolated microVM sandboxes for running AI coding agents.
> More information: <https://docs.docker.com/reference/cli/sbx/>.

- Open the interactive TUI dashboard:

`sbx`

- Create and run an agent session inside a sandbox:

`sbx run {{agent}} {{path/to/directory}}`

- List all sandboxes:

`sbx ls`

- Open an interactive shell inside a running sandbox:

`sbx exec {{[-it|--interactive --tty]}} {{sandbox_name}} {{bash}}`

- Stop one or more running sandboxes:

`sbx stop {{sandbox_name1 sandbox_name2 ...}}`

- Remove one or more sandboxes:

`sbx rm {{sandbox_name1 sandbox_name2 ...}}`

- Allow network access to a specific hostname or IP address for all sandboxes:

`sbx policy allow network {{hostname|ip_address}}`

- Store a secret globally for all sandboxes:

`sbx secret set {{secret_name}}`
