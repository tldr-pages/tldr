# vgcreate

> 创建卷组，结合多个大容量存储设备。
> 另见：`lvm`。
> 更多信息：<https://manned.org/vgcreate>。

- 使用 `/dev/sda1` 设备创建一个名为 vg1 的新卷组：

`vgcreate {{vg1}} {{/dev/sda1}}`

- 使用多个设备创建一个名为 vg1 的新卷组：

`vgcreate {{vg1}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`