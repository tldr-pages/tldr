# dysk

> 以表格形式显示文件系统信息。
> 更多信息：<https://dystroy.org/dysk>.

- 获取常用磁盘的标准概述：

`dysk`

- 按空闲空间排序：

`dysk --sort free`

- 仅包含HDD磁盘：

`dysk --filter 'disk = HDD'`

- 排除SSD磁盘：

`dysk --filter 'disk <> SSD'`

- 显示利用率达高或空闲空间低的磁盘：

`dysk --filter 'use > 65% | free < 50G'`