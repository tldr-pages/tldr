# timew

> 一个用于测量活动持续时间的时间跟踪工具。
> 更多信息：<https://timewarrior.net/docs>.

- 开始跟踪一个活动：

`timew start`

- 为当前活动添加标签：

`timew tag {{activity_tag}}`

- 开始跟踪并标记一个新的活动：

`timew start {{activity_tag}}`

- 停止当前活动：

`timew stop`

- 跟踪过去的活动：

`timew track {{start_time}} - {{end_time}} {{activity_tag}}`

- 查看当天的跟踪记录：

`timew summary`

- 查看最后一日、周、当前月等的报告：

`timew summary :{{today|yesterday|week|lastweek|month|lastmonth|year|lastyear}}`
