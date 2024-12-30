# virsh pool-list

> 列出虚拟机存储池的信息。
> 另见：`virsh`，`virsh-pool-autostart`，`virsh-pool-define-as`。
> 更多信息：<https://manned.org/virsh>。

- 列出活动存储池的名称、状态以及是否启用了自动启动：

`virsh pool-list`

- 列出活动和非活动存储池的信息，或仅列出非活动存储池：

`virsh pool-list --{{all|inactive}}`

- 列出活动存储池的持久性、容量、分配和可用空间的详细信息：

`virsh pool-list --details`

- 列出自动启动已启用或禁用的活动存储池的信息：

`virsh pool-list --{{autostart|no-autostart}}`

- 列出活动存储池是持久的还是临时的信息：

`virsh pool-list --{{persistent|transient}}`

- 列出活动存储池的名称和UUID：

`virsh pool-list --name --uuid`