# vzdump

> 虚拟机和容器的备份工具。
> 更多信息：<https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- 将客户虚拟机备份到默认的备份目录（通常是 `/var/lib/vz/dump/`），不包括快照：

`vzdump {{vm_id}}`

- 备份 ID 为 101、102 和 103 的客户虚拟机：

`vzdump {{101 102 103}}`

- 使用特定模式备份客户虚拟机：

`vzdump {{vm_id}} --mode {{suspend|snapshot}}`

- 备份所有客户系统并发送通知邮件给 root 和 admin 用户：

`vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}`

- 使用快照模式（无需停机）并指定非默认的备份目录：

`vzdump {{vm_id}} --dumpdir {{path/to/directory}} --mode {{snapshot}}`

- 备份所有客户虚拟机，但排除 ID 为 101 和 102 的虚拟机：

`vzdump --mode {{suspend}} --exclude {{101, 102}}`
