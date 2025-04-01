# vgchange

> 更改逻辑卷管理器 (LVM) 卷组的属性。
> 参见：`lvm`。
> 更多信息：<https://manned.org/vgchange>。

- 更改所有卷组中逻辑卷的激活状态：

`sudo vgchange --activate {{y|n}}`

- 更改指定卷组中逻辑卷的激活状态（使用 `vgscan` 确定卷组）：

`sudo vgchange --activate {{y|n}} {{volume_group}}`