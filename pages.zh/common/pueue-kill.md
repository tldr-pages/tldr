# pueue 杀死

> 杀死正在运行的任务或整个组。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 杀死默认组中的所有任务：

`pueue kill`

- 杀死特定任务：

`pueue kill {{task_id}}`

- 杀死任务并终止其所有子进程：

`pueue kill --children {{task_id}}`

- 杀死组中的所有任务并暂停该组：

`pueue kill --group {{group_name}}`

- 杀死所有组中的所有任务并暂停所有组：

`pueue kill --all`