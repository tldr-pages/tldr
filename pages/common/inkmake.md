# inkmake

> GNU Makefile-style SVG exporting using Inkscape's backend.
> More information: <https://github.com/wader/inkmake>.

- Display help:

`inkmake --help`

- Export an SVG file executing the specified Inkfile:

`./inkmake {{inkfile}}`

- Execute an Inkfile and show detailed information:

`./inkmake -v {{inkfile}}`

- Execute an Inkfile, specifying SVG input file(s) and an output file:

`./inkmake -s {{path/to/svg}} -o {{path/to/output}} {{inkfile}}`

- Specify a custom Inkscape binary to use as the backend:

`./inkmake -i {{path/to/inkscape}} {{inkfile}}`
