# ipcs

> 显示关于 System V IPC 设施的使用信息：共享内存段、消息队列和信号量数组。
> 另见：`lsipc` 作为更灵活的工具，`ipcmk` 用于创建 IPC 设施，以及 `ipcrm` 用于删除它们。
> 更多信息：<https://manned.org/ipcs>。

- 显示所有活动 IPC 设施的信息：

`ipcs`

- 显示活动的共享 [m]emory 段、消息 [q]ueues 或 [s]emaphore 集的相关信息：

`ipcs {{--shmems|--queues|--semaphores}}`

- 显示具有特定 [i]D 的资源的详细信息：

`ipcs {{--shmems|--queues|--semaphores}} --id {{resource_id}}`

- 以 [b]ytes 或人类可读格式显示 [l]imits：

`ipcs --limits {{--bytes|--human}}`

- 显示有关当前使用情况的 s[u]mmary：

`ipcs --summary`

- 显示所有 IPC 设施的创建者和拥有者的 UID 和 PID：

`ipcs --creator`

- 显示所有 IPC 设施的最后操作员的 [p]ID：

`ipcs --pid`

- 显示所有 IPC 设施的最后访问 [t]imes：

`ipcs --time`