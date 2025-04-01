# virsh pool-build

> 构建虚拟机存储池底层的存储系统，该存储池在其配置文件 `/etc/libvirt/storage` 中定义。
> 参见: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`。
> 更多信息: <https://manned.org/virsh>.

- 构建由名称或 UUID 指定的存储池（使用 `virsh pool-list` 确定）:

`virsh pool-build --pool {{name|uuid}}`