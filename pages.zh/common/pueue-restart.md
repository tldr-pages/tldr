# pueue 重启

> 重启任务。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 重启特定任务：

`pueue restart {{task_id}}`

- 一次重启多个任务，并立即启动它们（不入队）：

`pueue restart --start-immediately {{task_id}} {{task_id}}`

- 从不同路径重启特定任务：

`pueue restart --edit-path {{task_id}}`

- 在重启之前编辑命令：

`pueue restart --edit {{task_id}}`

- 原地重启任务（不作为单独任务入队）：

`pueue restart --in-place {{task_id}}`

- 重启所有失败的任务并将其存储：

`pueue restart --all-failed --stashed`