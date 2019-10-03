# alacritty

> Cross-platform, GPU-accelerated terminal emulator.
> More information: <https://github.com/jwilm/alacritty/>

- Open a new alacritty window:

`alacritty`

- Run in a specific directory:

`alacritty --working-directory {{path/to/directory}}`

- Run a command in a new alacritty window:

`alacritty -e {{command}}`

- Specify alternative configuration file [default: $XDG_CONFIG_HOME/alacritty/alacritty.yml]

`alacritty --config-file {{patch/to/config.yml}}`

- Run with live config reload enabled:

`alacritty --live-config-reload`
