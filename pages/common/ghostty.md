# ghostty

> A fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.
> Note: All options from the configuration file can also be used on the command-line (using `--option=argument`).
> More information: <https://ghostty.org/docs/config/reference>.

- Open a new Ghostty window (not supported on macOS):

`ghostty`

- Run a specific command in a new Ghostty window (not supported on macOS):

`ghostty -e {{command}}`

- List all default and configured keybindings:

`ghostty +list-keybinds`

- List all actions (i.e. what can be triggered via keybindings):

`ghostty +list-actions`

- Browse an interactive list of themes:

`ghostty +list-themes`

- Print the default configuration (including comments):

`ghostty +show-config --default --docs`
