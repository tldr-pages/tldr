# bspc

> A tool to control `bspwm`.
> More information: <https://github.com/baskerville/bspwm>.

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
