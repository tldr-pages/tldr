# inkmake

> GNU Makefile-style SVG exporting using Inkscape's backend.
> More information: <https://github.com/wader/inkmake#usage>.

- Export an SVG file executing the specified Inkfile:

`inkmake {{path/to/Inkfile}}`

- Execute an Inkfile and show detailed information:

`inkmake {{[-v|--verbose]}} {{path/to/Inkfile}}`

- Execute an Inkfile, specifying SVG input file(s) and an output file:

`inkmake {{[-s|--svg]}} {{path/to/file.svg}} {{[-o|--out]}} {{path/to/output_image}} {{path/to/Inkfile}}`

- Use a custom Inkscape binary as the backend:

`inkmake {{[-i|--inkscape]}} {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{path/to/Inkfile}}`

- Display help:

`inkmake {{[-h|--help]}}`
