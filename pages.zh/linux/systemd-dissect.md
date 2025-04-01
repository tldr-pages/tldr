# systemd-dissect

> 检查和与文件系统 OS 磁盘镜像交互，特别是可发现的磁盘镜像（DDIs）。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>。

- 显示 OS 镜像的常规信息：

`systemd-dissect {{path/to/image.raw}}`

- 挂载 OS 镜像：

`systemd-dissect --mount {{path/to/image.raw}} {{/mnt/image}}`

- 卸载 OS 镜像：

`systemd-dissect --umount {{/mnt/image}}`

- 列出镜像中的文件：

`systemd-dissect --list {{path/to/image.raw}}`

- 将 OS 镜像附加到自动分配的环回块设备，并打印其路径：

`systemd-dissect --attach {{path/to/image.raw}}`

- 从环回块设备中分离 OS 镜像：

`systemd-dissect --detach {{path/to/device}}`
