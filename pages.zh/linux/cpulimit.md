# cpulimit

> 一个用于限制其他进程 CPU 使用率的工具。
> 更多信息：<https://cpulimit.sourceforge.net/>。

- 限制 PID 为 1234 的现有进程，使其 CPU 使用率不超过 25%：

`cpulimit --pid {{1234}} --limit {{25%}}`

- 通过可执行文件名限制现有程序的 CPU 使用率：

`cpulimit --exe {{program}} --limit {{25}}`

- 启动给定的程序并限制其 CPU 使用率不超过 50%：

`cpulimit --limit {{50}} -- {{program argument1 argument2 ...}}`

- 启动程序，限制其 CPU 使用率为 50%，并使 cpulimit 在后台运行：

`cpulimit --limit {{50}} --background -- {{program}}`

- 如果程序的 CPU 使用率超过 50%，则终止该进程：

`cpulimit --limit 50 --kill -- {{program}}`

- 限制该程序及其子进程的 CPU 使用率，使其均不超过 25%：

`cpulimit --limit {{25}} --monitor-forks -- {{program}}`
