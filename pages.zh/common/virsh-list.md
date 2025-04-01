# virsh-list

> 列出虚拟机的 ID、名称和状态。
> 参见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 列出正在运行的虚拟机的信息：

`virsh list`

- 列出所有状态的虚拟机的信息：

`virsh list --all`

- 列出自动启动已启用或已禁用的虚拟机的信息：

`virsh list --all --{{autostart|no-autostart}}`

- 列出有快照或无快照的虚拟机的信息：

`virsh list --all --{{with-snapshot|without-snapshot}}`
