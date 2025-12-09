# cal

> Display a calendar with the current day highlighted.
> More information: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Display a calendar for the current month:

`cal`

- Display a calendar for a specific year:

`cal {{year}}`

- Display a calendar for a specific month and year:

`cal {{month}} {{year}}`

- Display the whole calendar for the current year:

`cal -y`

- Don't [h]ighlight today and display [3] months spanning the date:

`cal -h -3 {{month}} {{year}}`

- Display the 2 months [B]efore and 3 [A]fter a specific [m]onth of the current year:

`cal -A 3 -B 2 {{month}}`

- Display [j]ulian days (starting from one, numbered from January 1):

`cal -j`
