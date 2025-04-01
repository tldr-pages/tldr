# systemd-cat

> 将管道或程序的输出流连接到 systemd 日志。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-cat.html>.

- 将指定命令的输出写入日志（捕获所有输出流）：

`systemd-cat {{command}}`

- 将管道的输出写入日志（`stderr` 仍然连接到终端）：

`{{command}} | systemd-cat`
