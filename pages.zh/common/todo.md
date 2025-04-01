# todo

> 一个简单、基于标准的命令行待办事项管理器。
> 更多信息：<https://todoman.readthedocs.io>。

- 列出可开始的任务：

`todo list --startable`

- 向工作列表中添加新任务：

`todo new {{thing_to_do}} --list {{work}}`

- 为指定 ID 的任务添加位置信息：

`todo edit --location {{location_name}} {{task_id}}`

- 显示任务的详细信息：

`todo show {{task_id}}`

- 将指定 ID 的任务标记为已完成：

`todo done {{task_id1 task_id2 ...}}`

- 删除任务：

`todo delete {{task_id}}`

- 删除已完成的任务并重置剩余任务的 ID：

`todo flush`