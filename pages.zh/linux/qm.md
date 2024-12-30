# qm

> QEMU/KVM 虚拟机管理器。
> 一些子命令，如 `list`、`start`、`stop`、`clone` 等，有自己的使用文档。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 列出所有虚拟机：

`qm list`

- 使用上传到本地存储的 ISO 文件，在 `local-lvm` 存储上创建一个 4 GB 的 IDE 磁盘，ID 为 100：

`qm create {{100}} -ide0 {{local-lvm:4}} -net0 {{e1000}} -cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- 显示指定 ID 虚拟机的配置：

`qm config {{100}}`

- 启动特定的虚拟机：

`qm start {{100}}`

- 发送关闭请求，然后等待虚拟机关机：

`qm shutdown {{100}} && qm wait {{100}}`

- 销毁虚拟机并删除所有相关资源：

`qm destroy {{100}} --purge`