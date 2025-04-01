# tb

> 管理多个看板中的任务和笔记。
> 更多信息：<https://github.com/klaussinani/taskbook>.

- 向看板添加新任务：

`tb --task {{task_description}} @{{board_name}}`

- 向看板添加新笔记：

`tb --note {{note_description}} @{{board_name}}`

- 编辑项目的优先级：

`tb --priority @{{item_id}} {{priority}}`

- 勾选/取消勾选项目：

`tb --check {{item_id}}`

- 归档所有已勾选的项目：

`tb --clear`

- 将项目移动到另一个看板：

`tb --move @{{item_id}} {{board_name}}`