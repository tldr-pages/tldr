# wezterm cli

> Interact with a running Wezterm GUI or multiplexer.
> More information: <https://wezterm.org/cli/cli/index.html>.

- List windows, tabs, and panes:

`wezterm cli list`

- Split the current pane and print the new pane's ID to `stdout`:

`wezterm cli split-pane --{{left|right|top|bottom}} --{{cells|percent}} {{n}}`

- Activate (focus) a pane:

`wezterm cli activate-pane --pane-id {{id}}`

- Kill a pane:

`wezterm cli kill-pane --pane-id {{id}}`
