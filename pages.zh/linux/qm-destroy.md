# qm destroy

> 在 QEMU/KVM 虚拟机管理器中销毁虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 销毁特定的虚拟机：

`qm destroy {{vm_id}}`

- 销毁特定虚拟机配置中未显式引用的所有磁盘：

`qm destroy {{vm_id}} --destroy-unreferenced-disks`

- 销毁虚拟机并从所有位置删除（库存、备份任务、高可用性管理器等）：

`qm destroy {{vm_id}} --purge`

- 忽略锁定并强制销毁特定的虚拟机：

`sudo qm destroy {{vm_id}} --skiplock`
