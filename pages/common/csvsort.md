# csvsort

> Sorts CSV files.
> Included in csvkit.
> More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>.

- Sort a CSV file by column 9:

`csvsort -c {{9}} {{data.csv}}`

- Sort a CSV file by the "name" column in descending order:

`csvsort -r -c {{name}} {{data.csv}}`

- Sort a CSV file by column 2, then by column 4:

`csvsort -c {{2,4}} {{data.csv}}`

- Sort a CSV file without inferring data types:

`csvsort --no-inference -c {{columns}} {{data.csv}}`
