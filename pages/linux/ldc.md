# ldc

> LLVM front-end D compiler.
> More information: <https://wiki.dlang.org/Using_LDC>.

- Compile a source code file into an executable binary:

`ldc2 {{Source_file}}.d -of={{Output_Executable}}`

- Compile source without linking:

`ldc2 -c {{Source_file}}.d`

- Select the target architecture and OS:

`ldc -mtriple={{Architecture-OS}} -c {{Source_file}}.d`

- Get basic help instruction:

`ldc2 -h`

- Get complete help instruction:

`ldc2 -help-hidden`
