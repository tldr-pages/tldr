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

`objdump {{[-d|--disassemble]}} {{path/to/binary}} {{[-M|--disassembler-options]}} intel`

- Display the disassembled executable sections with jump visualizations and syntax highlighting:

`objdump {{[-d|--disassemble]}} {{path/to/binary}} --visualize-jumps={{color|extended-color}} --disassembler-color={{color|extended-color}}`

- Display the symbol table:

`objdump {{[-t|--syms]}} {{path/to/binary}}`

- Display a complete binary hex dump of all sections:

`objdump {{[-s|--full-contents]}} {{path/to/binary}}`
