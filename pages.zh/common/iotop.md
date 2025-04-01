# iotop

> 显示当前进程或线程的 I/O 使用情况表。
> 更多信息：<https://manned.org/iotop>。

- 启动类似 top 的 I/O 监控：

`sudo iotop`

- 仅显示正在进行 I/O 操作的进程或线程：

`sudo iotop {{[-o|--only]}}`

- 以非交互模式显示 I/O 使用情况：

`sudo iotop {{[-b|--batch]}}`

- 仅显示进程的 I/O 使用情况（默认显示所有线程）：

`sudo iotop {{[-P|--processes]}}`

- 显示指定 PID 的 I/O 使用情况：

`sudo iotop {{[-p|--pid]}} {{PID}}`

- 显示指定用户的 I/O 使用情况：

`sudo iotop {{[-u|--user]}} {{user}}`

- 显示累积 I/O 而不是带宽：

`sudo iotop {{[-a|--accumulated]}}`
