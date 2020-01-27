# tmux

> Tmux is a terminal multiplexer. It lets you switch easily between several programs in
> one terminal, detach them (they keep running in the background) and reattach them to
> a different terminal.
> More information: <https://github.com/tmux/tmux>.

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

- Kill session when attached:

`Ctrl + B, x (then hit 'y' for yes)`
