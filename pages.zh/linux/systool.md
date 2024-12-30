# systool

> 按总线和类别查看系统设备信息。
> 此命令是 `sysfs` 包的一部分。
> 更多信息：<https://github.com/linux-ras/sysfsutils>。

- 列出某个总线（例如 `pci`、`usb`）的所有设备属性。使用 `ls /sys/bus` 查看所有总线：

`systool -b {{bus}} -v`

- 列出某个设备类别（例如 `drm`、`block`）的所有设备属性。使用 `ls /sys/class` 查看所有类别：

`systool -c {{class}} -v`

- 仅显示某个总线（例如 `pci`、`usb`）的设备驱动程序：

`systool -b {{bus}} -D`