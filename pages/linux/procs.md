# procs

> procs displays information about the active processes.
> It can be a used as ps or top alternative
> More information: <https://github.com/dalance/procs>

- Show information about all the processes:

`procs`

- Show information about process with command or user containg `zsh`:

`procs {{zsh}}`

- Show information about all processes sorted in [d]escending order by `cpu` time:

`procs --sortd cpu`

- Show information about processes with pid `41` or (command or user) containing (`zsh` `or` `firefox`):

`procs --or {{zsh}} {{41}} {{firefox}}`

- Show information about processes with pid `41` and (command or user) containing `zsh`:

`procs --and {{41}} {{zsh}}`

