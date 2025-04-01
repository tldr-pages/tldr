# pueue stash

> 将任务存入暂存区以防止它们自动启动。
> 参见 `pueue start` 和 `pueue enqueue`。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 将排队的任务存入暂存区：

`pueue stash {{task_id}}`

- 一次性将多个任务存入暂存区：

`pueue stash {{task_id}} {{task_id}}`

- 立即启动一个暂存区的任务：

`pueue start {{task_id}}`

- 将任务排队，以在前面的任务完成后执行：

`pueue enqueue {{task_id}}`
