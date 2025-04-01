# daemon

> 将进程作为守护进程运行。
> 更多信息：<https://manned.org/daemon>.

- 以守护进程方式运行命令：

`daemon --name="{{name}}" {{command}}`

- 以守护进程方式运行命令，如果命令崩溃则重启：

`daemon --name="{{name}}" --respawn {{command}}`

- 以守护进程方式运行命令，如果命令崩溃则重启，每 10 秒尝试 2 次：

`daemon --name="{{name}}" --respawn --attempts=2 --delay=10 {{command}}`

- 以守护进程方式运行命令，将日志写入指定文件：

`daemon --name="{{name}}" --errlog={{path/to/file.log}} {{command}}`

- 杀死守护进程 (发送 SIGTERM 信号)：

`daemon --name="{{name}}" --stop`

- 列出所有守护进程：

`daemon --list`
