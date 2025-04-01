# virsh-connect

> 连接到虚拟机管理程序。
> 参见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 连接到默认的管理程序：

`virsh connect`

- 以 root 身份连接到本地的 QEMU/KVM 管理程序：

`virsh connect qemu:///system`

- 启动新的管理程序实例并以本地用户身份连接到它：

`virsh connect qemu:///session`

- 通过 SSH 以 root 身份连接到远程管理程序：

`virsh connect qemu+ssh://{{user_name@host_name}}/system`