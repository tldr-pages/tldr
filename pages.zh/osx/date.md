# date

> 设置或显示系统日期。
> 更多信息：<https://keith.github.io/xcode-man-pages/date.1.html>.

- 使用默认区域设置的格式显示当前日期：

`date +%c`

- 以 UTC 和 ISO 8601 格式显示当前日期：

`date -u +%Y-%m-%dT%H:%M:%SZ`

- 将当前日期显示为 unix 时间戳（自 1970-01-01 00:00:00 以来的秒数）：

`date +%s`

- 使用默认格式显示特定日期（格式化指定 UNIX 时间戳）：

`date -r {{1473305798}}`
