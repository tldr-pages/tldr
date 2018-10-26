# opt

> LLVM .bc -> .bc modular optimizer and analysis printer.

- Run an optimization or an analysis in a bitcode file:

`opt {{-passname}} {{file.bc}} -S -o {{file_opt.bc}}`

- Print the Control Flow Graph of a function to a "dot" file:

`opt {{-dot-cfg}} -S {{file.bc}} -disable-output`

- Optimize the program with "-O2" and write its output to another file:

`opt -O2 {{file.bc}} -S -o {{file_opt.bc}}`
