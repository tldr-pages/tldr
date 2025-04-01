# qm cleanup

> 清理 QEMU/KVM 虚拟机管理器上的资源，如 tap 设备、VGPU 等。
> 在虚拟机关闭、崩溃等情况下调用。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 清理资源：

`qm cleanup {{vm_id}} {{clean-shutdown}} {{guest-requested}}`
