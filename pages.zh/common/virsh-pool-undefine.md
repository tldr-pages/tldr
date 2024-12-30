# virsh pool-undefine

> 删除停止的虚拟机存储池在 `/etc/libvirt/storage` 中的配置文件。
> 另见: `virsh`, `virsh-pool-destroy`。
> 更多信息: <https://manned.org/virsh>。

- 删除指定名称或UUID的存储池的配置（使用 `virsh pool-list` 确定）：

`virsh pool-undefine --pool {{name|uuid}}`