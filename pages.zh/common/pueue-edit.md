# pueue 编辑

> 编辑已存储或排队任务的命令或路径。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 编辑任务，查看 `pueue status` 获取任务 ID：

`pueue edit {{task_id}}`

- 编辑任务执行的路径：

`pueue edit {{task_id}} --path`

- 使用指定的编辑器编辑命令：

`EDITOR={{nano}} pueue edit {{task_id}}`