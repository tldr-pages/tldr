# llvm-as

> LLVM Intermediate Representation (`.ll`) to Bitcode (`.bc`) assembler.
> More information: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- Assemble an IR file:

`llvm-as -o {{out.bc}} {{source.ll}}`

- Assemble an IR file and include a module hash in the produced Bitcode file:

`llvm-as --module-hash -o {{out.bc}} {{source.ll}}`

- Read IR from `stdin` and assemble it:

`llvm-as -o {{out.bc}}`

- Assemble an IR file to `stdout` (might mess up your terminal):

`llvm-as -f -o - {{source.ll}}`
