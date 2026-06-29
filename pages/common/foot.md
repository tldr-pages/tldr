# foot

> A fast, lightweight, and minimalistic Wayland terminal emulator.
> More information: <https://manned.org/foot>.

- Start a terminal:

`foot`

- Start the server (use `footclient` to start terminal windows that connect to the server):

`foot {{[-s|--server]}}`

- Execute a command in a new terminal window:

`foot {{command}}`

- Start a terminal in fullscreen mode:

`foot {{[-F|--fullscreen]}}`

- Start a terminal with the specified window dimensions, in pixels:

`foot {{[-w|--window-size-pixels]}} {{width}}x{{height}}`

- Start a terminal with the specified Wayland app id (default: `foot`):

`foot {{[-a|--app-id]}} {{id}}`

- Check for errors in the configuration file:

`foot {{[-C|--check-config]}}`

- Override a configuration option:

`foot {{[-o|--override]}} {{section}}.{{key}}={{value}}`
