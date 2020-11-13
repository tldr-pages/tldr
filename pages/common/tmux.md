# tmux

> Terminal multiplexer. It allows multiple sessions with windows, panes, and more.
> More information: <https://github.com/tmux/tmux>.

- Start a new session:

`tmux`

- Start a new named session:

`tmux new -s {{name}}`

- List existing sessions:

`tmux ls`

- Attach to the most recently used session:

`tmux attach`

- Detach from the current session (with prefix Ctrl-B):

`Ctrl-B d`

- Create a new window (with prefix Ctrl-B):

`Ctrl-B c`

- Switch between sessions and windows (with prefix Ctrl-B):

`Ctrl-B w`

- Kill a session by name:

`tmux kill-session -t {{name}}`
