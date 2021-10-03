# llc

> Compiles LLVM Intermediate Representation or bitcode to target-specific assembly language.
> More information: <https://www.llvm.org/docs/CommandGuide/llc.html>.

- Compile a bitcode or IR file to an assembly file with the same base name:

`llc {{path/to/file.ll}}`

- Optimize at level 2 and output assembly to a specific file:

`llc -O2 {{path/to/input.ll}} --output {{path/to/output.s}}`

- Emit fully relocateable, position independent code:

`llc -relocation-model=pic {{path/to/input.ll}}`
