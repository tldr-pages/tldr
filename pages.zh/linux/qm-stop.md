# qm stop

> 停止虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 立即停止虚拟机：

`qm stop {{VM_ID}}`

- 停止虚拟机并最多等待10秒：

`qm stop --timeout {{10}} {{VM_ID}}`

- 停止虚拟机并跳过锁定（仅root用户可以使用此选项）：

`qm stop --skiplock {{true}} {{VM_ID}}`

- 停止虚拟机但不取消激活存储卷：

`qm stop --keepActive {{true}} {{VM_ID}}`