# tb

> Manage tasks and notes across multiple boards.
> More information: <https://github.com/klaudiosinani/taskbook#usage>.

- Add a new task to a board:

`tb {{[-t|--task]}} {{task_description}} @{{board_name}}`

- Add a new note to a board:

`tb {{[-n|--note]}} {{note_description}} @{{board_name}}`

- Edit item's priority:

`tb {{[-p|--priority]}} @{{item_id}} {{priority}}`

- Check/uncheck item:

`tb {{[-c|--check]}} {{item_id}}`

- Archive all checked items:

`tb --clear`

- Move item to a board:

`tb {{[-m|--move]}} @{{item_id}} {{board_name}}`
