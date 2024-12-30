# screen

> 在远程服务器上保持会话打开。通过单个 SSH 连接管理多个窗口。
> 另见 `tmux` 和 `zellij`。
> 更多信息：<https://manned.org/screen>。

- 启动一个新的 screen 会话：

`screen`

- 启动一个新的命名 screen 会话：

`screen -S {{session_name}}`

- 启动一个新的守护进程并将输出记录到 `screenlog.x`：

`screen -dmLS {{session_name}} {{command}}`

- 显示打开的 screen 会话：

`screen -ls`

- 重新连接到一个打开的 screen：

`screen -r {{session_name}}`

- 从 screen 中分离：

`<Ctrl> + A, D`

- 杀死当前的 screen 会话：

`<Ctrl> + A, K`

- 杀死一个分离的 screen：

`screen -X -S {{session_name}} quit`