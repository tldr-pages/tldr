# wmctrl

> CLI for X Window Manager.
> More information: <https://manned.org/wmctrl>.

- List all windows, managed by the window manager:

`wmctrl -l`

- Switch to the first window whose (partial) title matches:

`wmctrl -a {{window_title}}`

- Move a window to the current workspace, raise it and give it focus:

`wmctrl -R {{window_title}}`

- Switch to a workspace:

`wmctrl -s {{workspace_number}}`

- Select a window and toggle fullscreen:

`wmctrl -r {{window_title}} -b toggle,fullscreen`

- Select a window a move it to a workspace:

`wmctrl -r {{window_title}} -t {{workspace_number}}`
