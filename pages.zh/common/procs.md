# procs

> 显示活动进程的信息。
> 更多信息：<https://github.com/dalance/procs>.

- 列出所有进程，显示 PID、用户、CPU 使用率、内存使用率和启动进程的命令：

`procs`

- 以树形结构列出所有进程：

`procs --tree`

- 如果启动进程的命令包含 Zsh，则列出这些进程的信息：

`procs {{zsh}}`

- 按 CPU 时间升序或降序排列列出所有进程的信息：

`procs {{--sorta|--sortd}} cpu`

- 列出 PID、命令或用户包含 `41` 或 `firefox` 的进程信息：

`procs --or {{PID|command|user}} {{41}} {{firefox}}`

- 列出 PID 为 `41` 且命令或用户包含 `zsh` 的进程信息：

`procs --and {{41}} {{zsh}}`
