# qmrestore

> 恢复 QemuServer 的 `vzdump` 备份。
> 更多信息：<https://pve.proxmox.com/pve-docs/qmrestore.1.html>。

- 从原始存储中的指定备份文件恢复虚拟机：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}}`

- 从原始存储中的指定备份文件覆盖现有虚拟机：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --force true`

- 从指定存储中的指定备份文件恢复虚拟机：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --storage {{local}}`

- 在后台恢复时立即从备份启动虚拟机（仅适用于 Proxmox Backup Server）：

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --live-restore true`