# opt

> A tool that takes LLVM source files and runs specified optimizations and/or analyses on them.
> More information: <https://llvm.org/docs/CommandGuide/opt.html>.

- Run an optimization or analysis on a bitcode file:

`opt -{{passname}} {{path/to/file.bc}} -S -o {{file_opt.bc}}`

- Output the Control Flow Graph of a function to a `.dot` file:

`opt {{-dot-cfg}} -S {{path/to/file.bc}} -disable-output`

- Optimize the program at level 2 and output the result to another file:

`opt -O2 {{path/to/file.bc}} -S -o {{path/to/output_file.bc}}`
