# zellij

> 带有内置功能的终端复用器。
> 另见 `tmux` 和 `screen`。
> 更多信息：<https://zellij.dev/documentation/>。

- 启动一个新的命名会话：

`zellij --session {{name}}`

- 列出现有会话：

`zellij list-sessions`

- 附加到最近使用的会话：

`zellij attach`

- 打开一个新的面板（在 zellij 会话内）：

`<Alt> + N`

- 从当前会话中分离（在 zellij 会话内）：

`<Ctrl> + O, D`