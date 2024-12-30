# xclock

> 以模拟或数字形式显示时间。
> 更多信息：<https://manned.org/xclock>。

- 显示一个模拟时钟：

`xclock`

- 显示一个仅包含小时和分钟字段的24小时数字时钟：

`xclock -digital -brief`

- 使用strftime格式字符串显示数字时钟（参见strftime(3)）：

`xclock -digital -strftime {{format}}`

- 显示一个每秒更新的24小时数字时钟，包含小时、分钟和秒字段：

`xclock -digital -strftime '%H:%M:%S' -update 1`

- 显示一个仅包含小时和分钟字段的12小时数字时钟：

`xclock -digital -twelve -brief`