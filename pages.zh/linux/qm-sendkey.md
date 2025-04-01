# qm sendkey

> 向虚拟机发送 QEMU 监控编码的按键事件。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 向特定的虚拟机发送指定的按键事件：

`qm sendkey {{vm_id}} {{key}}`

- 允许根用户发送按键事件并忽略锁：

`qm sendkey --skiplock {{true}} {{vm_id}} {{key}}`
