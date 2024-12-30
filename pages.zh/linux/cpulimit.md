# cpulimit

> 一种限制其他进程CPU使用率的工具。
> 更多信息：<https://cpulimit.sourceforge.net/>

- 将现有进程（PID为1234）限制为仅使用25%的CPU：

`cpulimit --pid {{1234}} --limit {{25%}}`

- 按可执行文件名称限制现有程序：

`cpulimit --exe {{program}} --limit {{25}}`

- 启动给定程序并限制其仅使用50%的CPU：

`cpulimit --limit {{50}} -- {{program argument1 argument2 ...}}`

- 启动一个程序，将其CPU使用率限制为50%，并在后台运行cpulimit：

`cpulimit --limit {{50}} --background -- {{program}}`

- 如果程序的CPU使用率超过50%，则杀死其进程：

`cpulimit --limit 50 --kill -- {{program}}`

- 同时限制该程序及其子进程，使其CPU使用率均不超过25%：

`cpulimit --limit {{25}} --monitor-forks -- {{program}}`