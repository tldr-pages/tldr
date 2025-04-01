# iostat

> 报告设备和分区的统计信息。
> 更多信息：<https://manned.org/iostat>.

- 显示自系统启动以来的 CPU 和磁盘统计信息：

`iostat`

- 以兆字节为单位显示 CPU 和磁盘统计信息：

`iostat -m`

- 显示 CPU 统计信息：

`iostat {{[-c|--compact]}}`

- 显示磁盘统计信息，包括磁盘名称（包含 LVM）：

`iostat -N`

- 显示设备 "sda" 的扩展磁盘统计信息，包括磁盘名称：

`iostat -xN {{sda}}`

- 每隔 2 秒显示一次 CPU 和磁盘的增量统计信息：

`iostat {{2}}`