# todo

> 一个简单的、基于标准的命令行待办事项管理器。
> 更多信息：<https://todoman.readthedocs.io>。

- 列出可启动的任务：

`todo list --startable`

- 向工作列表添加新任务：

`todo new {{待办事项}} --list {{工作}}`

- 为具有给定 ID 的任务添加位置：

`todo edit --location {{位置名称}} {{任务 ID}}`

- 显示有关任务的详细信息：

`todo show {{任务 ID}}`

- 将指定 ID 的任务标记为已完成：

`todo done {{任务 ID1 任务 ID2 ...}}`

- 删除任务：

`todo delete {{任务 ID}}`

- 删除已完成的任务并重置剩余任务的 ID：

`todo flush`