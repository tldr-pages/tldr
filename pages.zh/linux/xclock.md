# xclock

> 以模拟或数字形式显示时间。
> 更多信息：<https://manned.org/xclock>。

- 显示模拟时钟：

`xclock`

- 显示只有时和分的24小时数字时钟：

`xclock -digital -brief`

- 使用 strftime 格式字符串显示数字时钟（参见 strftime(3)）：

`xclock -digital -strftime {{format}}`

- 显示每秒更新一次的24小时数字时钟，包括时、分、秒：

`xclock -digital -strftime '%H:%M:%S' -update 1`

- 显示只有时和分的12小时数字时钟：

`xclock -digital -twelve -brief`