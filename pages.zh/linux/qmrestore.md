# qmrestore

> 恢复 QemuServer 的 `vzdump` 备份。
> 更多信息：<https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- 从给定的备份文件中恢复虚拟机到原始存储：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}}`

- 从给定的备份文件中覆盖已存在的虚拟机到原始存储：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --force true`

- 从给定的备份文件中将虚拟机恢复到指定的存储：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --storage {{local}}`

- 在恢复过程中立即启动虚拟机（仅在 Proxmox Backup Server 上可用）：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --live-restore true`