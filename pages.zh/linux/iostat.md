# iostat

> 报告设备和分区的统计信息。
> 更多信息：<https://manned.org/iostat>。

- 显示系统启动以来的 CPU 和磁盘统计报告：

`iostat`

- 以 MB 为单位显示 CPU 和磁盘统计报告：

`iostat -m`

- 显示 CPU 统计信息：

`iostat {{[-c|--compact]}}`

- 显示包含磁盘名称（含 LVM）的磁盘统计信息：

`iostat -N`

- 显示设备"sda"的扩展磁盘统计信息（包含磁盘名称）：

`iostat -xN {{sda}}`

- 每 2 秒显示一次 CPU 和磁盘的增量统计报告：

`iostat {{2}}`
