# qm

> QEMU/KVM 虚拟机管理器。
> 一些子命令如 `list`、`start`、`stop`、`clone` 等有自己的使用文档。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 列出所有虚拟机：

`qm list`

- 使用上传到本地存储的 ISO 文件，创建一个具有 4 GB IDE 磁盘（位于 `local-lvm` 存储）和 ID 为 100 的虚拟机：

`qm create {{100}} -ide0 {{local-lvm:4}} -net0 {{e1000}} -cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- 显示指定 ID 的虚拟机的配置：

`qm config {{100}}`

- 启动一个特定的虚拟机：

`qm start {{100}}`

- 发送关机请求，然后等待虚拟机停止：

`qm shutdown {{100}} && qm wait {{100}}`

- 销毁虚拟机并移除所有相关资源：

`qm destroy {{100}} --purge`
