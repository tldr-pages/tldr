# badblocks

> 搜索设备上的坏块。
> 一些使用方式可能会导致破坏性操作，如擦除磁盘上的所有数据，包括分区表。
> 更多信息：<https://manned.org/badblocks>。

- 使用非破坏性只读测试搜索磁盘上的坏块：

`sudo badblocks {{/dev/sdX}}`

- 使用非破坏性读写测试搜索未挂载的磁盘上的坏块：

`sudo badblocks -n {{/dev/sdX}}`

- 使用破坏性写入测试搜索未挂载的磁盘上的坏块：

`sudo badblocks -w {{/dev/sdX}}`

- 使用破坏性写入测试并显示详细的进度：

`sudo badblocks -svw {{/dev/sdX}}`

- 在破坏模式下，将找到的坏块输出到文件：

`sudo badblocks -o {{path/to/file}} -w {{/dev/sdX}}`

- 使用 4K 块大小和 64K 块计数以提高速度的破坏模式：

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sdX}}`
