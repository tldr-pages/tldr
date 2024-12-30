# qm 重启

> 通过关闭虚拟机并在应用待处理更改后再次启动它来重启虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 重启虚拟机：

`qm reboot {{vm_id}}`

- 在最多等待10秒后重启虚拟机：

`qm reboot --timeout {{10}} {{vm_id}}`