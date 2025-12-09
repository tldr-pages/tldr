# wofi

> An application launcher for wlroots-based Wayland compositors, similar to `rofi` and `dmenu`.
> More information: <https://manned.org/wofi>.

- Show the list of apps:

`wofi {{[-S|--show]}} drun`

- Show the list of all commands:

`wofi {{[-S|--show]}} run`

- Pipe a list of items to `stdin` and print the selected item to `stdout`:

`printf "{{Choice1\nChoice2\nChoice3}}" | wofi {{[-d|--dmenu]}}`
