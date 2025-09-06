# todoist

> Access <https://todoist.com> from the command-line.
> More information: <https://github.com/sachaos/todoist>.

- Add a task:

`todoist add "{{task_name}}"`

- Add a high priority task with a label, project, and due date:

`todoist add "{{task_name}}" --priority {{1}} --label-ids "{{label_id}}" --project-name "{{project_name}}" --date "{{tmr 9am}}"`

- Add a high priority task with a label, project, and due date in quick mode:

`todoist quick '#{{project_name}} "{{tmr 9am}}" p{{1}} {{task_name}} @{{label_name}}'`

- List all tasks with a header and color:

`todoist --header --color list`

- List all high priority tasks:

`todoist list --filter p{{1}}`

- List today's tasks with high priority that have the specified label:

`todoist list --filter '(@{{label_name}} | {{today}}) & p{{1}}'`
