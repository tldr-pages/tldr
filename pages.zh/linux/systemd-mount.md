# systemd-mount

> 建立和销毁临时挂载点或自动挂载点。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-mount.html>。

- 将文件系统（映像或块设备）挂载到 `/run/media/system/LABEL`，其中 LABEL 是文件系统的卷标或如果无卷标则为设备名称：

`systemd-mount {{path/to/file_or_device}}`

- 将文件系统（映像或块设备）挂载到指定位置：

`systemd-mount {{path/to/file_or_device}} {{path/to/mount_point}}`

- 列出所有本地已知的可以挂载的带有文件系统的块设备：

`systemd-mount --list`

- 创建一个自动挂载点，在首次访问时挂载实际的文件系统：

`systemd-mount --automount=yes {{path/to/file_or_device}}`

- 卸载一个或多个设备：

`systemd-mount --umount {{path/to/mount_point_or_device1}} {{path/to/mount_point_or_device2}}`

- 以特定文件系统类型挂载文件系统（映像或块设备）：

`systemd-mount --type={{file_system_type}} {{path/to/file_or_device}} {{path/to/mount_point}}`

- 以额外的挂载选项挂载文件系统（映像或块设备）：

`systemd-mount --options={{mount_options}} {{path/to/file_or_device}} {{path/to/mount_point}}`