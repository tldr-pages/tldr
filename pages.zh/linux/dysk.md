# dysk

> 以表格形式显示文件系统信息。
> 更多信息：<https://dystroy.org/dysk>。

- 获取您常用磁盘的标准概览：

`dysk`

- 按可用空间排序：

`dysk --sort free`

- 仅包含 HDD 磁盘：

`dysk --filter 'disk = HDD'`

- 排除 SSD 磁盘：

`dysk --filter 'disk <> SSD'`

- 显示高使用率或低可用空间的磁盘：

`dysk --filter 'use > 65% | free < 50G'`