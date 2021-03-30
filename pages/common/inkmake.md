# inkmake

> Use inkfiles to export SVG files using Inkscape's backend.
> More information: <https://github.com/wader/inkmake>.

- Display help:

`./inkmake -h`

- Export an SVG file executing the specified Inkfile:

`./inkmake {{inkfile}}`

- Execute an inkfile and show detailed information:

`./inkmake -v {{inkfile}}`

- Execute an inkfile by specifying SVG file(s) and output file:

`./inkmake -s {{path/to/svg}} -o {{path/to/output}} {{inkfile}}`

- Specify the path of the Inkscape binary:

`./inkmake -i {{path/to/inkscape}} {{inkfile}}`
