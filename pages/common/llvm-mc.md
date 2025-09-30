# llvm-mc

> LLVM Machine Code Playground. It provides a set of tools for working with LLVM machine code.
> Part of LLVM.
> More information: <https://llvm.org/docs/CommandGuide/llvm-mc.html>.

- Assemble assembly code file into object file with machine code:

`llvm-mc --filetype=obj -o {{path/to/output.o}} {{path/to/input.s}}`

- Disassemble object file with machine code into assembly code file:

`llvm-mc --disassemble -o {{path/to/output.s}} {{path/to/input.o}}`

- Compile LLVM bit code file into assembly code:

`llvm-mc -o {{path/to/output.s}} {{path/to/input.bc}}`

- Assemble assembly code from standard input stream and show encoding to standard output stream:

`echo "{{addl %eax, %ebx}}" | llvm-mc -show-encoding -show-inst`

- Disassemble machine code from standard input stream for specified triple:

`echo "{{0xCD 0x21}}" | llvm-mc --disassemble -triple={{target_name}}`
