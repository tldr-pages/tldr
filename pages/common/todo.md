# todo

> A simple task manager for the command line.
> More information: <https://todoman.readthedocs.io/en/stable/>.

- Print all outstanding tasks:

`todo list`

- Print all outstanding tasks from list {{work}} that take place in {{office}} and order them by their start date:

`todo list --location {{office}} --sort {{start}} {{work}}`

- Add a new task for cleaning the room to list {{private}} which is due on 23/12/2021:

`todo new --list {{private}} --due 23/12/2021 {{Clean the room}}`

- Add location {{office}} to task with ID {{42}}:

`todo edit --location {{office}} {{42}}`

- Mark tasks with ID {{2}} and {{3}} as done:

`todo done {{2}} {{3}}`

- Delete done tasks and reset the task ids:

`todo flush`
