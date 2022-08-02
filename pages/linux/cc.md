# cc

> Alias for gcc, preprocess and compile C and C++ source files, then assemble and link them together.
> More information: <https://gcc.gnu.org>.

- Compile multiple source files into executable:

`cc {{path/to/source1.c path/to/source2.c ...}} --output {{path/to/output_executable}}`

- Allow warnings, debug symbols in output:

`cc {{path/to/source.c}} -Wall -Og --output {{path/to/output_executable}}`

- Include libraries from a different path:

`cc {{path/to/source.c}} --output {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- Compile source code into Assembler instructions:

`cc -S {{path/to/source.c}}`

- Compile source code without linking:

`cc -c {{path/to/source.c}}`
