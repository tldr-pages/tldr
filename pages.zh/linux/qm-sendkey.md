# qm sendkey

> 将 QEMU 监控编码键事件发送到虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 将指定的键事件发送到特定的虚拟机：

`qm sendkey {{vm_id}} {{key}}`

- 允许 root 用户发送键事件并忽略锁定：

`qm sendkey --skiplock {{true}} {{vm_id}} {{key}}`