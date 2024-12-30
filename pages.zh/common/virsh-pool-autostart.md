# virsh pool-autostart

> 启用或禁用虚拟机存储池的自动启动。
> 另见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 为指定名称或UUID的存储池启用自动启动（使用 `virsh pool-list` 确定）：

`virsh pool-autostart --pool {{name|uuid}}`

- 为指定名称或UUID的存储池禁用自动启动：

`virsh pool-autostart --pool {{name|uuid}} --disable`