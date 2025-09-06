# mpirun

> Execute serial and parallel jobs in Open MPI.
> See also: `mpic++`.
> More information: <https://docs.open-mpi.org/en/main/man-openmpi/man1/mpirun.1.html>.

- Execute an Open MPI program:

`mpirun {{path/to/executable}}`

- Execute an Open MPI program with `n` parallel processes:

`mpirun -n {{n}} {{path/to/executable}}`

- Allow more processes than available physical cores:

`mpirun -oversubscribe {{path/to/executable}}`
