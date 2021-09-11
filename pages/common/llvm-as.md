# llvm-as

> LLVM Intermediate Representation (`.ll`) to Bitcode (`.bc`) assembler.
> More information: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- Assemble an IR file:

`llvm-as -o {{path/to/out.bc}} {{path/to/source.ll}}`

- Assemble an IR file and include a module hash in the produced Bitcode file:

`llvm-as --module-hash -o {{path/to/out.bc}} {{path/to/source.ll}}`

- Read IR from `stdin` and assemble it:

`llvm-as -o {{path/to/out.bc}}`

- Assemble an IR file to `stdout` (might mess up your terminal):

`llvm-as -f -o - {{path/to/source.ll}}`
