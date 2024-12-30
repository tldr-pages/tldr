# 弹出

> 弹出CD、软盘和磁带驱动器。
> 更多信息：<https://manned.org/eject>。

- 显示默认设备：

`eject -d`

- 弹出默认设备：

`eject`

- 弹出特定设备（默认顺序为CD-ROM、SCSI、软盘和磁带）：

`eject {{/dev/cdrom}}`

- 切换设备的托盘是打开还是关闭：

`eject -T {{/dev/cdrom}}`

- 弹出CD驱动器：

`eject -r {{/dev/cdrom}}`

- 弹出软盘驱动器：

`eject -f {{/mnt/floppy}}`

- 弹出磁带驱动器：

`eject -q {{/mnt/tape}}`