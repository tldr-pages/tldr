# vgcreate

> 创建结合多个存储设备的卷组。
> 参见: `lvm`。
> 更多信息: <https://manned.org/vgcreate>。

- 使用 `/dev/sda1` 设备创建名为 vg1 的新卷组：

`vgcreate {{vg1}} {{/dev/sda1}}`

- 使用多个设备创建名为 vg1 的新卷组：

`vgcreate {{vg1}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`
