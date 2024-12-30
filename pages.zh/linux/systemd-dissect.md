# systemd-dissect

> 反省和与文件系统操作系统磁盘映像交互，特别是可发现磁盘映像（DDIs）。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>。

- 显示有关操作系统映像的一般信息：

`systemd-dissect {{path/to/image.raw}}`

- 挂载操作系统映像：

`systemd-dissect --mount {{path/to/image.raw}} {{/mnt/image}}`

- 卸载操作系统映像：

`systemd-dissect --umount {{/mnt/image}}`

- 列出映像中的文件：

`systemd-dissect --list {{path/to/image.raw}}`

- 将操作系统映像附加到自动分配的回环块设备并打印其路径：

`systemd-dissect --attach {{path/to/image.raw}}`

- 从回环块设备分离操作系统映像：

`systemd-dissect --detach {{path/to/device}}`