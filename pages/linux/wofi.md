# wofi

> An application launcher for wlroots-based Wayland compositors, similar to `rofi` and `dmenu`.
> More information: <https://hg.sr.ht/~scoopta/wofi>.

- Show the list of apps:

`wofi --show drun`

- Show the list of all commands:

`wofi --show run`

- Pipe a list of items to `stdin` and print the selected item to `stdout`:

`printf "{{Choice1\nChoice2\nChoice3}}" | wofi --dmenu`
