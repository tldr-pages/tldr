# kill

> Sends a signal to a process
> Mostly used for stopping processes

- kill the process

`kill {{process_id}}`

- list signal names

`kill -l`

- read configure file,reload

`kill [-1][-SIGHUP] {{process_id}}`

- [ctrl]-c

`kill [-2][-SIGINT] {{process_id}}`

- forced to interrupt a program

`kill [-9][-SIGKILL] {{process_id}}`

- normal interrupt a program

`kill [-15][-SIGTERM] {{process_id}}`

- [ctrl]-z

`kill [-17][-SIGSTOP] {{process_id}}`
