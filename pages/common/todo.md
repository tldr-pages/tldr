# todo

> A simple task manager for the command line.
> More information: <https://todoman.readthedocs.io/en/stable/>.

- Print all outstanding tasks:

`todo list`

- Print all outstanding tasks from a given list that take place in a given location and order them by their start date:

`todo list --location {{location_name}} --sort {{start}} {{list_name}}`

- Add a new task which is due on a specific date to a given list:

`todo new --list {{list_name}} --due {{due_date}} {{task_description}}`

- Add a location to a task with a given ID:

`todo edit --location {{location_name}} {{task_id}}`

- Mark tasks with the specified IDs as done:

`todo done {{2}} {{3}}`

- Delete done tasks and reset the IDs of the remaining tasks:

`todo flush`
