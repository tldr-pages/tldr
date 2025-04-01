# qm disk resize

> 在 Proxmox Virtual Environment (PVE) 中调整虚拟机磁盘的大小。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 为虚拟磁盘增加 `n` 吉字节：

`qm disk resize {{vm_id}} {{disk_name}} +{{n}}G`
