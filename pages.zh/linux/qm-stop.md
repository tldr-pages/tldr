# qm 停止

> 停止一个虚拟机。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 立即停止一个虚拟机：

`qm stop {{VM_ID}}`

- 停止一个虚拟机，最多等待 10 秒：

`qm stop --timeout {{10}} {{VM_ID}}`

- 停止一个虚拟机并跳过锁定（只有 root 用户可以使用此选项）：

`qm stop --skiplock {{true}} {{VM_ID}}`

- 停止一个虚拟机并保持存储卷激活：

`qm stop --keepActive {{true}} {{VM_ID}}`