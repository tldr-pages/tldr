# virsh-list

> 列出虚拟机的ID、名称和状态。
> 另见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 列出运行中的虚拟机信息：

`virsh list`

- 列出所有虚拟机的信息，不论其状态：

`virsh list --all`

- 列出自动启动状态为启用或禁用的虚拟机信息：

`virsh list --all --{{autostart|no-autostart}}`

- 列出有快照或没有快照的虚拟机信息：

`virsh list --all --{{with-snapshot|without-snapshot}}`