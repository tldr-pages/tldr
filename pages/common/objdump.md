# objdump

> View information about object files.
> More information: <https://manned.org/objdump>.

- Display the file header information:

`objdump -f {{binary}}`

- Display the disassembled output of executable sections:

`objdump -d {{binary}}`

- Display the disassembled executable sections in intel syntax:

`objdump -M intel -d {{binary}}`

- Display a complete binary hex dump of all sections:

`objdump -s {{binary}}`
