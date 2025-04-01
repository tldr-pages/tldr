# pueue restart

> 重启任务。
> 更多信息：<https://github.com/Nukesor/pueue>.

- 重启特定任务：

`pueue restart {{task_id}}`

- 一次重启多个任务，并立即启动（不入队列）：

`pueue restart --start-immediately {{task_id}} {{task_id}}`

- 从不同路径重启特定任务：

`pueue restart --edit-path {{task_id}}`

- 重启前编辑命令：

`pueue restart --edit {{task_id}}`

- 就地重启任务（不作为单独任务入队）：

`pueue restart --in-place {{task_id}}`

- 重启所有失败的任务并收藏它们：

`pueue restart --all-failed --stashed`
