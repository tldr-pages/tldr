# csvlook

> Render a CSV file in the console as a fixed-width table.
> Included in csvkit.

- View a CSV file:

`csvlook {{data.csv}}`

- View a CSV file with _less_ for easy scrolling:

`csvlook {{data.csv}} | less`

- View columns 2 and 3 of a CSV file:

`csvcut -c {{2,3}} | csvlook`
