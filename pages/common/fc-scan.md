# fc-scan

> Scan font files or directories and print pattern information for each face found.
> More information: <https://manned.org/fc-scan>.

- Scan a font file:

`fc-scan {{path/to/font_file}}`

- Scan a directory of fonts recursively:

`fc-scan {{path/to/directory}}`

- Scan multiple files or directories:

`fc-scan {{path/to/font1.ttf path/to/font2.otf ...}}`

- Print results without including font sizes:

`fc-scan {{[-b|--brief]}} {{path/to/font_file}}`

- Print results using a custom output format:

`fc-scan {{[-f|--format]}} "{{%{family}\n}}" {{path/to/font_file}}`

- Display help:

`fc-scan {{[-h|--help]}}`

- Display version:

`fc-scan {{[-V|--version]}}`
