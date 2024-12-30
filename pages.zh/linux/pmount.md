# pmount

> 以普通用户身份挂载任意热插拔设备。
> 更多信息：<https://manned.org/pmount>。

- 将设备挂载到 `/media/` 目录下（使用设备作为挂载点）：

`pmount {{/dev/to/block/device}}`

- 将具有特定文件系统类型的设备挂载到 `/media/label`：

`pmount --type {{filesystem}} {{/dev/to/block/device}} {{label}}`

- 以只读模式挂载 CD-ROM（文件系统类型为 ISO9660）：

`pmount --type {{iso9660}} --read-only {{/dev/cdrom}}`

- 强制以读写访问挂载 NTFS 格式的磁盘：

`pmount --type {{ntfs}} --read-write {{/dev/sdX}}`

- 显示所有已挂载的可移动设备：

`pmount`