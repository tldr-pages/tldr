# virsh-connect

> 连接到虚拟机管理程序。
> 另见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 连接到默认的管理程序：

`virsh connect`

- 以root身份连接到本地QEMU/KVM管理程序：

`virsh connect qemu:///system`

- 启动一个新的管理程序实例并以本地用户身份连接：

`virsh connect qemu:///session`

- 以root身份通过SSH连接到远程管理程序：

`virsh connect qemu+ssh://{{user_name@host_name}}/system`