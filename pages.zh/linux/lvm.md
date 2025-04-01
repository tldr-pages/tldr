# lvm

> 使用逻辑卷管理器（LVM）的交互式 shell 管理物理卷、卷组和逻辑卷。
> 更多信息：<https://manned.org/lvm>.

- 启动逻辑卷管理器的交互式 shell：

`sudo lvm`

- 初始化一个磁盘或分区作为物理卷：

`sudo lvm pvcreate {{/dev/sdXY}}`

- 显示物理卷的信息：

`sudo lvm pvdisplay`

- 从 `/dev/sdXY` 的物理卷创建一个名为 vg1 的卷组：

`sudo lvm vgcreate {{vg1}} {{/dev/sdXY}}`

- 显示卷组的信息：

`sudo lvm vgdisplay`

- 从卷组 vg1 创建一个大小为 10G 的逻辑卷：

`sudo lvm lvcreate -L {{10G}} {{vg1}}`

- 显示逻辑卷的信息：

`sudo lvm lvdisplay`

- 显示特定命令的帮助：

`lvm help {{command}}`