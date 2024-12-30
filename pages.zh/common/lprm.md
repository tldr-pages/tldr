# lprm

> 取消服务器上排队的打印作业。
> 另见：`lpq`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lprm.html>。

- 取消默认打印机上的当前作业：

`lprm`

- 取消特定服务器上的一个作业：

`lprm -h {{server[:port]}} {{job_id}}`

- 通过加密连接取消多个作业：

`lprm -E {{job_id1 job_id2 ...}}`

- 取消所有作业：

`lprm -`

- 取消特定打印机或类别的当前作业：

`lprm -P {{destination[/instance]}}`