# vzdump

> 虚拟机和容器的备份工具。
> 更多信息：<https://pve.proxmox.com/pve-docs/vzdump.1.html>。

- 将一个来宾虚拟机转储到默认的转储目录（通常是 `/var/lib/vz/dump/`），排除快照：

`vzdump {{vm_id}}`

- 备份ID为101、102和103的来宾虚拟机：

`vzdump {{101 102 103}}`

- 使用特定模式转储来宾虚拟机：

`vzdump {{vm_id}} --mode {{suspend|snapshot}}`

- 备份所有来宾系统，并向root和admin用户发送通知邮件：

`vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}`

- 使用快照模式（无需停机）和非默认的转储目录：

`vzdump {{vm_id}} --dumpdir {{path/to/directory}} --mode {{snapshot}}`

- 备份所有来宾虚拟机，排除ID为101和102的虚拟机：

`vzdump --mode {{suspend}} --exclude {{101, 102}}`