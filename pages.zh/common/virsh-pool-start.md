# virsh pool-start

> 启动之前已配置但未激活的虚拟机存储池。
> 另见：`virsh`，`virsh-pool-define-as`，`virsh-pool-destroy`。
> 更多信息：<https://manned.org/virsh>。

- 启动由名称或 UUID 指定的存储池（可以使用 `virsh pool-list` 确定），并在存储系统不存在时创建它：

`virsh pool-start --pool {{name|uuid}} --build`