# rizin

> Reverse engineering framework and command-line toolset.
> Fork of radare2 with improved stability and features.
> More information: <https://rizin.re>.

- Open a binary for analysis:

`rizin {{path/to/binary}}`

- Open in write mode:

`rizin -w {{path/to/binary}}`

- Run a command on opening:

`rizin -c "{{command}}" {{path/to/binary}}`

- Analyze the binary automatically:

`rizin -A {{path/to/binary}}`

- Print disassembly of main function:

`rizin -c "{{aa; pdf @main}}" {{path/to/binary}}`

- List functions:

`rizin -c "{{afl}}" {{path/to/binary}}`

- Run rizin script:

`rizin -i {{script.rz}} {{path/to/binary}}`

- Dump binary info:

`rizin -c "{{iI}}" {{path/to/binary}}`
