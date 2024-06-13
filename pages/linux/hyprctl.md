# hyprctl

> Utility for controlling parts of Hyprland from a CLI or a script
> More information: https://wiki.hyprland.org/Configuring/Using-hyprctl

- Print the current Hyprland version: 

`hyprctl version`

- Reload Hyprland config:

`hyprctl reload`

- Return the active window name:

`hyprctl activewindow`

- List all connected input devices:

`hyprctl devices`

- List all outputs with respective properties:

`hyprctl workspaces`

- Call a dispatcher with an argument:

`hyprctl dispatch exec {{app}}`

- Set a config keyword dynamically:

`hyprctl keyword {{keyword}} {{value}}`
