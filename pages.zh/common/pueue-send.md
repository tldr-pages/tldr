# pueue send

> 向任务发送输入。
> 更多信息：<https://github.com/Nukesor/pueue>.

- 向正在运行的命令发送输入：

`pueue send {{task_id}} "{{input}}"`

- 向需要 y/N 确认的任务发送确认（例如 APT、cp）：

`pueue send {{task_id}} {{y}}`
