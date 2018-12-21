# pkill

> Signal process by name.
> Mostly used for stopping processes.

- Kill all processes which match:

`pkill -9 {{process_name}}`

- Kill all processes which match their full command instead of just the process name:

`pkill -9 -f "{{command_name}}"`

- Send SIGUSR1 signal to processes which match:

`pkill -USR1 {{process_name}}`
