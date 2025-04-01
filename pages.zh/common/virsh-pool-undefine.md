# virsh pool-undefine

> 删除已停止的虚拟机存储池在 `/etc/libvirt/storage` 中的配置文件。
> 参见：`virsh`，`virsh-pool-destroy`。
> 更多信息：<https://manned.org/virsh>。

- 删除指定名称或 UUID 的存储池的配置（使用 `virsh pool-list` 确定名称或 UUID）：

`virsh pool-undefine --pool {{name|uuid}}`
