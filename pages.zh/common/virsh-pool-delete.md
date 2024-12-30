# virsh pool-delete

> 删除一个非活动虚拟机存储池的底层存储系统。
> 另请参见：`virsh`、`virsh-pool-destroy`、`virsh-pool-undefine`。
> 更多信息：<https://manned.org/virsh>。

- 删除指定名称或 UUID 的存储池的底层存储系统（使用 `virsh pool-list` 确定）：

`virsh pool-delete --pool {{name|uuid}}`