# tmux

> Tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.
> More information: <https://github.com/tmux/tmux>.

> By default, your tmux prefix is Ctrl-b.  In the examples below, it'll mention {{prefix}}.
> If you haven't changed your prefix, use Ctrl-b.  If you have, use your prefix.

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

- Detach from your current session:

`{{prefix}} d`

- Kill a session by name:

`tmux kill-session -t {{name}}`

- Kill your current session (when attached):

`{{prefix}} :kill-session<Enter>`
