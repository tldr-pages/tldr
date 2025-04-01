# pueue parallel

> 设置允许并行运行的任务数量。
> 更多信息：<https://github.com/Nukesor/pueue>.

- 设置默认组中允许并行运行的最大任务数：

`pueue parallel {{max_number_of_parallel_tasks}}`

- 设置特定组中允许并行运行的最大任务数：

`pueue parallel --group {{group_name}} {{maximum_number_of_parallel_tasks}}`
