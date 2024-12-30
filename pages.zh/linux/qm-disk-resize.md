# qm 磁盘调整大小

> 在 Proxmox 虚拟环境 (PVE) 中调整虚拟机磁盘的大小。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 向虚拟磁盘添加 `n` 吉字节：

`qm disk resize {{vm_id}} {{disk_name}} +{{n}}G`