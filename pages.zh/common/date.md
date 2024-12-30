# 日期

> 设置或显示系统日期。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>。

- 使用默认区域格式显示当前日期：

`date +%c`

- 以UTC格式显示当前日期，使用ISO 8601格式：

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- 以Unix时间戳形式显示当前日期（自Unix纪元以来的秒数）：

`date +%s`

- 将指定为Unix时间戳的日期转换为默认格式：

`date -d @{{1473305798}}`

- 将给定的日期转换为Unix时间戳格式：

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- 使用RFC-3339格式（`YYYY-MM-DD hh:mm:ss TZ`）显示当前日期：

`date --rfc-3339 s`

- 使用格式`MMDDhhmmYYYY.ss`设置当前日期（`YYYY`和`.ss`是可选的）：

`date {{093023592021.59}}`

- 显示当前ISO周数：

`date +%V`