# virsh pool-start

> 启动一个之前配置但处于非活动状态的虚拟机存储池。
> 另见：`virsh`，`virsh-pool-define-as`，`virsh-pool-destroy`。
> 更多信息：<https://manned.org/virsh>。

- 启动指定名称或UUID的存储池（使用 `virsh pool-list` 确定），如果底层存储系统不存在，则创建它：

`virsh pool-start --pool {{name|uuid}} --build`