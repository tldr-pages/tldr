# topydo

> A todo list application that uses the todo.txt format.
> More information: <https://github.com/topydo/topydo>.

- Add a todo to a specific project with a given context:

`topydo add "{{todo_message}} +{{project_name}} @{{context_name}}"`

- Add todo which should be done till tomorow with a "A" priority:

`topydo add "(A) call mom due:1d"`

- Add a todo with a due date of friday:

`topydo add "{{todo_message}} due:{{fri}}"`

- Add non-strict repeating todo (next due = now + rec):

`topydo add "water flowers due:mon rec:1w"`

- Add strict repeating todo (next due = currentdue + rec):

`topydo add "pay rent due:2020-01-01 rec:+1m"`

- Undo last topydo command:

`topydo revert`
