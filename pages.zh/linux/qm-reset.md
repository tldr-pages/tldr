# qm reset

> 重置 QEMU/KVM 虚拟机管理器上的虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 重置虚拟机：

`qm reset {{vm_id}}`

- 重置虚拟机并跳过锁（仅 root 用户可以使用此选项）：

`qm reset --skiplock {{true}} {{vm_id}}`