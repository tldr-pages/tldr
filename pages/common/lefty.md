# lefty

> A programmable graphics editor for technical pictures.
> Note: This command is deprecated.
> More information: <https://graphviz.org/docs/cli/lefty/>.

- Open a Lefty program file:

`lefty {{path/to/file.lefty}}`

- Read a program from standard input:

`lefty -`

- Execute an expression:

`lefty -e '{{expression}}'`

- Exit after processing the input file:

`lefty -x {{path/to/file.lefty}}`

- Set the error reporting level (`0` through `5`):

`lefty -el {{level}} {{path/to/file.lefty}}`

- Display version information:

`lefty -v`

- Display usage information:

`lefty -?`
