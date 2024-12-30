# virsh pool-info

> 列出虚拟机存储池的信息。
> 另见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 列出指定名称或 UUID 的存储池的名称、UUID、状态、持久性类型、自动启动状态、容量、已分配空间和可用空间（使用 `virsh pool-list` 确定）：

`virsh pool-info --pool {{name|uuid}}`