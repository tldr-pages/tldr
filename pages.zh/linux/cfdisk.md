# cfdisk

> 使用 curses 界面管理硬盘上的分区表和分区。
> 更多信息：<https://manned.org/cfdisk>。

- 使用特定设备启动分区管理器：

`cfdisk {{/dev/sdX}}`

- 为特定设备创建一个新的分区表并管理它：

`cfdisk {{[-z|--zero]}} {{/dev/sdX}}`