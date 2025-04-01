# qm wait

> 等待虚拟机停止。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 等待虚拟机停止：

`qm wait {{vm_id}}`

- 等待虚拟机在10秒超时内停止：

`qm wait --timeout {{10}} {{vm_id}}`

- 发送关机请求，然后等待虚拟机在10秒超时内停止：

`qm shutdown {{vm_id}} && qm wait --timeout {{10}} {{vm_id}}`
