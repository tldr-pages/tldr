# tmux

> 终端复用器。
> 支持包含窗口、窗格等的多个会话。
> 另请参阅：`zellij`, `screen`。
> 更多信息：<https://github.com/tmux/tmux>。

- 启动一个新会话：

`tmux`

- 启动一个指定名称的新会话（[s]ession）：

`tmux {{[new|new-session]}} -s {{name}}`

- 列出现有会话：

`tmux {{[ls|list-sessions]}}`

- 连接到最近使用的会话：

`tmux {{[a|attach]}}`

- 从当前 tmux 会话断开连接：

`<Ctrl b><d>`

- 创建一个新窗口（在 tmux 会话中）：

`<Ctrl b><c>`

- 在会话和窗口之间切换（在 tmux 会话中）：

`<Ctrl b><w>`

- 终止指定目标会话（[t]arget）：

`tmux kill-session -t {{name}}`
