# iostat

> 报告设备和分区的统计信息。
> 更多信息：<https://manned.org/iostat>.

- 显示系统启动以来的CPU和磁盘统计报告：

`iostat`

- 以MB为单位显示CPU和磁盘统计报告：

`iostat -m`

- 显示CPU统计信息：

`iostat {{[-c|--compact]}}`

- 显示包含磁盘名称（含LVM）的磁盘统计信息：

`iostat -N`

- 显示设备"sda"的扩展磁盘统计信息（包含磁盘名称）：

`iostat -xN {{sda}}`

- 每2秒显示一次CPU和磁盘的增量统计报告：

`iostat {{2}}`
