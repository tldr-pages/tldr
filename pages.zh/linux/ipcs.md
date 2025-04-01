# ipcs

> 显示关于 System V IPC 设施（共享内存段、消息队列和信号量数组）使用情况的信息。
> 参见：`lsipc`（更灵活的工具）、`ipcmk`（用于创建 IPC 设施）和 `ipcrm`（用于删除 IPC 设施）。
> 更多信息：<https://manned.org/ipcs>.

- 显示所有活动的 IPC 设施的信息：

`ipcs`

- 显示活动的共享内存段、消息队列或信号量集的信息：

`ipcs{{--shmems|--queues|--semaphores}}`

- 显示具有特定 ID 的资源的详细信息：

`ipcs{{--shmems|--queues|--semaphores}}{{[-i|--id]}}{{resource_id}}`

- 以字节或人类可读格式显示限制：

`ipcs{{[-l|--limits]}}{{--bytes|--human}}`

- 显示当前使用情况的概要：

`ipcs{{[-u|--summary]}}`

- 显示所有 IPC 设施的创建者和所有者的 UID 和 PID：

`ipcs{{[-c|--creator]}}`

- 显示所有 IPC 设施的最后操作者的 PID：

`ipcs{{[-p|--pid]}}`

- 显示所有 IPC 设施的最后访问时间：

`ipcs{{[-t|--time]}}`