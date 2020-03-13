# lpr

> CUPS tool for printing files.

- Print a file to the default printer:

`lpr {{path/to/file}}`

- Print a certain number of copies:

`lpr -# {{copies}} {{path/to/file}}`

- Print to a named printer:

`lpr -P {{printer}} {{path/to/file}}`

- Print double sided in portrait:

`lpr -o sides=two-sided-long-edge {{path/to/file}}`

- Print double sided in landscape:

`lpr -o sides=two-sided-short-edge {{path/to/file}}`

- Set page size (a4, letter, legal, etc):

`lpr -o media={{paper_type}} {{path/to/file}}`

- Print multiple pages per sheet (2, 4, 6, 9, or 16):

`lpr -o number-up={{pages_per_sheet}} {{path/to/file}}`
