# rc-status

> Show status info about runlevels.
> See also `openrc`.
> More information: <https://manned.org/rc-status>.

- Show a summary of services and their status:

`rc-status`

- Include services in all runlevels in the summary:

`rc-status --all`

- List services that have crashed:

`rc-status --crashed`

- List manually started services:

`rc-status --manual`

- List supervised services:

`rc-status --supervised`

- Get the current runlevel:

`rc-status --runlevel`

- List all runlevels:

`rc-status --list`
