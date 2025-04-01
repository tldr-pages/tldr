# truss

> 用于跟踪系统调用的故障排除工具。
> 与 SunOS 的 strace 等效。
> 更多信息：<https://www.unix.com/man-page/linux/1/truss>.

- 通过执行程序并跟踪所有子进程来开始跟踪：

`truss -f {{program}}`

- 通过 PID 跟踪特定进程：

`truss -p {{pid}}`

- 通过执行程序并显示参数和环境变量来开始跟踪：

`truss -a -e {{program}}`

- 在程序退出时，统计每个系统调用的时间、调用次数和错误，并报告摘要：

`truss -c -p {{pid}}`

- 跟踪进程并按系统调用过滤输出：

`truss -p {{pid}} -t {{system_call_name}}`