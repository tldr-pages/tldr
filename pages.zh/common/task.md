# 任务

> 命令行待办事项管理器。
> 更多信息：<https://taskwarrior.org/docs/>.

- 添加一个明天到期的新任务：

`task add {{描述}} due:{{明天}}`

- 更新任务的优先级：

`task {{任务ID}} modify priority:{{高|中|低}}`

- 完成一个任务：

`task {{任务ID}} done`

- 删除一个任务：

`task {{任务ID}} delete`

- 列出所有未完成的任务：

`task list`

- 列出本周末之前到期的未完成任务：

`task list due.before:{{周末结束}}`

- 按天显示图形化的燃尽图：

`task burndown.daily`

- 列出所有报告：

`task reports`