# icalBuddy

> 用于从 macOS 日历数据库打印事件和任务的命令行工具。
> 更多信息：<https://hasseg.org/icalBuddy/>。

- 显示今天晚些时候的事件：

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- 显示未完成的任务：

`icalBuddy uncompletedTasks`

- 显示今天所有事件的按日历分隔的格式化列表：

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- 显示指定天数内的任务：

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+{{number_of_days}}"`

- 显示时间范围内的事件：

`icalBuddy eventsFrom:{{start_date}} to:{{end_date}}`