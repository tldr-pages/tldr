# setsid

> 如果调用进程不是进程组的领导者，则在新会话中运行程序。创建的会话默认不受当前终端控制。更多信息：<https://manned.org/setsid>。

- 在新会话中运行程序：

`setsid {{program}}`

- 在新会话中运行程序，丢弃结果输出和错误：

`setsid {{program}} > /dev/null 2>&1`

- 在新会话中运行程序并创建一个新进程：

`setsid --fork {{program}}`

- 当程序退出时，将程序的退出代码作为setsid的退出代码返回：

`setsid --wait {{program}}`

- 在新会话中运行程序，将当前终端设置为控制终端：

`setsid --ctty {{program}}`