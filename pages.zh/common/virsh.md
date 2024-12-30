# virsh

> 管理 `virsh` 客户域。 （注意：`guest_id` 可以是客户的 ID、名称或 UUID）。
> 一些子命令如 `list` 有自己的使用文档。
> 更多信息：<https://libvirt.org/manpages/virsh.html>。

- 连接到虚拟机监控器会话：

`virsh connect {{qemu:///system}}`

- 激活名为 `default` 的网络：

`virsh net-start {{default}}`

- 列出所有域：

`virsh list --all`

- 从配置文件创建一个客户：

`virsh create {{path/to/config_file.xml}}`

- 编辑客户的配置文件（编辑器可以通过 $EDITOR 改变）：

`virsh edit {{guest_id}}`

- 启动/重启/关闭/挂起/恢复一个客户：

`virsh {{command}} {{guest_id}}`

- 将客户的当前状态保存到文件中：

`virsh save {{guest_id}} {{filename}}`

- 删除一个正在运行的客户：

`virsh destroy {{guest_id}} && virsh undefine {{guest_id}}`