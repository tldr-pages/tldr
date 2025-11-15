# gh codespace

> Connect and manage your codespaces in GitHub.
> More information: <https://cli.github.com/manual/gh_codespace>.

- Create a codespace in GitHub interactively:

`gh {{[cs|codespace]}} create`

- List all available codespaces:

`gh {{[cs|codespace]}} {{[ls|list]}}`

- Connect to a codespace via SSH interactively:

`gh {{[cs|codespace]}} ssh`

- Transfer a specific file to a codespace interactively:

`gh {{[cs|codespace]}} cp {{path/to/source_file}} remote:{{path/to/remote_file}}`

- List the ports of a codespace interactively:

`gh {{[cs|codespace]}} ports`

- Display the logs from a codespace interactively:

`gh {{[cs|codespace]}} logs`

- Delete a codespace interactively:

`gh {{[cs|codespace]}} delete`

- Display help for a subcommand:

`gh {{[cs|codespace]}} {{code|cp|create|delete|edit|...}} {{[-h|--help]}}`
