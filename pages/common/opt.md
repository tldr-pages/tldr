# opt

> LLVM .bc -> .bc modular optimizer and analysis printer. `opt` takes LLVM source files as input, runs the specified optimizations or analyses on it, and then outputs the optimized file or the analysis results.

- Run an optimization or analysis on a bitcode file:

`opt {{-passname}} {{path/to/file.bc}} -S -o {{file_opt.bc}}`

- Output the Control Flow Graph of a function to a "dot" file:

`opt {{-dot-cfg}} -S {{path/to/file.bc}} -disable-output`

- Optimize the program at level 2 and output the result to another file:

`opt -O2 {{path/to/file.bc}} -S -o {{file_opt.bc}}`
