# qm guest passwd

> 为 QEMU/KVM 虚拟机管理器中的用户设置密码。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 交互式地为虚拟机中的特定用户设置密码：

`qm guest passwd {{vm_id}} {{username}}`

- 交互式地为虚拟机中的特定用户设置一个已经哈希过的密码：

`qm guest passwd {{vm_id}} {{username}} --crypted 1`