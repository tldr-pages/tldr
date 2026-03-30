# shpool

> Tool for creating and attaching to persistent shell sessions.
> See also: `tmux`, `screen`.
> More information: <https://github.com/shell-pool/shpool>.

- Create a new session or attach to an existing one:

`shpool attach {{session_name}}`

- List existing sessions:

`shpool list`

- Detach from the current session:

`shpool detach`

- Detach from a session:

`shpool detach {{session_name}}`

- Kill a named session:

`shpool kill {{session_name}}`

- Start the `shpool` daemon:

`shpool daemon`
