# tmux

> 终端复用器。
> 它允许多个会话，带有窗口、窗格等。
> 另请参见：`zellij`，`screen`。
> 更多信息：<https://github.com/tmux/tmux>。

- 启动一个新会话：

`tmux`

- 启动一个新的命名会话：

`tmux new -s {{name}}`

- 列出现有会话：

`tmux ls`

- 附加到最近使用的会话：

`tmux attach`

- 从当前会话中分离（在 tmux 会话内）：

`<Ctrl>-B d`

- 创建一个新窗口（在 tmux 会话内）：

`<Ctrl>-B c`

- 在会话和窗口之间切换（在 tmux 会话内）：

`<Ctrl>-B w`

- 按名称结束会话：

`tmux kill-session -t {{name}}`