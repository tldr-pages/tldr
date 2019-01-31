# stdbuf

> Run a command with modified input/output stream buffering.

- Run a command with unbuffered standard output:

`stdbuf --output {{0}} {{command}}`

- Run a command with line buffered standard output:

`stdbuf --output {{L}} {{command}}`

- Run a command setting the buffer size of its standard input to {{2MB}}:

`stdbuf --input {{2MB}} {{command}}`

- Run a command with all three standard input/output streams in unbuffered mode:

`stdbuf --input {{0}} --output {{0}} --error {{0}} {{command}}`
