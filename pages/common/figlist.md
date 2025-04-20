# figlist

> Lists the figlet fonts and control files.
> See also: `figlet`, `showfigfonts`, `chkfont`.
> More information: <https://linux.die.net/man/6/figlist>.

- List all available fonts using the default font directory:

`figlist`

- List fonts from a custom directory:

`figlist -d {{path/to/custom_directory}}`

- Search for a font by keyword:

`figlist -d {{path/to/custom_directory}} | grep {{keyword}}`

- Count the total number of available fonts in a specified directory:

`figlist -d {{path/to/custom_directory}} | wc -l`
