# mpicc

> Open MPI C wrapper compiler.
> The wrappers are simply thin shells on top of a C compiler, they add the relevant compiler and linker flags to the command line that are necessary to compile/link Open MPI programs, and then invoke the underlying C compiler to actually perform the command.

- To compile a single file, write:

`mpicc -c foo.c`

- To link the output and make an executable write:

`mpicc -o foo foo.o`

- To combine compilation and linking, write:

`mpicc -o foo foo.c`
