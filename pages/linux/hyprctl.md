# hyprctl

> Control parts of the Hyprland Wayland compositor.
> More information: <https://wiki.hyprland.org/Configuring/Using-hyprctl>.

- Reload Hyprland configuration:

`hyprctl reload`

- Return the active window name:

`hyprctl activewindow`

- List all connected input devices:

`hyprctl devices`

- List all outputs with respective properties:

`hyprctl workspaces`

- Call a dispatcher:

`hyprctl dispatch {{dispatcher}}`

- Set a configuration keyword dynamically:

`hyprctl keyword {{keyword}} {{value}}`

- Display version:

`hyprctl version`
