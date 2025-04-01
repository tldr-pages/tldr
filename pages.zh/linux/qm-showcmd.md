# qm showcmd

> 显示用于启动虚拟机的命令行（调试信息）。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 显示特定虚拟机的命令行：

`qm showcmd {{vm_id}}`

- 将每个选项放在新行以提高可读性：

`qm showcmd --pretty {{true}} {{vm_id}}`

- 从特定快照中获取配置值：

`qm showcmd --snapshot {{string}} {{vm_id}}`
