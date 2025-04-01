# fstrim

> 丢弃已安装文件系统中的未使用块。
> 仅支持闪存设备，如SSD和microSD卡。
> 更多信息：<https://manned.org/fstrim>。

- 修剪支持此功能的所有已挂载分区中的未使用块：

`sudo fstrim {{[-a|--all]}}`

- 修剪指定分区中的未使用块：

`sudo fstrim {{/}}`

- 修剪后显示统计信息：

`sudo fstrim {{[-v|--verbose]}} {{/}}`