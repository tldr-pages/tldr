# woeusb

> Windows 媒体创建工具。
> 更多信息：<https://github.com/WoeUSB/WoeUSB>。

- 格式化 USB 然后创建一个可启动的 Windows 安装驱动器：

`woeusb --device {{path/to/windows.iso}} {{/dev/sdX}}`

- 将 Windows 文件复制到 USB 存储设备的现有分区，并使其可启动，而不删除当前数据：

`woeusb --partition {{path/to/windows.iso}} {{/dev/sdXN}}`