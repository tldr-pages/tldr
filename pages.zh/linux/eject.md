# eject

> 弹出光盘、软盘和磁带。
> 更多信息：<https://manned.org/eject>.

- 显示默认设备：

`eject {{[-d|--default]}}`

- 弹出默认设备：

`eject`

- 弹出特定设备（默认顺序为：cd-rom、scsi、软盘和磁带）：

`eject {{/dev/cdrom}}`

- 切换设备托盘的打开或关闭状态：

`eject {{[-T|--traytoggle]}} {{/dev/cdrom}}`

- 弹出光盘驱动器：

`eject {{[-r|--cdrom]}} {{/dev/cdrom}}`

- 弹出软盘驱动器：

`eject {{[-f|--floppy]}} {{/mnt/floppy}}`

- 弹出磁带驱动器：

`eject {{[-q|--tape]}} {{/mnt/tape}}`

- 设置物理弹出按钮是否被忽略（`on` 表示不允许弹出）：

`eject {{[-i|--manualeject]}} {{on|off}}`