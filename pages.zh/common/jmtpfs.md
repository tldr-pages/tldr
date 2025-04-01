# jmtpfs

> 基于 FUSE 的文件系统，用于访问 MTP 设备。
> 更多信息：<https://manned.org/jmtpfs>.

- 将一个 MTP 设备挂载到一个目录：

`jmtpfs {{路径/到/目录}}`

- 设置挂载选项：

`jmtpfs -o {{allow_other,auto_unmount}} {{路径/到/目录}}`

- 列出可用的 MTP 设备：

`jmtpfs --listDevices`

- 如果存在多个设备，挂载一个特定的设备：

`jmtpfs -device={{总线_id}},{{设备_id}} {{路径/到/目录}}`

- 卸载 MTP 设备：

`fusermount -u {{路径/到/目录}}`
