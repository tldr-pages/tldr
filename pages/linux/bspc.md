# bspc

> Configure and control `bspwm`, managing nodes, desktops, monitors, and more.
> See also: `bspwm`.
> More information: <https://github.com/baskerville/bspwm>.

- Define two virtual desktops:

`bspc monitor {{[-d|--reset-desktops]}} {{desktop_name1}} {{desktop_name2}}`

- Focus the given desktop:

`bspc desktop {{[-f|--focus]}} {{number}}`

- Close the windows rooted at the selected node:

`bspc node {{[-c|--close]}}`

- Send the selected node to the given desktop:

`bspc node {{[-d|--to-desktop]}} {{number}}`

- Toggle full screen mode for the selected node:

`bspc node {{[-t|--state]}} ~fullscreen`

- Set the value of a specific setting:

`bspc config {{setting_name}} {{value}}`
