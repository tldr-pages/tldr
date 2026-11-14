# lefty

> A programmable graphics editor for technical pictures.
> Note: This command is deprecated.
> More information: <https://graphviz.org/docs/cli/lefty/>.

- Open a Lefty program file:

`lefty {{path/to/file.lefty}}`

- Read a program from `stdin`:

`lefty -`

- Execute an [e]xpression:

`lefty -e '{{expression}}'`

- E[x]it after processing the input file:

`lefty -x {{path/to/file.lefty}}`

- Set the [e]rror reporting [l]evel (`0` through `5`):

`lefty -el {{level}} {{path/to/file.lefty}}`

- Display version:

`lefty -v`

- Display help:

`lefty -?`
