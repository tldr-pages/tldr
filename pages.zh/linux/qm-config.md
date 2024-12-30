# qm 配置

> 显示虚拟机配置，并应用待处理的配置更改。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 显示虚拟机配置：

`qm config {{vm_id}}`

- 显示虚拟机当前的配置值，而不是待处理的值：

`qm config --current {{true}} {{vm_id}}`

- 从给定快照中获取配置值：

`qm config --snapshot {{snapshot_name}} {{vm_id}}`