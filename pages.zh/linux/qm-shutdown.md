# qm 关闭

> 在 QEMU/KVM 虚拟机管理器上关闭虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 关闭虚拟机：

`qm shutdown {{VM_ID}}`

- 最多等待 10 秒后关闭虚拟机：

`qm shutdown --timeout {{10}} {{VM_ID}}`

- 关闭虚拟机并不禁用存储卷：

`qm shutdown --keepActive {{true}} {{VM_ID}}`

- 关闭虚拟机并跳过锁定（仅 root 可以使用此选项）：

`qm shutdown --skiplock {{true}} {{VM_ID}}`

- 强制停止并关闭虚拟机：

`qm shutdown --forceStop {{true}} {{VM_ID}}`