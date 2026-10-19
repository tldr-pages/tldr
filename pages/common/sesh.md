# sesh

> Manage `tmux` sessions using `zoxide`.
> More information: <https://github.com/joshmedeski/sesh#how-to-use>.

- List sessions excluding the currently attached:

`sesh list {{[-H|--hide-attached]}}`

- List sessions with icons:

`sesh list {{[-i|--icons]}}`

- Start fuzzy picker of sessions with icons:

`sesh picker {{[-i|--icons]}}`

- Connect to a session:

`sesh connect {{session_name}}`

- Connect to the previously connected session:

`sesh last`

- Preview the active window in a session:

`sesh preview {{session_name}}`
