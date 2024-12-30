# cfdisk

> 使用 curses 用户界面管理硬盘上的分区表和分区。
> 更多信息：<https://manned.org/cfdisk>。

- 使用特定设备启动分区管理器：

`cfdisk {{/dev/sdX}}`

- 为特定设备创建新的分区表并进行管理：

`cfdisk --zero {{/dev/sdX}}`