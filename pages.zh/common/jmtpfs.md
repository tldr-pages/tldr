# jmtpfs

> 基于 FUSE 的文件系统，用于访问 MTP 设备。
> 更多信息：<https://manned.org/jmtpfs>。

- 将 MTP 设备挂载到目录：

`jmtpfs {{path/to/directory}}`

- 设置挂载选项：

`jmtpfs -o {{allow_other,auto_unmount}} {{path/to/directory}}`

- 列出可用的 MTP 设备：

`jmtpfs --listDevices`

- 如果有多个设备，挂载特定设备：

`jmtpfs -device={{bus_id}},{{device_id}} {{path/to/directory}}`

- 卸载 MTP 设备：

`fusermount -u {{path/to/directory}}`