# topydo

> 一款使用 todo.txt 格式的待办事项应用程序。
> 更多信息：<https://github.com/topydo/topydo>。

- 将待办事项添加到特定项目和给定上下文中：

`topydo add "{{todo_message}} +{{project_name}} @{{context_name}}"`

- 添加一个截止日期为明天、优先级为 `A` 的待办事项：

`topydo add "(A) {{todo_message}} due:{{1d}}"`

- 添加一个截止日期为星期五的待办事项：

`topydo add "{{todo_message}} due:{{fri}}"`

- 添加一个非严格重复的待办事项（下一个截止日期 = 现在 + 重复）：

`topydo add "浇花 due:{{mon}} rec:{{1w}}"`

- 添加一个严格重复的待办事项（下一个截止日期 = 当前截止日期 + 重复）：

`topydo add "{{todo_message}} due:{{2020-01-01}} rec:{{+1m}}"`

- 撤销上一个执行的 `topydo` 命令：

`topydo revert`