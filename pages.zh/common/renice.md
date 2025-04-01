# renice

> 更改运行中进程的调度优先级/亲和度。
> 亲和度值范围从 -20（对进程最有利）到 19（对进程最不利）。
> 请参阅：`nice`。
> 更多信息：<https://manned.org/renice.1p>。

- 提高/降低运行中进程的优先级：

`renice -n {{3}} -p {{pid}}`

- 提高/降低某个用户拥有所有进程的优先级：

`renice -n {{-4}} -u {{uid|user}}`

- 提高/降低属于某个进程组的所有进程的优先级：

`renice -n {{5}} -g {{process_group}}`
