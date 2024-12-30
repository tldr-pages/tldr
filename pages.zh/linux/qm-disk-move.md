# qm 磁盘移动

> 在同一 Proxmox 集群内将虚拟磁盘从一个存储移动到另一个存储。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 移动虚拟磁盘：

`qm disk move {{vm_id}} {{destination}} {{index}}`

- 删除虚拟磁盘的先前副本：

`qm disk move -delete {{vm_id}} {{destination}} {{index}}`