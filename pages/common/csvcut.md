# csvcut

> Filter and truncate CSV files. Like Unix's `cut` command, but for tabular data.
> Included in csvkit.
> More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- Print indices and names of all columns:

`csvcut {{[-n|--names]}} {{data.csv}}`

- Extract the first and third columns:

`csvcut {{[-c|--columns]}} {{1,3}} {{data.csv}}`

- Extract all columns except the fourth one:

`csvcut {{[-C|--not-columns]}} {{4}} {{data.csv}}`

- Extract the columns named "id" and "first name" (in that order):

`csvcut {{[-c|--columns]}} {{id,"first name"}} {{data.csv}}`
