# tb

> CLI for managing tasks and notes across multiple boards.
> More information: <https://github.com/klaussinani/taskbook>.

- Add a new task to a board:

`tb --task {{task description}} @{{board_name}}`

- Add a new note to a board:

`tb --note {{note description}} @{{board_name}}`

- Edit item's priority:

`tb --priority @{{item_id}} {{priority}}`

- Check/uncheck item:

`tb --check {{item_id}}`

- Archive all checked items:

`tb --clear`

- Move item to a board:

`tb --move @{{item_id}} {{board_name}}`
