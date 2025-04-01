# strace

> 用于跟踪系统调用的故障排除工具。
> 更多信息：<https://manned.org/strace>.

- 通过 PID 开始跟踪特定进程：

`strace {{[-p|--attach]}} {{pid}}`

- 跟踪进程并按系统调用 [e]xpression 过滤输出：

`strace {{[-p|--attach]}} {{pid}} -e {{system_call,system_call2,...}}`

- 为每个系统调用计数时间、调用次数和错误，并在程序退出时报告总结：

`strace {{[-p|--attach]}} {{pid}} {{[-c|--summary-only]}}`

- 显示每个系统调用所花费的时间，并指定打印的最大字符串大小：

`strace {{[-p|--attach]}} {{pid}} {{[-T|--syscall-times]}} {{[-s|--string-limit]}} {{32}}`

- 通过执行程序开始跟踪：

`strace {{program}}`

- 跟踪程序的文件操作：

`strace -e trace=file {{program}}`

- 跟踪程序及其派生的所有子进程的网络操作，并将输出保存到文件中：

`strace {{[-f|--follow-forks]}} -e trace=network {{[-o|--output]}} {{trace.txt}} {{program}}`
