# frps

> Quickly set up a reverse proxy service.
> Part of `frp`.
> More information: <https://github.com/fatedier/frp>.

- Start the service, using the default config file (assumed to be `frps.ini` in the current directory):

`frps`

- Start the service, using the newer TOML config file (`frps.toml` instead of `frps.ini`) in the current directory:

`frps --config ./frps.toml`

- Start the service, using a specified config file:

`frps --config {{path/to/file}}`

- Verify that the configuration file is valid:

`frps verify --config {{path/to/file}}`

- Generate `frps` command autocompletion setup script for Bash, Fish, PowerShell, or Zsh (printed to `stdout`):

`frps completion {{bash|fish|powershell|zsh}}`

- Display version:

`frps --version`
