# task

> Manage your TODO list from the command line.
> More information: <https://taskwarrior.org/docs/>.

- Add a new task:

`task add {{description}} due:{{tomorrow}}`

- Modify a task:

`task {{task_id}} modify priority:{{H|M|L}}`

- Mark a task as completed:

`task {{task_id}} done`

- Delete a task:

`task {{task_id}} delete`

- List all open tasks:

`task list`

- List open tasks due before the end of the week:

`task list due.before:{{eow}}`

- Show a graphical burndown chart, by day:

`task burndown.daily`

- List all reports:

`task reports`
