# pvecm

> Proxmox VE 集群管理器。
> 更多信息：<https://pve.proxmox.com/pve-docs/pvecm.1.html>。

- 将当前节点添加到现有集群：

`pvecm add {{hostname_or_ip}}`

- 将节点添加到集群配置（内部使用）：

`pvecm addnode {{node}}`

- 显示此节点上可用的集群加入 API 版本：

`pvecm apiver`

- 生成新的集群配置：

`pvecm create {{clustername}}`

- 从集群配置中删除节点：

`pvecm delnode {{node}}`

- 显示集群节点的本地视图：

`pvecm nodes`

- 显示集群状态的本地视图：

`pvecm status`