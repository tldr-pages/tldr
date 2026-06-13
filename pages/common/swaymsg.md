# swaymsg

> Send messages to a running instance of Sway using IPC.
> See <https://github.com/swaywm/sway/blob/master/sway/sway.5.scd> for available commands.
> More information: <https://github.com/swaywm/sway/blob/master/swaymsg/swaymsg.1.scd>.

- Run a Sway command:

`swaymsg {{command}}`

- Display a list of workspaces:

`swaymsg {{[-t|--type]}} get_workspaces`

- Display a list of input devices:

`swaymsg {{[-t|--type]}} get_inputs`

- Display a list of output devices:

`swaymsg {{[-t|--type]}} get_outputs`

- Display a layout tree of all open windows, containers, outputs, and workspaces:

`swaymsg {{[-t|--type]}} get_tree`
