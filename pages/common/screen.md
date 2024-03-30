# screen

> Hold a session open on a remote server. Manage multiple windows with a single SSH connection.
> See also `tmux` and `zellij`.
> More information: <https://manned.org/screen>.

- Start a new screen session:

`screen`

- Start a new named screen session:

`screen -S {{session_name}}`

- Start a new daemon and log the output to `screenlog.x`:

`screen -dmLS {{session_name}} {{command}}`

- Show open screen sessions:

`screen -ls`

- Reattach to an open screen:

`screen -r {{session_name}}`

- Detach from inside a screen:

`<Ctrl> + A, D`

- Kill the current screen session:

`<Ctrl> + A, K`

- Kill a detached screen:

`screen -X -S {{session_name}} quit`
