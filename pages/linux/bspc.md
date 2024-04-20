# bspc

> Configure and control `bspwm`, managing nodes, desktops, monitors, and more.
> See also: `bspwm`.
> More information: <https://github.com/baskerville/bspwm>.

- Define two virtual desktops:

`bspc monitor --reset-desktops {{desktop_name1}} {{desktop_name2}}`

- Focus the given desktop:

`bspc desktop --focus {{number}}`

- Close the windows rooted at the selected node:

`bspc node --close`

- Send the selected node to the given desktop:

`bspc node --to-desktop {{number}}`

- Toggle full screen mode for the selected node:

`bspc node --state ~fullscreen`

- Set the value of a specific setting:

`bspc config {{setting_name}} {{value}}`
