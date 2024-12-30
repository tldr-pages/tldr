# fstrim

> 在已挂载的文件系统上丢弃未使用的块。
> 仅支持闪存设备，如SSD和microSD卡。
> 更多信息：<https://manned.org/fstrim>。

- 在所有支持的已挂载分区上丢弃未使用的块：

`sudo fstrim --all`

- 在指定分区上丢弃未使用的块：

`sudo fstrim {{/}}`

- 在修剪后显示统计信息：

`sudo fstrim --verbose {{/}}`