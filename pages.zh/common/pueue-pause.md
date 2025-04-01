# pueue pause

> 暂停正在运行的任务或组。
> 参见：`pueue start`。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 暂停默认组中的所有任务：

`pueue pause`

- 暂停一个正在运行的任务：

`pueue pause {{task_id}}`

- 暂停一个正在运行的任务，并停止其所有直接子任务：

`pueue pause --children {{task_id}}`

- 暂停一个组中的所有任务，并阻止该组启动新的任务：

`pueue pause --group {{group_name}}`

- 暂停所有任务，并阻止所有组启动新的任务：

`pueue pause --all`
