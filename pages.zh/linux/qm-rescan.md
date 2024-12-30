# qm 重新扫描

> 重新扫描所有存储并更新虚拟机的磁盘大小和未使用的磁盘映像。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 重新扫描所有存储并更新特定虚拟机的磁盘大小和未使用的磁盘映像：

`qm rescan {{vm_id}}`

- 在特定虚拟机上执行重新扫描的干运行，不对配置进行任何更改：

`qm rescan --dryrun {{true}} {{vm_id}}`