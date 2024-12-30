# wait

> 等待一个进程完成后再继续。
> 更多信息：<https://manned.org/wait>。

- 等待给定进程 ID (PID) 的进程完成，并返回其退出状态：

`wait {{pid}}`

- 等待所有已知的与调用 shell 相关的进程完成：

`wait`

- 等待一个作业完成：

`wait %{{N}}`