# f3probe

> 探测块设备（例如闪存驱动器或microSD卡）以检测伪造的闪存内存。
> 另见：`f3read`，`f3write`，`f3fix`。
> 更多信息：<https://github.com/AltraMayor/f3>。

- 探测块设备：

`sudo f3probe {{路径/到/块设备}}`

- 使用最少的RAM：

`sudo f3probe --min-memory {{路径/到/块设备}}`

- 计时磁盘操作：

`sudo f3probe --time-ops {{路径/到/块设备}}`