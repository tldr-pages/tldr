# footclient

> Start a new terminal window handled by the `foot` server.
> Note: `foot --server` must be started before using the client.
> More information: <https://manned.org/footclient>.

- Start a new terminal window, wait until the window is closed and return its exit code:

`footclient`

- Start a new terminal window and exit immediately:

`footclient {{[-N|--no-wait]}}`

- Execute a command in a new terminal window:

`footclient {{command}}`

- Start a terminal in fullscreen mode:

`footclient {{[-F|--fullscreen]}}`

- Start a terminal with the specified window dimensions, in pixels:

`footclient {{[-w|--window-size-pixels]}} {{width}}x{{height}}`

- Start a terminal with the specified Wayland app id (default: `footclient`):

`footclient {{[-a|--app-id]}} {{id}}`

- Override a configuration option:

`footclient {{[-o|--override]}} {{section}}.{{key}}={{value}}`
