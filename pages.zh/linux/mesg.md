# mesg

> 检查或设置终端接收来自其他用户的消息的能力，通常来自 `write` 命令。
> 另请参阅 `write`，`talk`。
> 更多信息：<https://manned.org/mesg.1>。

- 检查终端是否开放接收消息：

`mesg`

- 不允许接收来自其他用户的消息：

`mesg n`

- 允许接收来自其他用户的消息：

`mesg y`

- 启用 [v]erbose 模式，如果命令不是从终端执行，则打印警告：

`mesg --verbose`