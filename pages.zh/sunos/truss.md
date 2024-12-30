# truss

> 用于追踪系统调用的故障排除工具。
> SunOS 中与 strace 等效的工具。
> 更多信息：<https://www.unix.com/man-page/linux/1/truss>。

- 通过执行程序开始追踪，并跟踪所有子进程：

`truss -f {{program}}`

- 通过进程 PID 开始追踪特定进程：

`truss -p {{pid}}`

- 通过执行程序开始追踪，显示参数和环境变量：

`truss -a -e {{program}}`

- 计算每个系统调用的时间、调用次数和错误，并在程序退出时报告总结：

`truss -c -p {{pid}}`

- 追踪一个进程，按系统调用过滤输出：

`truss -p {{pid}} -t {{system_call_name}}`