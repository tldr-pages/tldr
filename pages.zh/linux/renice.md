# renice

> 调整运行中进程的调度优先级/友好度。
> 优先级值范围从 -20（对进程最有利）到 19（对进程最不利）。
> 请参见：`nice`。
> 更多信息：<https://manned.org/renice>。

- 设置运行中进程的绝对优先级：

`renice --priority {{3}} {{[-p|--pid]}} {{pid}}`

- 提高运行中进程的优先级：

`sudo renice --relative {{-4}} {{[-p|--pid]}} {{pid}}`

- 降低某个用户拥有的所有进程的优先级：

`renice --relative {{4}} {{[-u|--user]}} {{uid|user}}`

- 设置属于某个进程组的所有进程的优先级：

`sudo renice {{-5}} {{[-g|--pgrp]}} {{process_group}}`