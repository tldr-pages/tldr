# shutdown

> 用于关闭、重启或注销计算机的工具。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- 关闭当前计算机：

`shutdown /s`

- 强制关闭当前计算机的所有应用程序：

`shutdown /s /f`

- 立即重启当前计算机：

`shutdown /r /t 0`

- 休眠当前计算机：

`shutdown /h`

- 注销当前计算机：

`shutdown /l`

- 指定在关闭前等待的秒数：

`shutdown /s /t {{秒}}`

- 中止尚未超时的关机序列：

`shutdown /a`

- 关闭远程计算机：

`shutdown /m {{\\ 主机名}}`
