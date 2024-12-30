# udisksctl

> 与 `udisksd` 交互以查询和操作存储设备。
> 更多信息：<https://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>。

- 显示有关磁盘驱动器和块设备的高级信息：

`udisksctl status`

- 显示有关设备的详细信息：

`udisksctl info --block-device {{/dev/sdX}}`

- 显示有关设备分区的详细信息：

`udisksctl info --block-device {{/dev/sdXN}}`

- 挂载设备分区并打印挂载点：

`udisksctl mount --block-device {{/dev/sdXN}}`

- 卸载设备分区：

`udisksctl unmount --block-device {{/dev/sdXN}}`

- 监控守护进程以获取事件：

`udisksctl monitor`