# ipcs

> 显示关于 XSI IPC 设施使用情况的信息：共享内存段、消息队列和信号量数组。
> 更多信息：<https://manned.org/ipcs.1p>。

- 显示所有 IPC 的信息：

`ipcs -a`

- 显示活动共享 [m]emory 段、消息 [q]ueues 或 [s]emaphore 集的信息：

`ipcs {{-m|-q|-s}}`

- 显示最大允许大小（以 [b]ytes 为单位）：

`ipcs -b`

- 显示所有 IPC 设施的 [c]reator 用户名和组名：

`ipcs -c`

- 显示所有 IPC 设施的最后操作员的 [p]ID：

`ipcs -p`

- 显示所有 IPC 设施的访问 [t]imes：

`ipcs -t`

- 显示活动消息队列和共享内存段的 [o]utstanding 使用情况：

`ipcs -o`