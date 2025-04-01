# topydo

> 一个使用 todo.txt 格式的待办事项应用程序。
> 更多信息：<https://github.com/topydo/topydo>.

- 向特定项目添加待办事项，同时指定上下文：

`topydo add "{{todo_message}} +{{project_name}} @{{context_name}}"`

- 添加一个优先级为 `A` 的待办事项，截止日期为明天：

`topydo add "(A) {{todo_message}} due:{{1d}}"`

- 添加一个截止日期为周五的待办事项：

`topydo add "{{todo_message}} due:{{fri}}"`

- 添加一个非严格重复的待办事项（下次截止日期 = 现在 + 周期）：

`topydo add "浇花 due:{{mon}} rec:{{1w}}"`

- 添加一个严格重复的待办事项（下次截止日期 = 当前截止日期 + 周期）：

`topydo add "{{todo_message}} due:{{2020-01-01}} rec:{{+1m}}"`

- 撤销上一次执行的 `topydo` 命令：

`topydo revert`