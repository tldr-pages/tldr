# woeusb

> Windows 安装媒体创建工具。
> 更多信息：<https://github.com/WoeUSB/WoeUSB>。

- 格式化 USB 并创建 Windows 安装启动盘：

`woeusb --device {{path/to/windows.iso}} {{/dev/sdX}}`

- 将 Windows 文件复制到 USB 存储设备的现有分区，并使其可引导，而不会删除现有数据：

`woeusb --partition {{path/to/windows.iso}} {{/dev/sdXN}}`