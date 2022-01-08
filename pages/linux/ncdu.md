# ncdu

> Disk usage analyzer with an ncurses interface.
> More information: <https://manned.org/ncdu>.

- Analyze the current working directory:

`ncdu`

- Colorize output (available colors `off`, `dark`):

`ncdu --color {{dark}}`

- Analyze a given directory:

`ncdu {{path/to/directory}}`

- Save results to a file:

`ncdu -o {{path/to/file}}`

- Exclude files that match a pattern, argument can be given multiple times to add more patterns:

`ncdu --exclude '{{*.txt}}'`
