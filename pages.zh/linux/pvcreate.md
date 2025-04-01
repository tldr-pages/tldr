# pvcreate

> 初始化磁盘或分区以用作物理卷。
> 参见：`lvm`。
> 更多信息：<https://manned.org/pvcreate>。

- 初始化 `/dev/sda1` 卷以供 LVM 使用：

`pvcreate {{/dev/sda1}}`

- 强制创建而不进行任何确认提示：

`pvcreate --force {{/dev/sda1}}`