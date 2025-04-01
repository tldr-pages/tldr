# qm suspend

> 在 Proxmox 虚拟环境中（PVE）挂起虚拟机（VM）。
> 使用 `--skiplock` 和 `--skiplockstorage` 标志时要谨慎，因为在某些情况下可能导致数据损坏。
> 更多信息： <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 通过 ID 挂起虚拟机：

`qm suspend {{vm_id}} {{integer}}`

- 挂起 VM 时跳过锁检查：

`qm suspend {{vm_id}} {{integer}} --skiplock`

- 挂起 VM 时跳过存储锁检查：

`qm suspend {{vm_id}} {{integer}} --skiplockstorage`