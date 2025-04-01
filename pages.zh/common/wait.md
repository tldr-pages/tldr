# wait

> 等待进程完成后再继续执行。
> 更多信息：<https://manned.org/wait>.

- 等待给定进程 ID (PID) 的进程完成并返回其退出状态：

`wait {{pid}}`

- 等待调用 shell 知道的所有进程完成：

`wait`

- 等待作业完成：

`wait %{{job_number}}`

- 显示帮助：

`wait --help`