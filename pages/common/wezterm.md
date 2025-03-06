# wezterm

> Wez's Terminal Emulator, a powerful cross-platform terminal emulator and multiplexer written in Rust.
> Usage: wezterm [OPTIONS] [COMMAND].
> More information: <https://wezterm.org>.

- Start a new Wezterm process and create a window:

`wezterm`

- Establish an ssh session:

`wezterm ssh <user@host:port>`

- Connect to wezterm multiplexer:

`wezterm connect <domain_name>`

- Output an image to the terminal:

`wezterm imgcat <img>`

- Record a terminal session as an asciicat (by default recordings are found in /tmp):

`wezterm record`

- Replay an asciicat terminal session:

`wezterm replay <cast_file>`

- Specify the configuration file to use, overrides the normal configuration file resolution:

`wezterm --config-file <config_file>`

- Print help message:

`wezterm help`
