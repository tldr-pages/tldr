# mpicc

> Open MPI C wrapper compiler.
> The wrappers are simply thin shells on top of a C compiler, they add the relevant compiler and linker flags to the command line that are necessary to compile/link Open MPI programs, and then invoke the underlying C compiler to actually perform the command.
> More information: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- Compile a source code file into an object file:

`mpicc -c {{path/to/file.c}}`

- Link an object file and make an executable:

`mpicc -o {{executable}} {{path/to/object_file.o}}`

- Compile and link source code in a single command:

`mpicc -o {{executable}} {{path/to/file.c}}`
