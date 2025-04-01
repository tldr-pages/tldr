# qm resume

> 恢复虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 恢复特定的虚拟机：

`qm resume {{vm_id}}`

- 恢复特定的虚拟机并忽略锁（需要 root 权限）：

`sudo qm resume {{vm_id}} --skiplock true`