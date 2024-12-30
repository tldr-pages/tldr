# pueue 入队

> 入队暂存的任务。
> 参见：`pueue stash`。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 一次性入队多个暂存任务：

`pueue enqueue {{task_id}} {{task_id}}`

- 在60秒后入队一个暂存任务：

`pueue enqueue --delay {{60}} {{task_id}}`

- 在下周三入队一个暂存任务：

`pueue enqueue --delay {{wednesday}} {{task_id}}`

- 在四个月后入队一个暂存任务：

`pueue enqueue --delay "4 months" {{task_id}}`

- 在2021-02-19入队一个暂存任务：

`pueue enqueue --delay {{2021-02-19}} {{task_id}}`

- 列出所有可用的日期/时间格式：

`pueue enqueue --help`