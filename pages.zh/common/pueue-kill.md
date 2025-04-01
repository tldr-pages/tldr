# pueue kill

> 终止运行中的任务或整个组。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 终止默认组中的所有任务：

`pueue kill`

- 终止特定任务：

`pueue kill {{task_id}}`

- 终止任务并终止其所有子进程：

`pueue kill --children {{task_id}}`

- 终止组中的所有任务并暂停该组：

`pueue kill --group {{group_name}}`

- 终止所有组中的所有任务并暂停所有组：

`pueue kill --all`