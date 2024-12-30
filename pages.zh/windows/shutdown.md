# 关机

> 一个用于关机、重启或注销机器的工具。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>。

- 关机当前机器：

`shutdown /s`

- 强制关闭所有应用程序后关机当前机器：

`shutdown /s /f`

- 立即重启当前机器：

`shutdown /r /t 0`

- 休眠当前机器：

`shutdown /h`

- 注销当前机器：

`shutdown /l`

- 指定等待关机的超时时间（单位：秒）：

`shutdown /s /t {{8}}`

- 中止尚未到期的关机序列：

`shutdown /a`

- 关机远程机器：

`shutdown /m {{\\hostname}}`