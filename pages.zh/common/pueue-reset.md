# pueue reset

> 终止所有任务并重置。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 终止所有任务并移除所有内容（日志、状态、组、任务ID）：

`pueue reset`

- 终止所有任务，结束其子进程，并重置所有内容：

`pueue reset --children`

- 不提示确认直接重置：

`pueue reset --force`
