# systemd-run

> 在瞬态范围单元、服务单元或路径、套接字或定时器触发的服务单元中运行程序。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-run.html>。

- 启动一个瞬态服务：

`sudo systemd-run {{command}} {{argument1 argument2 ...}}`

- 在当前用户的服务管理器下启动一个瞬态服务（无权限）：

`systemd-run --user {{command}} {{argument1 argument2 ...}}`

- 启动一个具有自定义单元名称和描述的瞬态服务：

`sudo systemd-run --unit={{name}} --description={{string}} {{command}} {{argument1 argument2 ...}}`

- 启动一个在终止后不会被清理的瞬态服务，并设置自定义环境变量：

`sudo systemd-run --remain-after-exit --set-env={{name}}={{value}} {{command}} {{argument1 argument2 ...}}`

- 启动一个定期运行其瞬态服务的瞬态定时器（请参见 `man systemd.time` 以获取日历事件格式）：

`sudo systemd-run --on-calendar={{calendar_event}} {{command}} {{argument1 argument2 ...}}`

- 与程序共享终端（允许交互式输入/输出）并确保程序退出后执行细节保持：

`systemd-run --remain-after-exit --pty {{command}}`

- 设置进程的属性（例如 CPUQuota、MemoryMax）并等待其退出：

`systemd-run --property MemoryMax={{memory_in_bytes}} --property CPUQuota={{percentage_of_CPU_time}}% --wait {{command}}`

- 在 shell 管道中使用程序：

`{{command1}} | systemd-run --pipe {{command2}} | {{command3}}`