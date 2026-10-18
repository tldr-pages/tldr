# sesh

> Sesh is a tool for managing tmux sessions using [zoxide](https://github.com/ajeetdsouza/zoxide).
> More information: <https://github.com/joshmedeski/sesh>.

- List sessions excluding the currently attached with icons:

`sesh list --hide-attached --icons`

- List panes for the currently connected session:

`sesh list --panes`

- Start fuzzy picker of sessions with icons:

`sesh picker --icons`

- Connect to a session:

`sesh connect {{name}}`

- Connect to the previously connected session:

`sesh last`

- Preview the active window in a session:

`sesh preview {{name}}`
