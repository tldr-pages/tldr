# date

> 设置或显示系统日期。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>。

- 使用默认区域设置格式显示当前日期：

`date +%c`

- 以 UTC 时区和 ISO 8601 格式显示当前日期：

`date {{[-u|--utc]}} +%Y-%m-%dT%H:%M:%S%Z`

- 以 Unix 时间戳（自 Unix 纪元以来的秒数）显示当前日期：

`date +%s`

- 将 Unix 时间戳转换为默认格式的日期：

`date {{[-d|--date]}} @{{1473305798}}`

- 将指定日期转换为 Unix 时间戳格式：

`date {{[-d|--date]}} "{{2018-09-01 00:00}}" +%s {{[-u|--utc]}}`

- 以 RFC-3339 格式（`YYYY-MM-DD hh:mm:ss TZ`）显示当前日期并指定精度：

`date --rfc-3339 {{date|seconds|ns}}`

- 使用 `MMDDhhmmYYYY.ss` 格式设置当前日期（`YYYY` 和 `.ss` 为可选）：

`sudo date {{093023592021.59}}`

- 显示当前的 ISO 周数：

`date +%V`
