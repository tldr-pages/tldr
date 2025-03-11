# frps

> Quickly set up a reverse proxy service.
> Part of `frp`.
> More information: <https://github.com/fatedier/frp>.

- Start the service, using the default configuration file (assumed to be `frps.ini` in the current directory):

`frps`

- Start the service, using the newer TOML configuration file (`frps.toml` instead of `frps.ini`) in the current directory:

`frps {{[-c|--config]}} ./frps.toml`

- Start the service, using a specified config file:

`frps {{[-c|--config]}} {{path/to/file}}`

- Check if the configuration file is valid:

`frps verify {{[-c|--config]}} {{path/to/file}}`

- Print autocompletion setup script for Bash, fish, PowerShell, or Zsh:

`frps completion {{bash|fish|powershell|zsh}}`

- Display version:

`frps {{[-v|--version]}}`
