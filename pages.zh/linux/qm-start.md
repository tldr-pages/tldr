# qm 启动

> 在 QEMU/KVM 虚拟机管理器上启动虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 启动特定的虚拟机：

`qm start {{100}}`

- 指定 QEMU 机器类型（即要模拟的 CPU）：

`qm start {{100}} --machine {{q35}}`

- 启动特定的虚拟机，超时时间为 60 秒：

`qm start {{100}} --timeout {{60}}`