# shutdown

> 用于关闭，重新启动或注销计算机的工具。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- 关闭当前的计算机：

`shutdown /s`

- 重启当前的计算机：

`shutdown /r`

- 休眠当前的计算机：

`shutdown /h`

- 注销当前的计算机：

`shutdown /l`

- 指定在关闭之前等待的时间（以秒为单位）：

`shutdown /s /t {{秒}}`

- 指定一个关机的理由：

`shutdown /s /c "{{理由}}"`

- 在超时之前取消关机指令：

`shutdown /a`

- 关闭远程的计算机：

`shutdown /m {{\\ 主机名}}`
