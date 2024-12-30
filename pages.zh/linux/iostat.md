# iostat

> 报告设备和分区的统计信息。
> 更多信息：<https://manned.org/iostat>。

- 显示从系统启动以来的 CPU 和磁盘统计信息报告：

`iostat`

- 显示单位转换为兆字节的 CPU 和磁盘统计信息报告：

`iostat -m`

- 显示 CPU 统计信息：

`iostat -c`

- 显示带有磁盘名称（包括 LVM）的磁盘统计信息：

`iostat -N`

- 显示设备 "sda" 的扩展磁盘统计信息及其磁盘名称：

`iostat -xN {{sda}}`

- 每 2 秒显示一次 CPU 和磁盘统计信息的增量报告：

`iostat {{2}}`