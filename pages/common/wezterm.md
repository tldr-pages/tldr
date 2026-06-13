# wezterm

> Wez's Terminal Emulator - a powerful cross-platform terminal emulator and multiplexer.
> Some subcommands such as `cli` have their own usage documentation.
> More information: <https://wezterm.org/cli/general>.

- Start a new Wezterm process and create a window:

`wezterm`

- Establish an `ssh` session in a new Wezterm window:

`wezterm ssh {{user}}@{{host}}:{{port}}`

- Connect to the multiplexer (`wezterm-mux-server`):

`wezterm connect {{domain_name}}`

- Output an image to the terminal:

`wezterm imgcat {{path/to/image}}`

- Record a terminal session as an asciicast (by default recordings are saved to `/tmp`):

`wezterm record`

- Replay an asciicast terminal session:

`wezterm replay {{path/to/cast_file}}`

- Specify the configuration file to use (overrides the normal configuration file resolution):

`wezterm --config-file {{path/to/config_file}}`

- Display help:

`wezterm help`
