# lprm

> 取消服务器中的打印任务队列。
> 参见: `lpq`。
> 更多信息: <https://openprinting.github.io/cups/doc/man-lprm.html>。

- 取消默认打印机上的当前任务：

`lprm`

- 取消特定服务器上的任务：

`lprm -h {{server[:port]}} {{job_id}}`

- 通过加密连接取消服务器上的多个任务：

`lprm -E {{job_id1 job_id2 ...}}`

- 取消所有任务：

`lprm -`

- 取消特定打印机或打印组的当前任务：

`lprm -P {{destination[/instance]}}`
