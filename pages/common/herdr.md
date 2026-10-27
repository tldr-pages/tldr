# herdr

> Terminal workspace manager for AI coding agents.
> Note: The layout is Session > Workspace > Tab > Pane.
> See also: `tmux`, `zellij`, `screen`.
> More information: <https://herdr.dev/docs/cli-reference/>.

- Start a new session or attach to the default one:

`herdr`

- Show local client and server status:

`herdr status`

- Generate default config and print to `stdout`:

`herdr --default-config`

- Detach from the current session (inside a herdr session):

`<Ctrl b><q>`

- Show keybinds (inside a herdr session):

`<Ctrl b><?>`

- Create new workspace (inside a herdr session):

`<Ctrl b><Shift n>`

- Create new tab (inside a herdr session):

`<Ctrl b><c>`

- Split pane vertically/horizontally (inside a herdr session):

`<Ctrl b>{{<v>|<->}}`
