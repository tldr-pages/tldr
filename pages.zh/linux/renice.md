# renice

> 更改正在运行的进程的调度优先级/友好度。
> 友好度值范围从 -20（对进程最有利）到 19（对进程最不利）。
> 另见：`nice`。
> 更多信息：<https://manned.org/renice>。

- 设置正在运行的 [p]rocess 的绝对优先级：

`renice {{+3}} -p {{pid}}`

- 增加/减少某个 [u]用户所有进程的优先级：

`renice --relative {{-4}} -u {{uid|user}}`

- 设置属于某个进程 [g]roup 的所有进程的优先级：

`renice --absolute {{5}} -g {{process_group}}`