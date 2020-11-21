# lpr

> CUPS tool for printing files.
> See also `lpstat` and `lpadmin` for listing and configuring printers.
> More information: <http://www.CUPS.org>.

- Print a file to the default printer:

`lpr {{path/to/file}}`

- Print 2 copies:

`lpr -# {{2}} {{path/to/file}}`

- Print to a named printer:

`lpr -P {{printer}} {{path/to/file}}`

- Print either a single page (e.g. 2) or a range of pages (e.g. 2–16):

`lpr -o page-ranges={{2|2-16}} {{path/to/file}}`

- Print double sided either in portrait (long) or in landscape (short):

`lpr -o sides={{two_sided_long_edge|two_sided_short_edge}} {{path/to/file}}`

- Set page size (more options may be available depending on setup):

`lpr -o media={{a4|letter|legal}} {{path/to/file}}`

- Print multiple pages per sheet:

`lpr -o number-up={{2|4|6|9|16}} {{path/to/file}}`
