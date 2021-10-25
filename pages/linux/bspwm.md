# bspwm

> A tiling window manager based on binary space partitioning.
> More information: <https://github.com/baskerville/bspwm>.

- Start `bspwm` (note that a pre-existing window manager must not be open when this command is run):

`bspwm -c {{path/to/config}}`

- Define two virtual desktop:

`bspc monitor --reset-desktops {{1}} {{2}}`

- Focus the given desktop:

`bspc desktop --focus {{number}}`

- Close the windows rooted at the selected node:

`bspc node --close`

- Send the selected node to the given desktop:

`bspc node --to-desktop {{number}}`

- Toggle full screen mode for the selected node:

`bspc node --state ~fullscreen`
