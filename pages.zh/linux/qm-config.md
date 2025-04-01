# qm config

> 显示应用了待处理配置变更的虚拟机配置。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 显示虚拟机配置：

`qm config {{vm_id}}`

- 显示虚拟机的当前配置值，而不是待处理的配置值：

`qm config --current {{true}} {{vm_id}}`

- 从给定的快照中获取配置值：

`qm config --snapshot {{snapshot_name}} {{vm_id}}`