# tmux

> Tmux is a terminal multiplexer. It allows you to have multiple sessions with windows, panes, and so much more.
> More information: <https://github.com/tmux/tmux>.

- Start a new session:

`tmux`

- Start a new named session:

`tmux new-session -s {{name}}`

- List existing sessions:

`tmux ls`

- Attach to your last used session:

`tmux attach-session`

- Attach to a named session:

`tmux attach-session -t {{name}}`

- Detach from your current session (with prefix Ctrl-B):

`Ctrl-B d`

- Kill a session by name:

`tmux kill-session -t {{name}}`

- Kill your current session (with prefix Ctrl-B):

`Ctrl-B :kill-session<Enter>`
