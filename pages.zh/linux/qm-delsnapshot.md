# qm delsnapshot

> 删除虚拟机快照。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 删除一个快照：

`qm delsnapshot {{vm_id}} {{snapshot_name}}`

- 从配置文件中删除一个快照（即使删除磁盘快照失败也继续）：

`qm delsnapshot {{vm_id}} {{snapshot_name}} --force 1`