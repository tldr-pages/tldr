# cal

> Display a calendar with the current day highlighted.
> More information: <https://man.openbsd.org/cal>.

- Display a calendar for the current month:

`cal`

- Display a calendar for a specific year:

`cal {{year}}`

- Display a calendar for a specific month and year:

`cal {{month}} {{year}}`

- Display a calendar for the current [y]ear:

`cal -y`

- Display [j]ulian days (starting from one, numbered from January 1):

`cal -j`

- Use [m]onday as week start instead of Sunday:

`cal -m`

- Number [w]eek numbers (incompatible with `-j`):

`cal -w`
