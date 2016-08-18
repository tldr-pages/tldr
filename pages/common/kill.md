# kill

> Sends a signal to a process.
> Mostly used for stopping processes.

- Kill the process:

`kill {{process_id}}`

- List signal names:

`kill -l`

- read configure file,reload

`kill [-1][-SIGHUP] {{process_id}}`

- interrupt, program can handle SIGINT

`kill [-2][-SIGINT] {{process_id}}`

- forced to interrupt a program

`kill [-9][-SIGKILL] {{process_id}}`

- normal interrupt a program

`kill [-15][-SIGTERM] {{process_id}}`

- stop program 

`kill [-17][-SIGSTOP] {{process_id}}`
