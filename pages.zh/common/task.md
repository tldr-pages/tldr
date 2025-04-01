# task

> 命令行待办事项管理器。
> 更多信息：<https://taskwarrior.org/docs/>.

- 添加一个新任务，该任务的截止日期为明天：

`task add {{description}} due:{{tomorrow}}`

- 更新任务的优先级：

`task {{task_id}} modify priority:{{H|M|L}}`

- 完成一个任务：

`task {{task_id}} done`

- 删除一个任务：

`task {{task_id}} delete`

- 列出所有未完成的任务：

`task list`

- 列出在本周结束前到期的未完成任务：

`task list due.before:{{eow}}`

- 显示每日图形燃尽图：

`task burndown.daily`

- 列出所有报告：

`task reports`
