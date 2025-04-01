# icalBuddy

> 用于打印 macOS 日历数据库中的事件和任务的命令行工具。
> 更多信息：<https://hasseg.org/icalBuddy/>.

- 显示今天晚些时候的事件：

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- 显示未完成的任务：

`icalBuddy uncompletedTasks`

- 以格式化列表的形式按日历分隔显示今天的所有事件：

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- 显示指定天数内的任务：

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+{{number_of_days}}"`

- 显示指定时间范围内的事件：

`icalBuddy eventsFrom:{{start_date}} to:{{end_date}}`
