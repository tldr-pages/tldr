# qm 暂停

> 在Proxmox虚拟环境（PVE）中暂停虚拟机（VM）。
> 使用`--skiplock`和`--skiplockstorage`标志时请谨慎，因为在某些情况下可能导致数据损坏。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 通过ID暂停虚拟机：

`qm suspend {{vm_id}} {{integer}}`

- 在暂停虚拟机时跳过锁检查：

`qm suspend {{vm_id}} {{integer}} --skiplock`

- 在暂停虚拟机时跳过存储的锁检查：

`qm suspend {{vm_id}} {{integer}} --skiplockstorage`