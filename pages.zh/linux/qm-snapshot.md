# qm snapshot

> 创建虚拟机快照。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 创建特定虚拟机的快照：

`qm snapshot {{vm_id}} {{snapshot_name}}`

- 创建具有特定描述的快照：

`qm snapshot {{vm_id}} {{snapshot_name}} --description {{description}}`

- 创建包含虚拟机状态的快照：

`qm snapshot {{vm_id}} {{snapshot_name}} --description {{description}} --vmstate 1`