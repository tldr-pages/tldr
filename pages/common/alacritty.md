# alacritty

> Cross-platform, GPU-accelerated terminal emulator.
> More information: <https://github.com/alacritty/alacritty>.

- Open a new Alacritty window:

`alacritty`

- Run in a specific directory:

`alacritty --working-directory {{path/to/directory}}`

- [e]xecute a command in a new Alacritty window:

`alacritty -e {{command}}`

- Use an alternative configuration file (defaults to `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{path/to/config.toml}}`

- Run with live configuration reload enabled (can also be enabled by default in `alacritty.toml`):

`alacritty --live-config-reload --config-file {{path/to/config.toml}}`
