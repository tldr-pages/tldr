# polybar-msg

> 通过进程间通信（IPC）控制 `polybar`。
> 注意：IPC 默认是禁用的，可以在 Polybar 配置中设置 `enable-ipc = true` 来启用。
> 更多信息：<https://polybar.rtfd.io/en/stable/user/ipc.html>。

- 退出栏：

`polybar-msg cmd quit`

- 在原地重新启动栏：

`polybar-msg cmd restart`

- 隐藏栏（如果栏已隐藏则不执行任何操作）：

`polybar-msg cmd hide`

- 再次显示栏（如果栏未隐藏则不执行任何操作）：

`polybar-msg cmd show`

- 切换隐藏/显示状态：

`polybar-msg cmd toggle`

- 执行模块操作（数据字符串是可选的）：

`polybar-msg action "#{{module_name}}.{{action_name}}.{{data_string}}"`

- 仅向特定的 Polybar 实例发送消息（默认为所有实例）：

`polybar-msg -p {{pid}} {{cmd|action}} {{payload}}`
