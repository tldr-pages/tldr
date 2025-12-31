# mpirun

> Voer seriële en parallelle taken uit in Open MPI.
> Zie ook: `mpic++`.
> Meer informatie: <https://docs.open-mpi.org/en/main/man-openmpi/man1/mpirun.1.html>.

- Voer een Open MPI programma uit:

`mpirun {{pad/naar/executable}}`

- Voer een Open MPI programma uit met `n` parallelle processen:

`mpirun -n {{n}} {{pad/naar/executable}}`

- Sta meer processen toe dan beschikbare fysieke cores:

`mpirun -oversubscribe {{pad/naar/executable}}`
