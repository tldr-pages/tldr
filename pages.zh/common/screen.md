# screen

> 在远程服务器上保持会话打开。通过单个 SSH 连接管理多个窗口。
> 类似工具请参阅 `tmux` 和 `zellij`。
> 更多信息：<https://manned.org/screen>.

- 启动一个新的 screen 会话：

`screen`

- 启动一个指定名称的新 screen 会话：

`screen -S {{会话名称}}`

- 启动一个后台会话，指定会话名称并执行指定命令并将日志输出到 screenlog.x：

`screen -dmLS {{会话名称}} {{命令}}`

- 显示所有打开的 screen 会话：

`screen -ls`

- 重新连接到一个打开的 screen 会话：

`screen -r {{会话名称}}`

- 从当前 screen 会话中分离（先按 `Ctrl + A` 然后按 `D` 分离会话）：

`<Ctrl a><d>`

- 关闭当前 screen 会话：

`<Ctrl a><k>`

- 关闭一个已经分离的 screen 会话：

`screen -X -S {{会话名称}} quit`
