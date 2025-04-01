# disown

> 允许子进程在其连接的 shell 退出后仍继续运行。
> 请参阅 `jobs` 命令。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- 释放当前作业：

`disown`

- 释放特定作业：

`disown %{{job_number}}`

- 释放所有作业：

`disown -a`

- 保留作业（不释放），但在 shell 退出时标记作业以不再接收未来的 SIGHUP 信号：

`disown -h %{{job_number}}`
