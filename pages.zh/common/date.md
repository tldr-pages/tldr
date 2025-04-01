# date

> 设置或显示系统日期。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>.

- 使用默认区域设置的格式显示当前日期：

`date +%c`

- 使用 ISO 8601 格式显示当前日期（UTC）：

`date {{[-u|--utc]}} +%Y-%m-%dT%H:%M:%S%Z`

- 以 Unix 时间戳格式（自 Unix 纪元以来的秒数）显示当前日期：

`date +%s`

- 将指定的 Unix 时间戳转换为默认格式：

`date {{[-d|--date]}} @{{1473305798}}`

- 将给定的日期转换为 Unix 时间戳格式：

`date {{[-d|--date]}} "{{2018-09-01 00:00}}" +%s {{[-u|--utc]}}`

- 使用 RFC-3339 格式（`YYYY-MM-DD hh:mm:ss TZ`）显示当前日期：

`date --rfc-3339 s`

- 使用格式 `MMDDhhmmYYYY.ss`（`YYYY` 和 `.ss` 是可选的）设置当前日期：

`date {{093023592021.59}}`

- 显示当前的 ISO 周数：

`date +%V`
