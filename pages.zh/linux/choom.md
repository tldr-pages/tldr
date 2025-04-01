# choom

> 显示并更改进程的内存不足（OOM）杀手评分。
> 更多信息：<https://manned.org/choom>.

- 显示特定进程的 OOM-killer 评分：

`choom {{[-p|--pid]}} {{pid}}`

- 更改特定进程的 OOM-killer 评分：

`choom {{[-p|--pid]}} {{pid}} {{[-n|--adjust]}} {{-1000..+1000}}`

- 以特定的 OOM-killer 评分运行命令：

`choom {{[-n|--adjust]}} {{-1000..+1000}} {{command}} {{argument1 argument2 ...}}`
