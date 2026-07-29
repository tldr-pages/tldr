# renice

> 更改正在运行的进程的调度优先级/niceness。
> Niceness 值范围从 -20（最有利于进程）到 19（最不利于进程）。
> 另请参阅：`nice`。
> 更多信息：<https://manned.org/renice.1p>。

- 增加/减少正在运行的进程的优先级：

`renice -n {{3}} -p {{pid}}`

- 增加/减少用户拥有的所有进程的优先级：

`renice -n {{-4}} -u {{uid|用户}}`

- 增加/减少属于进程组的所有进程的优先级：

`renice -n {{5}} -g {{进程组}}`
