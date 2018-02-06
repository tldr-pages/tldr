# rabin2

> Get information about binary files - symbols, sections, linked libraries, etc.
> Comes bundled with radare2

- Display general information about a binary (architecture, type, endianness):

`rabin2 -I {{path/to/binary}}`

- Display linked libraries:

`rabin2 -l {{path/to/binary}}`

- Display symbols imported from libraries:

`rabin2 -i {{path/to/binary}}`

- Display strings contained in the binary:

`rabin2 -z {{path/to/binary}}`

- Output in JSON (works for every subcommand):

`rabin2 -j -I {{path/to/binary}}`
