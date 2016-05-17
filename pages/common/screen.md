# screen

> Hold a session open on a remote server. Manage multiple windows with a single SSH connection.

- Start a new screen session:

`screen`

- Start a new named screen session:

`screen -S {{session_name}}`

- Show open screen sessions:

`screen -ls`

- Reattach to an open screen:

`screen -r {{session_name}}`

- Detach from inside a screen:

`ctrl+A D`

- Kill a detached screen:

`screen -X -S {{session_name}} quit`
