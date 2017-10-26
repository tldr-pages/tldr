# write

> Write a message on the terminal of a specified logged in user (ctrl-C to stop writing messages).
> To find out all terminal_ids of all users active on the system see the 'who' command.

- Send a message to user {{username}} on terminal {{terminal_id}}:

`write {{username}} {{terminal_id}}`

- Send message to user 'testuser' on terminal /dev/tty/5:

`write {{testuser}} {{tty/5}}`

- Send message to user 'jhondoe' on pseudo terminal /dev/pts/5:

`write {{jhondoe}} {{pts/5}}`
