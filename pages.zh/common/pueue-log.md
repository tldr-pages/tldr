# pueue log

> 显示一个或多个任务的日志输出。
> 参见: `pueue status`。
> 更多信息: <https://github.com/Nukesor/pueue>。

- 显示所有任务的最后几行输出：

`pueue log`

- 显示指定任务的完整输出：

`pueue log {{task_id}}`

- 显示几个任务的最后几行输出：

`pueue log {{task_id}} {{task_id}}`

- 从输出尾部打印指定数量的行：

`pueue log --lines {{number_of_lines}} {{task_id}}`
