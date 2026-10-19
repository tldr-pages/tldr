# sesh

> Manage `tmux` sessions using `zoxide`.
> More information: <https://github.com/joshmedeski/sesh#how-to-use>.

- List sessions excluding the currently attached:

`sesh list --hide-attached`

- List sessions with icons:

`sesh list --icons`

- List panes for the currently connected session:

`sesh list --panes`

- Start fuzzy picker of sessions with icons:

`sesh picker --icons`

- Connect to a session:

`sesh connect {{session_name}}`

- Connect to the previously connected session:

`sesh last`

- Preview the active window in a session:

`sesh preview {{session_name}}`
