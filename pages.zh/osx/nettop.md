# nettop

> 显示网络的更新信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/nettop.1.html>。

- 监控所有接口的 TCP 和 UDP 套接字：

`nettop`

- 监控回环接口的 TCP 套接字：

`nettop -m {{tcp}} -t {{loopback}}`

- 监控特定进程：

`nettop -p "{{process_id|process_name}}"`

- 显示每个进程的摘要信息：

`nettop -P`

- 打印 10 次网络信息样本：

`nettop -l {{10}}`

- 每 5 秒监控一次变化：

`nettop -d -s {{5}}`

- 在运行 nettop 时，列出交互命令：

`<h>`

- 显示帮助信息：

`nettop -h`