# wait

> 等待进程完成后再继续。
> 另请参阅：`ps`、`waitpid`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-wait>。

- 等待给定进程 ID（PID）的进程完成并返回其退出状态：

`wait {{pid}}`

- 等待调用 shell 已知的所有进程完成：

`wait`

- 等待作业完成（运行 `jobs` 查找作业编号）：

`wait %{{作业编号}}`

- 显示帮助信息：

`wait --help`
