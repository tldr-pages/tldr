# ldc

> D compiler using LLVM as a backend.
> More information: <https://wiki.dlang.org/Using_LDC>.

- Compile a source code file into an executable binary:

`ldc2 {{path/to/source.d}} -of={{path/to/output_executable}}`

- Compile the source code file without linking:

`ldc2 -c {{path/to/source.d}}`

- Select the target architecture and OS:

`ldc -mtriple={{architecture_OS}} -c {{path/to/source.d}}`

- Display help:

`ldc2 -h`

- Display complete help:

`ldc2 -help-hidden`
