# pidstat

> 显示系统资源使用情况，包括 CPU、内存、IO 等。
> 更多信息：<https://manned.org/pidstat>.

- 以 2 秒的间隔显示 CPU 统计信息，共显示 10 次：

`pidstat {{2}} {{10}}`

- 显示页面错误和内存使用情况：

`pidstat -r`

- 显示每个进程 ID 的输入/输出使用情况：

`pidstat -d`

- 显示特定 PID 的信息：

`pidstat -p {{PID}}`

- 显示命令名为 "fox" 或 "bird" 的所有进程的内存统计信息：

`pidstat -C "{{fox|bird}}" -r -p ALL`