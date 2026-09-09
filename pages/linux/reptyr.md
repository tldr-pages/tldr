# reptyr

> Move a running process to a new terminal.
> Best used when you forget to start a long running task in `screen`.
> More information: <https://github.com/nelhage/reptyr#usage>.

- Move a running process to your current terminal:

`reptyr {{process_id}}`

- Attach to a process using its name:

`reptyr $(pidof {{htop}})`
