# inkmake

> Exports from SVG files using Inkscape's backend.
> More information: <https://rubygems.org/gems/inkmake>.

- Display help:

`./inkmake -h`

- Execute an inkfile to export:

`./inkmake {{inkfile}}`

- Execute an inkfile with detailed info:

`./inkmake -v {{inkfile}}`

- Execute by specifying svg file(s) and output:

`./inkmake -s {{path/to/svg}} -o {{path/to/output}} {{inkfile}}`

- Specify the path of the Inkscape binary:

`./inkmake -i {{path/to/inkscape}} {{inkfile}}`
