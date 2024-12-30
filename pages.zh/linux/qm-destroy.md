# qm 销毁

> 在 QEMU/KVM 虚拟机管理器中销毁虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 销毁特定虚拟机：

`qm destroy {{vm_id}}`

- 销毁在特定虚拟机配置中未明确引用的所有磁盘：

`qm destroy {{vm_id}} --destroy-unreferenced-disks`

- 销毁虚拟机并从所有位置（库存、备份作业、高可用性管理器等）中删除：

`qm destroy {{vm_id}} --purge`

- 销毁特定虚拟机，忽略锁并强制销毁：

`sudo qm destroy {{vm_id}} --skiplock`