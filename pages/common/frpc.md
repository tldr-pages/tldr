# frpc

> Connect to a `frps` server to start proxying connections on the current host.
> Part of `frp`.
> More information: <https://github.com/fatedier/frp>.

- Start the service, using the default config file (assumed to be `frps.ini` in the current directory):

`frpc`

- Start the service, using the newer TOML config file (`frps.toml` instead of `frps.ini`) in the current directory:

`frpc -c ./frps.toml`

- Start the service, using a specified [c]onfig file:

`frpc -c {{path/to/file}}`

- Verify that the configuration file is valid:

`frpc verify -c {{path/to/file}}`

- Generate `frpc` command autocompletion setup script for Bash, Fish, PowerShell, or Zsh (printed to `stdout`):

`frpc completion {{bash|fish|powershell|zsh}}`
