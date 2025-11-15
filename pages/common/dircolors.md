# dircolors

> Output commands to set the LS_COLOR environment variable and style `ls`, `dir`, etc.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- Output commands to set LS_COLOR using default colors:

`dircolors`

- Display each filetype with the color they would appear in `ls`:

`dircolors --print-ls-colors`

- Output commands to set LS_COLOR using colors from a file:

`dircolors {{path/to/file}}`

- Output commands for Bourne shell:

`dircolors {{[-b|--bourne-shell]}}`

- Output commands for C shell:

`dircolors {{[-c|--c-shell]}}`

- View the default colors for file types and extensions:

`dircolors {{[-p|--print-database]}}`
