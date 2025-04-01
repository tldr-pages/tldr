# virsh pool-autostart

> 启用或禁用虚拟机存储池的自启动功能。
> 参见：`virsh`。
> 更多信息：<https://manned.org/virsh>。

- 启用指定名称或 UUID 的存储池的自启动功能（使用 `virsh pool-list` 确定）：

`virsh pool-autostart --pool {{name|uuid}}`

- 禁用指定名称或 UUID 的存储池的自启动功能：

`virsh pool-autostart --pool {{name|uuid}} --disable`