# qm migrate

> 迁移虚拟机。
> 用于创建新的迁移任务。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 迁移特定的虚拟机：

`qm migrate {{vm_id}} {{target}}`

- 覆盖当前的 I/O 带宽限制为 10 KiB/s：

`qm migrate {{vm_id}} {{target}} --bwlimit 10`

- 允许迁移使用本地设备的虚拟机（仅限 root 用户）：

`qm migrate {{vm_id}} {{target}} --force true`

- 如果虚拟机正在运行，则使用在线/实时迁移：

`qm migrate {{vm_id}} {{target}} --online true`

- 为本地磁盘启用实时存储迁移：

`qm migrate {{vm_id}} {{target}} --with-local-disks true`
