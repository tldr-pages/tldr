# timetrap

> 简单的命令行时间记录工具，使用 Ruby 编写。
> 更多信息：<https://github.com/samg/timetrap>.

- 创建新的时间表：

`timetrap sheet {{timesheet}}`

- 从5分钟前开始记录一个条目：

`timetrap in --at "{{5 minutes ago}}" {{entry_notes}}`

- 显示当前的时间表：

`timetrap display`

- 编辑最后一条记录的结束时间：

`timetrap edit --end {{time}}`
