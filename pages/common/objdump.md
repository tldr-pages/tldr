# objdump

> View information about object files.
> More information: <https://manned.org/objdump>.

- Display the file header information:

`objdump -f {{path/to/binary}}`

- Display all header information:

`objdump -x {{path/to/binary}}`

- Display the disassembled output of executable sections:

`objdump -d {{path/to/binary}}`

- Display the disassembled executable sections in Intel syntax:

`objdump -M intel -d {{path/to/binary}}`

- Display a complete binary hex dump of all sections:

`objdump -s {{path/to/binary}}`
