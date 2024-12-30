# pueue 并行

> 设置允许的并行任务数量。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 设置默认组中允许并行运行的最大任务数量：

`pueue parallel {{最大并行任务数量}}`

- 设置特定组中允许并行运行的最大任务数量：

`pueue parallel --group {{组名}} {{最大并行任务数量}}`