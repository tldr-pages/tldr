# procs

> 显示有关活动进程的信息。
> 更多信息：<https://github.com/dalance/procs>。

- 列出所有进程，显示 PID、用户、CPU 使用率、内存使用率以及启动它们的命令：

`procs`

- 以树状结构列出所有进程：

`procs --tree`

- 列出有关进程的信息，前提是启动它们的命令包含 Zsh：

`procs {{zsh}}`

- 列出所有进程的信息，按 CPU 时间升序或降序排序：

`procs {{--sorta|--sortd}} cpu`

- 列出 PID、命令或用户包含 `41` 或 `firefox` 的进程的信息：

`procs --or {{PID|command|user}} {{41}} {{firefox}}`

- 列出同时包含 PID `41` 和命令或用户中包含 `zsh` 的进程的信息：

`procs --and {{41}} {{zsh}}`