# cl

> The Microsoft C/C++ compiler for compiling and linking source code files.
> More information: <https://learn.microsoft.com/cpp/build/reference/compiler-command-line-syntax>.

- Compile a source file:

`cl {{path/to/source.c}}`

- Compile and create an executable with a custom name:

`cl /Fe {{path/to/output_executable}} {{path/to/source.c}}`

- Compile a source file with optimization enabled:

`cl /O2 {{path/to/source.c}}`

- Compile a source file and create a debug executable:

`cl /Zi {{path/to/source.c}}`

- Compile multiple source files:

`cl {{path/to/source1.c path/to/source2.c ...}}`

- Specify the output directory for compiled files:

`cl /Fo {{path/to/output_directory}}/ {{path/to/source.c}}`

- Compile with warnings as errors:

`cl /WX {{path/to/source.c}}`
