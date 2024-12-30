# renice

> 修改正在运行的进程的调度优先级/亲和度。
> 亲和度值的范围是 -20（对进程最有利）到 19（对进程最不利）。
> 另见：`nice`。
> 更多信息：<https://manned.org/renice>。

- 增加/降低一个正在运行的 [p]rocess 的优先级：

`renice -n {{3}} -p {{pid}}`

- 增加/降低一个 [u]ser 所有进程的优先级：

`renice -n {{-4}} -u {{uid|user}}`

- 增加/降低属于一个进程 [g]roup 的所有进程的优先级：

`renice -n {{5}} -g {{process_group}}`