# procs

> Display information about the active processes.
> More information: <https://github.com/dalance/procs>.

- List all processes showing the PID, user, CPU usage, memory usage, and the command which started them:

`procs`

- List information about processes, if the commands which started them contain `zsh`:

`procs {{zsh}}`

- List information about all processes sorted by CPU time in ascending or descending order:

`procs {{--sortd|--sorta}} cpu`

- List information about processes with either a PID, command, or user containing (`zsh` or `firefox`):

`procs --or {{PID|command|user}} {{41}} {{firefox}}`

- List information about processes with both PID `41` and a command or user containing `zsh`:

`procs --and {{41}} {{zsh}}`
