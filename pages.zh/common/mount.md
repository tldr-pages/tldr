# 挂载

> 在一个目录中访问整个文件系统。
> 更多信息：<https://manned.org/mount.8>。

- 显示所有已挂载的文件系统：

`mount`

- 将设备挂载到目录：

`mount -t {{文件系统类型}} {{设备文件路径}} {{目标目录路径}}`

- 如果目录不存在则创建特定目录并将设备挂载到该目录：

`mount --mkdir {{设备文件路径}} {{目标目录路径}}`

- 将设备挂载到特定用户的目录：

`mount -o uid={{用户ID}},gid={{组ID}} {{设备文件路径}} {{目标目录路径}}`

- 将CD-ROM设备（文件类型为ISO9660）挂载到`/cdrom`（只读）：

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- 挂载在`/etc/fstab`中定义的所有文件系统：

`mount -a`

- 挂载在`/etc/fstab`中描述的特定文件系统（例如`/dev/sda1 /my_drive ext2 defaults 0 2`）：

`mount {{/my_drive}}`

- 将一个目录挂载到另一个目录：

`mount --bind {{旧目录路径}} {{新目录路径}}`