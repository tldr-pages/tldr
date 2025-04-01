# qm reboot

> 通过关闭虚拟机并应用待处理的更改后重新启动虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 重新启动虚拟机：

`qm reboot {{vm_id}}`

- 等待最多 10 秒后重新启动虚拟机：

`qm reboot --timeout {{10}} {{vm_id}}`
