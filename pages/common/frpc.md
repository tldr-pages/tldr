# frpc

> Connect to a `frps` server to start proxying connections on the current host.
> Part of `frp`.
> More information: <https://github.com/fatedier/frp>.

- Start the service, using the default configuration file (assumed to be `frps.ini` in the current directory):

`frpc`

- Start the service, using the newer TOML configuration file (`frps.toml` instead of `frps.ini`) in the current directory:

`frpc {{[-c|--config]}} ./frps.toml`

- Start the service, using a specific configuration file:

`frpc {{[-c|--config]}} {{path/to/file}}`

- Check if the configuration file is valid:

`frpc verify {{[-c|--config]}} {{path/to/file}}`

- Print autocompletion setup script for Bash, fish, PowerShell, or Zsh:

`frpc completion {{bash|fish|powershell|zsh}}`

- Display version:

`frpc {{[-v|--version]}}`
