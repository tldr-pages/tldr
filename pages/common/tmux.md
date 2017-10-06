# tmux

> Multiplex several virtual consoles.

- Start a new tmux session:

`tmux`

- Start a new named tmux session:

`tmux new -s {{name}}`

- List sessions:

`tmux ls`

- Attach to a session:

`tmux a`

- Attach to a named session:

`tmux a -t {{name}}`

- Detach from session:

`Ctrl + B, D`

- Kill session:

`tmux kill-session -t {{name}}`
