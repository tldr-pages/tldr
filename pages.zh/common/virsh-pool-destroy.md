# virsh pool-destroy

> 停止活动的虚拟机存储池。
> 参见：`virsh`，`virsh-pool-delete`。
> 更多信息：<https://manned.org/virsh>。

- 停止通过名称或 UUID 指定的存储池（使用 `virsh pool-list` 查看名称或 UUID）：

`virsh pool-destroy --pool {{name|uuid}}`
