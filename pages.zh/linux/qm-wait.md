# qm 等待

> 等待直到虚拟机停止。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 等待直到虚拟机停止：

`qm wait {{vm_id}}`

- 等待直到虚拟机停止，设置 10 秒超时：

`qm wait --timeout {{10}} {{vm_id}}`

- 发送关闭请求，然后等待直到虚拟机停止，设置 10 秒超时：

`qm shutdown {{vm_id}} && qm wait --timeout {{10}} {{vm_id}}`