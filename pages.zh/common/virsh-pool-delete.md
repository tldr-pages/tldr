# virsh pool-delete

> 删除处于非活动状态的虚拟机存储池的基础存储系统。
> 参见：`virsh`，`virsh-pool-destroy`，`virsh-pool-undefine`。
> 更多信息：<https://manned.org/virsh>。

- 删除由名称或 UUID 指定的存储池的基础存储系统（使用 `virsh pool-list` 确定名称或 UUID）：

`virsh pool-delete --pool {{name|uuid}}`