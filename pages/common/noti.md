# noti

> Monitor a process and trigger a notification.

- Display a notification when tar finishes compressing files:

`noti {{tar -cjf example.tar.bz2 example/}}`

- Display a notification even when you put it after the command to watch:

`{{command_to_watch}}; noti`

- Monitor a process by PID and trigger a notification when the pid disappears:

`noti -w {{process_id}}`
