# f3probe

> 检测块设备（例如闪存盘或 microSD 卡）是否有伪造的闪存。
> 参见：`f3read`，`f3write`，`f3fix`。
> 更多信息：<https://github.com/AltraMayor/f3>。

- 检测块设备：

`sudo f3probe {{path/to/block_device}}`

- 使用尽可能少的内存：

`sudo f3probe --min-memory {{path/to/block_device}}`

- 计时磁盘操作：

`sudo f3probe --time-ops {{path/to/block_device}}`
