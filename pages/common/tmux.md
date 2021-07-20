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

INSIDE A TMUX SESSION:

- Detach from the current session:

`Ctrl-B d`

- Terminology (from `man tmux`):
  -   Session: collection of pseudo terminals managed by tmux
  -   Window: occupies the entire screen, can be split into panes (rectangles)
  -   Pane: one pseudo terminal

- Create a new window:

`Ctrl-B c`

- Cycle through windows:

`Ctrl-B n`

- Create a vertical pane within current window:

`Ctrl-B %`

- Cycle through panes:

`Ctrl-B o`

- Go to most recent pane: 

`Ctrl-B ;`

- Switch between sessions and windows:

`Ctrl-B w`

- Kill a session by name (outside tmux session):

`tmux kill-session -t {{name}}`
