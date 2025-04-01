# qm disk move

> 将虚拟磁盘从一个存储移动到同一个 Proxmox 集群中的另一个存储。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 移动虚拟磁盘：

`qm disk move {{vm_id}} {{destination}} {{index}}`

- 删除虚拟磁盘的旧副本：

`qm disk move -delete {{vm_id}} {{destination}} {{index}}`
