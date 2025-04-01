# virsh pool-list

> 列出虚拟机存储池的信息。
> 参见：`virsh`，`virsh-pool-autostart`，`virsh-pool-define-as`。
> 更多信息：<https://manned.org/virsh>。

- 列出活动存储池的名称、状态和自动启动是否启用：

`virsh pool-list`

- 列出活动和非活动或仅非活动存储池的信息：

`virsh pool-list --{{all|inactive}}`

- 列出活动存储池的扩展信息，包括持久性、容量、分配和可用空间：

`virsh pool-list --details`

- 列出自动启动已启用或已禁用的活动存储池的信息：

`virsh pool-list --{{autostart|no-autostart}}`

- 列出持久或临时的活动存储池的信息：

`virsh pool-list --{{persistent|transient}}`

- 列出活动存储池的名称和 UUID：

`virsh pool-list --name --uuid`
