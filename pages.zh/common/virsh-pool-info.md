# virsh pool-info

> 列出有关虚拟机存储池的信息。
> 参见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 列出由名称或 UUID 指定的存储池的名称、UUID、状态、持久性类型、是否开机启动、容量、已分配空间和可用空间（使用 `virsh pool-list` 确定名称或 UUID）：

`virsh pool-info --pool {{name|uuid}}`