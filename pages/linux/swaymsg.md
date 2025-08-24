# swaymsg

> Communicates with running instance of Sway, a tiling window manager.
> More information: <https://manned.org/man/swaymsg>.

- List current inputs identifiers (keyboard, mouse, …) (see <https://github.com/swaywm/sway/wiki#input-configuration>):

`swaymsg --pretty --type get_inputs | grep --after-context=2 'Input device'`

- List current outputs identifiers (connected displays, …) (see <https://github.com/swaywm/sway/wiki#display-configuration>, <https://gitlab.freedesktop.org/emersion/kanshi>):

`swaymsg --pretty --type get_outputs | grep --after-context=1 '^Output'`

- List Sway's workspaces and their status:

`swaymsg --type get_workspaces`

- List all open windows, containers, outputs, workspaces, … Helpful to identity `assign` commands' criterias (see <https://manned.org/man/sway.5>):

`swaymsg --type get_tree`

- Print Sway's current configuration. Doesn't expand includes:

`swaymsg --type get_config`

- Get a JSON-encoded configuration for swaybar (see <https://manned.org/man/sway-bar>):

`swaymsg --type get_bar_config`
