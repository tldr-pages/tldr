# virsh pool-build

> 根据在 `/etc/libvirt/storage` 中的配置文件定义，构建虚拟机存储池的基础存储系统。
> 另请参见： `virsh`, `virsh-pool-define-as`, `virsh-pool-start`。
> 更多信息： <https://manned.org/virsh>。

- 构建通过名称或 UUID 指定的存储池（使用 `virsh pool-list` 确定）：

`virsh pool-build --pool {{name|uuid}}`