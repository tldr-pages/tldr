# 守护进程

> 将进程运行为守护进程。
> 更多信息：<https://manned.org/daemon>。

- 以守护进程方式运行命令：

`daemon --name="{{name}}" {{command}}`

- 以守护进程方式运行命令，如果命令崩溃则重启：

`daemon --name="{{name}}" --respawn {{command}}`

- 以守护进程方式运行命令，如果崩溃则重启，每10秒尝试两次：

`daemon --name="{{name}}" --respawn --attempts=2 --delay=10 {{command}}`

- 以守护进程方式运行命令，将日志写入特定文件：

`daemon --name="{{name}}" --errlog={{path/to/file.log}} {{command}}`

- 杀死一个守护进程（SIGTERM）：

`daemon --name="{{name}}" --stop`

- 列出守护进程：

`daemon --list`