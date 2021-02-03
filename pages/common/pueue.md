# pueue

> Pueue is a command-line task management tool for sequential and parallel execution of long-running tasks.
> More information: <https://github.com/Nukesor/pueue>.

- Add a command to the task list:

`pueue add -- {{tr -u a-z A-Z}}`

- List tasks in the task list:

`pueue status`

- Send data to a task's stdin:

`pueue send {{task_id}} {{"hello"}}`

- View a task's stdout and stderr, as well as basic information about that task:

`pueue log {{task_id}}`

- Create a task group:

`pueue group --add {{group_name}}`

- Kill a task:

`pueue kill {{task_id}}`

- Set maximum amount of parallel tasks (queued tasked are started as needed to meet this limit):

`pueue parallel {{number_of_parallel_tasks}}`

- Edit the command line of a stopped tasked, in the default editor (as specified by `$EDITOR`):

`pueue edit {{task_id}}`
