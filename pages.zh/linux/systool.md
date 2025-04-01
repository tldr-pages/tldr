# systool

> 通过总线和类查看系统设备信息。
> 此命令是 `sysfs` 包的一部分。
> 更多信息：<https://github.com/linux-ras/sysfsutils>。

- 列出总线（例如 `pci`、`usb`）上的所有设备属性。使用 `ls /sys/bus` 查看所有总线：

`systool -b {{bus}} -v`

- 列出设备类（例如 `drm`、`block`）的所有属性。使用 `ls /sys/class` 查看所有类：

`systool -c {{class}} -v`

- 仅显示总线（例如 `pci`、`usb`）上的设备驱动程序：

`systool -b {{bus}} -D`