# pkill

> Signal process by name
> Mostly used for stopping processes

- kill all processes which match

`pkill -9 {{process_name}}`

- send SIGUSR1 signal to processes which match

`pkill -USR1 {{process_name}}`
