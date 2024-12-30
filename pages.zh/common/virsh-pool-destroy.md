# virsh pool-destroy

> 停止一个活动的虚拟机存储池。
> 另见：`virsh`，`virsh-pool-delete`。
> 更多信息：<https://manned.org/virsh>。

- 停止指定名称或UUID的存储池（使用 `virsh pool-list` 确定）：

`virsh pool-destroy --pool {{name|uuid}}`