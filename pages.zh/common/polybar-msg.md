# polybar-msg

> 使用进程间通信 (IPC) 控制 `polybar`。
> 注意：IPC 默认是禁用的，可以通过在 Polybar 配置中设置 `enable-ipc = true` 来启用。
> 更多信息：<https://polybar.rtfd.io/en/stable/user/ipc.html>。

- 退出工具栏：

`polybar-msg cmd quit`

- 在原地重启工具栏：

`polybar-msg cmd restart`

- 隐藏工具栏（如果工具栏已经隐藏，则无效）：

`polybar-msg cmd hide`

- 再次显示工具栏（如果工具栏没有隐藏，则无效）：

`polybar-msg cmd show`

- 切换隐藏/可见状态：

`polybar-msg cmd toggle`

- 执行模块操作（数据字符串是可选的）：

`polybar-msg action "#{{module_name}}.{{action_name}}.{{data_string}}"`

- 仅向特定的 Polybar 实例发送消息（默认情况下向所有实例发送）：

`polybar-msg -p {{pid}} {{cmd|action}} {{payload}}`