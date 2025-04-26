# objdump

> View information about object files.
> More information: <https://manned.org/objdump>.

- Display the file header information:

`objdump {{[-f|--file-headers]}} {{path/to/binary}}`

- Display all header information:

`objdump {{[-x|--all-headers]}} {{path/to/binary}}`

- Display the disassembled output of executable sections:

`objdump {{[-d|--disassemble]}} {{path/to/binary}}`

- Display the disassembled executable sections in Intel syntax:

`objdump {{[-M|--disassembler-options]}} intel {{[-d|--disassemble]}} {{path/to/binary}}`

- Display a complete binary hex dump of all sections:

`objdump {{[-s|--full-contents]}} {{path/to/binary}}`
