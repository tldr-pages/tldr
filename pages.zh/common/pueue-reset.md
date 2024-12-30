# pueue 重置

> 杀死所有进程并重置。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 杀死所有任务并删除所有内容（日志、状态、组、任务 ID）：

`pueue reset`

- 杀死所有任务，终止其子进程，并重置所有内容：

`pueue reset --children`

- 不询问确认进行重置：

`pueue reset --force`