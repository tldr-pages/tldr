# zmx

> Persist terminal sessions across client connections.
> See also: `abduco`, `shpool`, `tmux`.
> More information: <https://zmx.sh>.

- Create a named session or attach to an existing one:

`zmx {{[a|attach]}} {{session_name}}`

- List active sessions:

`zmx {{[l|list]}}`

- Detach the current client (inside a zmx session):

`<Ctrl \>`

- Run a non-interactive command in a session without attaching:

`zmx {{[r|run]}} {{session_name}} {{command arguments...}}`

- Run a command in a session and [d]etach from the calling terminal:

`zmx {{[r|run]}} {{session_name}} -d {{command arguments...}}`

- Wait for tasks in one or more sessions to finish:

`zmx {{[w|wait]}} {{session_name1 session_name2 ...}}`

- Kill a named session:

`zmx {{[k|kill]}} {{session_name}}`

- Display the last 100 lines of a session's scrollback:

`zmx {{[hi|history]}} {{session_name}} | tail -100`
