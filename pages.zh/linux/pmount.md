# pmount

> 以普通用户身份挂载任意可热插拔的设备。
> 更多信息：<https://manned.org/pmount>.

- 挂载设备到 `/media/` 目录下（使用设备作为挂载点）：

`pmount {{/dev/to/block/device}}`

- 挂载具有特定文件系统的设备到 `/media/label`：

`pmount --type {{filesystem}} {{/dev/to/block/device}} {{label}}`

- 以只读模式挂载 CD-ROM（文件系统类型 ISO9660）：

`pmount --type {{iso9660}} --read-only {{/dev/cdrom}}`

- 挂载一个 NTFS 格式的磁盘，并强制以读写模式访问：

`pmount --type {{ntfs}} --read-write {{/dev/sdX}}`

- 显示所有已挂载的可移动设备：

`pmount`