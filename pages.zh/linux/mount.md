# mount

> 将整个文件系统挂载到一个目录下。
> 更多信息：<https://manned.org/mount.8>。

- 显示所有已挂载的文件系统：

`mount`

- 将设备挂载到目录：

`mount {{[-t|--types]}} {{文件系统类型}} {{路径/到/设备文件}} {{路径/到/目标目录}}`

- 如果指定的目录不存在则创建它，并将设备挂载到该目录：

`mount {{[-m|--mkdir]}} {{路径/到/设备文件}} {{路径/到/目标目录}}`

- 为特定用户挂载设备到目录：

`mount {{[-o|--options]}} uid={{用户ID}},gid={{组ID}} {{路径/到/设备文件}} {{路径/到/目标目录}}`

- 将 CD-ROM 设备（文件类型为 ISO9660）以只读方式挂载到 `/cdrom`：

`mount {{[-t|--types]}} {{iso9660}} {{[-o|--options]}} ro {{/dev/cdrom}} {{/cdrom}}`

- 挂载 `/etc/fstab` 中定义的所有文件系统：

`mount {{[-a|--all]}}`

- 挂载 `/etc/fstab` 中描述的特定文件系统（例如：`/dev/sda1 /my_drive ext2 defaults 0 2`）：

`mount {{/my_drive}}`

- 将一个目录挂载到另一个目录：

`mount {{[-B|--bind]}} {{路径/到/旧目录}} {{路径/到/新目录}}`