# sfdisk

> 显示或操作磁盘分区表。
> 更多信息：<https://manned.org/sfdisk>.

- 将分区布局备份到文件：

`sudo sfdisk {{[-d|--dump]}} {{path/to/device}} > {{path/to/file.dump}}`

- 恢复分区布局：

`sudo sfdisk {{path/to/device}} < {{path/to/file.dump}}`

- 设置分区类型：

`sfdisk --part-type {{path/to/device}}} {{partition_number}} {{swap}}`

- 删除分区：

`sfdisk --delete {{path/to/device}} {{partition_number}}`

- 显示帮助：

`sfdisk {{[-h|--help]}}`