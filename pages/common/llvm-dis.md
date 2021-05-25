# llvm-dis

> Converts LLVM bitcode files into human-readable LLVM Intermediate Representation (IR).
> More information: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- Output a bitcode file as LLVM IR to standard output:

`llvm-dis {{path/to/input.bc}} -o -`

- Convert a bitcode file to LLVM IR with the same filename:

`llvm-dis {{path/to/file.bc}}`

- Convert a bitcode file to LLVM IR:

`llvm-dis {{path/to/input.bc}} -o {{path/to/output.ll}}`
