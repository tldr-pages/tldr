# pueue enqueue

> 将暂存的任务加入队列。
> 参见：`pueue stash`。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 一次将多个暂存的任务加入队列：

`pueue enqueue {{task_id}} {{task_id}}`

- 60秒后将暂存的任务加入队列：

`pueue enqueue --delay {{60}} {{task_id}}`

- 下周三将暂存的任务加入队列：

`pueue enqueue --delay {{wednesday}} {{task_id}}`

- 四个月后将暂存的任务加入队列：

`pueue enqueue --delay "4 months" {{task_id}}`

- 2021年2月19日将暂存的任务加入队列：

`pueue enqueue --delay {{2021-02-19}} {{task_id}}`

- 查看所有可用的日期/时间格式：

`pueue enqueue --help`
