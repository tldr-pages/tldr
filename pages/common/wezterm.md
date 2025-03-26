# wezterm

> Wez's Terminal Emulator - a powerful cross-platform terminal emulator and multiplexer.
> More information: <https://wezterm.org/cli/general>.

- Start a new Wezterm process and create a window:

`wezterm`

- Establish an `ssh` session:

`wezterm ssh {{user}}@{{host}}:{{port}}`

- Connect to the multiplexer (`wezterm-mux-server`):

`wezterm connect {{domain_name}}`

- Output an image to the terminal:

`wezterm imgcat {{path/to/image}}`

- Record a terminal session as an asciicat (by default recordings are found in `/tmp`):

`wezterm record`

- Replay an asciicat terminal session:

`wezterm replay {{path/to/cast_file}}`

- Specify the configuration file to use (overrides the normal configuration file resolution):

`wezterm --config-file {{path/to/config_file}}`

- Display help:

`wezterm help`
