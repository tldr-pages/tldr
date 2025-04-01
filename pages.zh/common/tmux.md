# tmux

> 终端复用器。
> 它允许多个会话，窗口，窗格等。
> 参见：`zellij`，`screen`。
> 更多信息：<https://github.com/tmux/tmux>。

- 启动一个新会话：

`tmux`

- 启动一个命名会话：

`tmux new -s {{name}}`

- 列出现有会话：

`tmux ls`

- 连接到最近使用的会话：

`tmux attach`

- 从当前会话中分离（在 tmux 会话内）：

`<Ctrl b><d>`

- 创建一个新窗口（在 tmux 会话内）：

`<Ctrl b><c>`

- 在会话和窗口之间切换（在 tmux 会话内）：

`<Ctrl b><w>`

- 通过名称终止会话：

`tmux kill-session -t {{name}}`