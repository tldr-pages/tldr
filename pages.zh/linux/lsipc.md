# lsipc

> 显示当前系统中使用的 System V IPC 设施的信息。
> 另见：`ipcs`（旧工具）。
> 更多信息：<https://manned.org/lsipc>。

- 显示所有活动的 IPC 设施的信息：

`lsipc`

- 显示活动的共享[m]内存段、消息[q]队列或[s]信号量集的信息：

`lsipc {{--shmems|--queues|--semaphores}}`

- 显示特定 ID 资源的完整详细信息：

`lsipc {{--shmems|--queues|--semaphores}} {{[-i|--id]}} {{resource_id}}`

- 打印给定的输出列（使用 `--help` 查看所有支持的列）：

`lsipc {{[-o|--output]}} {{KEY,ID,PERMS,SEND,STATUS,NSEMS,RESOURCE,...}}`

- 使用[r]aw、[J]SON、[l]ist 或[e]xport（key="value"）格式：

`lsipc {{--raw|--json|--list|--export}}`

- 不截断输出：

`lsipc --notruncate`
