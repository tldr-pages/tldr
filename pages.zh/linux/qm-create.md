# qm create

> 在 QEMU/KVM 虚拟机管理器上创建或恢复虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 创建虚拟机：

`qm create {{100}}`

- 创建后自动启动虚拟机：

`qm create {{100}} --start 1`

- 指定虚拟机上的操作系统类型：

`qm create {{100}} --ostype {{win10}}`

- 替换现有虚拟机（需要先归档）：

`qm create {{100}} --archive {{path/to/backup_file.tar}} --force 1`

- 指定根据虚拟机状态自动执行的脚本：

`qm create {{100}} --hookscript {{path/to/script.pl}}`
