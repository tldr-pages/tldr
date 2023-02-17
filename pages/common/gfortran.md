# gfortran

> Preprocess and compile Fortran source files, then assemble and link them together.
> More information: <https://gcc.gnu.org/wiki/GFortran>.

- Compile multiple source files into an executable:

`gfortran {{path/to/source1.f90 path/to/source2.f90 ...}} -o {{path/to/output_executable}}`

- Show common warnings, debug symbols in output, and optimize without affecting debugging:

`gfortran {{path/to/source.f90}} -Wall -g -Og -o {{path/to/output_executable}}`

- Include libraries from a different path:

`gfortran {{path/to/source.f90}} -o {{path/to/output_executable}} -I{{path/to/mod_and_include}} -L{{path/to/library}} -l{{library_name}}`

- Compile source code into Assembler instructions:

`gfortran -S {{path/to/source.f90}}`

- Compile source code into an object file without linking:

`gfortran -c {{path/to/source.f90}}`
