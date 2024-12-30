# lsipc

> 显示系统中当前使用的 System V IPC 设施的信息。
> 另见：旧工具 `ipcs`。
> 更多信息：<https://manned.org/lsipc>。

- 显示所有活动 IPC 设施的信息：

`lsipc`

- 显示活动的共享 [m]emory 段、消息 [q]ueues 或 [s]emaphore 集合的信息：

`lsipc {{--shmems|--queues|--semaphores}}`

- 显示特定 [i]D 资源的详细信息：

`lsipc {{--shmems|--queues|--semaphores}} --id {{resource_id}}`

- 打印给定的 [o]utput 列（使用 `--help` 查看所有支持的列）：

`lsipc --output {{KEY,ID,PERMS,SEND,STATUS,NSEMS,RESOURCE,...}}`

- 使用 [r]aw、[J]SON、[l]ist 或 [e]xport（key="value"）格式：

`lsipc {{--raw|--json|--list|--export}}`

- 不截断输出：

`lsipc --notruncate`