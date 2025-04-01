# todoist

> 从命令行访问 <https://todoist.com>。
> 更多信息: <https://github.com/sachaos/todoist>.

- 添加任务:

`todoist add "{{task_name}}"`

- 添加高优先级任务，包含标签、项目和截止日期:

`todoist add "{{task_name}}" --priority {{1}} --label-ids "{{label_id}}" --project-name "{{project_name}}" --date "{{tmr 9am}}"`

- 以快速模式添加高优先级任务，包含标签、项目和截止日期:

`todoist quick '#{{project_name}} "{{tmr 9am}}" p{{1}} {{task_name}} @{{label_name}}'`

- 列出所有任务，带有标题和颜色:

`todoist --header --color list`

- 列出所有高优先级任务:

`todoist list --filter p{{1}}`

- 列出今天具有高优先级并带有指定标签的任务:

`todoist list --filter '(@{{label_name}} | {{today}}) & p{{1}}'`
