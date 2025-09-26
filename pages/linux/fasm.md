# fasm

> Flat Assembler — fast and lightweight assembler for x86 architecture.
> Generates ELF executables or flat binaries from assembly source code.
> More information: <https://flatassembler.net>.

- Assemble an x86 or x86-64 assembly file into a binary (default output is `a.out` or specified name):

`fasm {{path/to/source.asm}}`

- Assemble and specify the output file name:

`fasm {{path/to/source.asm}} {{path/to/output}}`

- Assemble a 64-bit ELF Linux executable:

`fasm {{hello.asm}}`

- Show FASM version:

`fasm -v`

- Display help:

`fasm`
