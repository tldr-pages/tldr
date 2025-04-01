# setsid

> 如果调用进程不是进程组的领导者，则在一个新的会话中运行程序。
> 默认情况下，创建的会话不受当前终端的控制。
> 更多信息：<https://manned.org/setsid>.

- 在新的会话中运行程序：

`setsid {{program}}`

- 在新的会话中运行程序，并丢弃输出和错误：

`setsid {{program}} > /dev/null 2>&1`

- 在新的会话中运行程序并创建一个新进程：

`setsid {{[-f|--fork]}} {{program}}`

- 当程序退出时，返回程序的退出码作为 setsid 的退出码：

`setsid {{[-w|--wait]}} {{program}}`

- 在新的会话中运行程序，并将当前终端设置为控制终端：

`setsid {{[-c|--ctty]}} {{program}}`
