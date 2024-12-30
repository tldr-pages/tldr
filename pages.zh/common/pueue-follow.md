# pueue 跟随

> 跟随当前运行任务的输出。
> 另见: `pueue log`。
> 更多信息: <https://github.com/Nukesor/pueue>。

- 跟随一个任务的输出（`stdout` + `stderr`）:

`pueue follow {{task_id}}`

- 跟随一个任务的 `stderr`:

`pueue follow --err {{task_id}}`