# qm rescan

> 重新扫描所有存储，并更新虚拟机的磁盘大小和未使用的磁盘映像。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 重新扫描所有存储，并更新特定虚拟机的磁盘大小和未使用的磁盘映像：

`qm rescan {{vm_id}}`

- 对特定虚拟机进行重新扫描的预演，并不将任何更改写入配置文件：

`qm rescan --dryrun {{true}} {{vm_id}}`
