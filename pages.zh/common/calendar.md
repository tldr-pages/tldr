# 日历

> 从日历文件中显示即将发生的事件。
> 更多信息：<https://manned.org/calendar>。

- 显示今天和明天（或周五的周末）来自默认日历的事件：

`calendar`

- 向前查看，显示接下来的30天的事件：

`calendar -A {{30}}`

- 向后查看，显示之前7天的事件：

`calendar -B {{7}}`

- 从自定义日历[f]文件中显示事件：

`calendar -f {{path/to/file}}`