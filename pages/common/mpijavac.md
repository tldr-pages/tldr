# mpijavac

> Open MPI compiler wrapper for Java.
> See also: `mpirun`.
> More information: <https://docs.open-mpi.org/en/main/features/java.html#building-java-mpi-applications>.

- Compile a Java source file:

`mpijavac {{path/to/source_file.java}}`

- Pass application-specific classpaths to compiler:

`mpijavac -cp {{path/to/app.jar}} {{path/to/source_file.java}}`

- Show the flags necessary to build MPI Java applications:

`mpijavac --showme`

- Show the flags necessary to compile MPI Java applications:

`mpijavac --showme:compile`

- Show full invoked Java compiler command line:

`mpijavac {{path/to/source_file.java}} --showme`
