# pueue stash

> 存储任务以防止它们自动开始。
> 另请参见 `pueue start` 和 `pueue enqueue`。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 存储一个已入队的任务：

`pueue stash {{task_id}}`

- 同时存储多个任务：

`pueue stash {{task_id}} {{task_id}}`

- 立即开始一个存储的任务：

`pueue start {{task_id}}`

- 将任务入队，以便在前面的任务完成后执行：

`pueue enqueue {{task_id}}`