# qm clone

> 在 QEMU/KVM 虚拟机管理器上创建虚拟机的副本。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 复制一个虚拟机：

`qm copy {{vm_id}} {{new_vm_id}}`

- 使用特定名称复制一个虚拟机：

`qm copy {{vm_id}} {{new_vm_id}} --name {{name}}`

- 使用特定描述复制一个虚拟机：

`qm copy {{vm_id}} {{new_vm_id}} --description {{description}}`

- 创建一个所有磁盘的完整副本：

`qm copy {{vm_id}} {{new_vm_id}} --full`

- 使用特定格式的文件存储复制一个虚拟机（需要 `--full`）：

`qm copy {{vm_id}} {{new_vm_id}} --full --format {{qcow2|raw|vmdk}}`

- 复制一个虚拟机并将其添加到特定的资源池：

`qm copy {{vm_id}} {{new_vm_id}} --pool {{pool_name}}`