# procs

> Display information about the active processes.
> More information: <https://github.com/dalance/procs>.

- List all processes showing the PID, user, CPU usage, memory usage, and the command which started them:

`procs`

- List information about processes, if the commands which started them contain `zsh`:

`procs {{zsh}}`

- List information about all processes sorted by CPU time in [a]scending or [d]escending order:

`procs {{--sorta|--sortd}} cpu`

- List information about processes with either a PID, command, or user containing `41` or `firefox`:

`procs --or {{PID|command|user}} {{41}} {{firefox}}`

- List information about processes with both PID `41` and a command or user containing `zsh`:

`procs --and {{41}} {{zsh}}`
