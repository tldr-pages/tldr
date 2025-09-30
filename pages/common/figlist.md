# figlist

> List the figlet fonts and control files.
> See also: `figlet`, `showfigfonts`, `chkfont`.
> More information: <https://manned.org/figlist>.

- List all available fonts using the default font directory:

`figlist`

- List fonts from a custom directory:

`figlist -d {{path/to/directory}}`

- Search for a font by keyword:

`figlist -d {{path/to/directory}} | grep {{keyword}}`

- Count the total number of available fonts in a specified directory:

`figlist -d {{path/to/directory}} | wc {{[-l|--lines]}}`
