# rc-status

> Show status info about runlevels.
> See also `openrc`.
> More information: <https://manned.org/rc-status>.

- Show a summary of services and their status:

`rc-status`

- Include services in all runlevels in the summary:

`rc-status {{[-a|--all]}}`

- List services that have crashed:

`rc-status {{[-c|--crashed]}}`

- List manually started services:

`rc-status {{[-m|--manual]}}`

- List supervised services:

`rc-status {{[-S|--supervised]}}`

- Display the current runlevel:

`rc-status {{[-r|--runlevel]}}`

- List all runlevels:

`rc-status {{[-l|--list]}}`
