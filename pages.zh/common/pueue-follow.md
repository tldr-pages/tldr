# pueue follow

> 跟踪正在运行的任务的输出。
> 参见：`pueue log`。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 跟踪任务的输出（`stdout` + `stderr`）：

`pueue follow {{task_id}}`

- 跟踪任务的 `stderr`：

`pueue follow --err {{task_id}}`
