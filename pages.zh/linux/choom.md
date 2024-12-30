# choom

> 显示和更改调整的内存不足杀手分数。
> 更多信息：<https://manned.org/choom>。

- 显示具有特定ID的进程的OOM-killer分数：

`choom -p {{pid}}`

- 更改特定进程的调整OOM-killer分数：

`choom -p {{pid}} -n {{-1000..+1000}}`

- 以特定的调整OOM-killer分数运行命令：

`choom -n {{-1000..+1000}} {{command}} {{argument1 argument2 ...}}`