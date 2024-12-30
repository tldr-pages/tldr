# timetrap

> 用 Ruby 编写的简单命令行时间跟踪器。
> 更多信息: <https://github.com/samg/timetrap>。

- 创建一个新的时间表：

`timetrap sheet {{时间表}}`

- 签到一条在 5 分钟前开始的条目：

`timetrap in --at "{{5分钟前}}" {{条目备注}}`

- 显示当前时间表：

`timetrap display`

- 编辑最后一条条目的结束时间：

`timetrap edit --end {{时间}}`