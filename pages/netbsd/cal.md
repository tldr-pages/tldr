# cal

> Display a calendar.
> More information: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Display a calendar for the current month:

`cal`

- Display a calendar for a specific year:

`cal {{year}}`

- Display a calendar for a specific month and year:

`cal {{month}} {{year}}`

- Display the whole calendar for the current year using [j]ulian days (one-based, numbered from January 1):

`cal -y -j`

- [h]ighlight today and display [3] months spanning the date:

`cal -h -3 {{month}} {{year}}`

- Display the 2 months [B]efore and 3 [A]fter a specific [m]onth of the current year:

`cal -A 3 -B 2 {{month}}`

- Display a specific number of months before and after ([C]ontext) the specified month:

`cal -C {{months}} {{month}}`

- Specify the starting [d]ay of the week (0: Sunday, 1: Monday, ..., 6: Saturday):

`cal -d {{0..6}}`
