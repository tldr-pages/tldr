# csvtool

> Utility to filter and extract data from CSV formatted sources.
> More information: <https://github.com/maroofi/csvtool>.

- Extract the second column from a CSV file:

`csvtool {{[-c|--column]}} {{2}} {{path/to/file.csv}}`

- Extract the second and fourth columns from a CSV file:

`csvtool {{[-c|--column]}} {{2,4}} {{path/to/file.csv}}`

- Extract lines from a CSV file where the second column exactly matches `Foo`:

`csvtool {{[-c|--column]}} {{2}} {{[-s|--search]}} '{{^Foo$}}' {{path/to/file.csv}}`

- Extract lines from a CSV file where the second column starts with `Bar`:

`csvtool {{[-c|--column]}} {{2}} {{[-s|--search]}} '{{^Bar}}' {{path/to/file.csv}}`

- Find lines in a CSV file where the second column ends with `Baz` and then extract the third and sixth columns:

`csvtool {{[-c|--column]}} {{2}} {{[-s|--search]}} '{{Baz$}}' {{path/to/file.csv}} | csvtool {{[-e|--no-header]}} {{[-c|--column]}} {{3,6}}`
