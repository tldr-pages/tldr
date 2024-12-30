# pueue 启动

> 恢复任务或任务组的操作。
> 另见：`pueue 暂停`。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 恢复默认组中的所有任务：

`pueue start`

- 恢复特定任务：

`pueue start {{task_id}}`

- 一次恢复多个任务：

`pueue start {{task_id}} {{task_id}}`

- 恢复所有任务并启动它们的子任务：

`pueue start --all --children`

- 恢复特定组中的所有任务：

`pueue start group {{group_name}}`