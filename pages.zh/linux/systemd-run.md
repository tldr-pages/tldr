# systemd-run

> 在临时作用域单元、服务单元或由路径、套接字或定时器触发的服务单元中运行程序。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-run.html>。

- 启动一个临时服务：

`sudo systemd-run {{command}} {{argument1 argument2 ...}}`

- 以当前用户的系统管理器（无特权）启动一个临时服务：

`systemd-run --user {{command}} {{argument1 argument2 ...}}`

- 启动一个具有自定义单元名称和描述的临时服务：

`sudo systemd-run --unit={{name}} --description={{string}} {{command}} {{argument1 argument2 ...}}`

- 启动一个在终止后不会被清理且带有自定义环境变量的临时服务：

`sudo systemd-run --remain-after-exit --set-env={{name}}={{value}} {{command}} {{argument1 argument2 ...}}`

- 启动一个定期运行其临时服务的临时定时器（有关日历事件格式，请参阅 `man systemd.time`）：

`sudo systemd-run --on-calendar={{calendar_event}} {{command}} {{argument1 argument2 ...}}`

- 与程序共享终端（允许交互式输入/输出），并确保程序退出后执行详细信息保留：

`systemd-run --remain-after-exit --pty {{command}}`

- 设置进程属性（例如 CPUQuota、MemoryMax）并等待其退出：

`systemd-run --property MemoryMax={{memory_in_bytes}} --property CPUQuota={{percentage_of_CPU_time}}% --wait {{command}}`

- 在 shell 管道中使用程序：

`{{command1}} | systemd-run --pipe {{command2}} | {{command3}}`
