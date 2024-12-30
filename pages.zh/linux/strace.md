# strace

> 用于跟踪系统调用的故障排除工具。
> 更多信息：<https://manned.org/strace>。

- 通过进程ID（PID）开始跟踪特定的[p]rocess：

`strace -p {{pid}}`

- 跟踪一个[p]rocess，并通过系统调用过滤输出：

`strace -p {{pid}} -e {{system_call,system_call2,...}}`

- 计算每个系统调用的时间、调用次数和错误，并在程序退出时报告摘要：

`strace -p {{pid}} -c`

- 显示每个系统调用所花费的[T]ime，并指定要打印的最大字符串[s]ize：

`strace -p {{pid}} -T -s {{32}}`

- 通过执行程序开始跟踪：

`strace {{program}}`

- 开始跟踪程序的文件操作：

`strace -e trace=file {{program}}`

- 开始跟踪程序的网络操作以及所有其[f]orked和子进程，将[o]utput保存到文件中：

`strace -f -e trace=network -o {{trace.txt}} {{program}}`