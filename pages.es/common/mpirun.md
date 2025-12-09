# mpirun

> Ejecuta trabajos en serie y en paralelo en Open MPI.
> Vea también: `mpic++`.
> Más información: <https://docs.open-mpi.org/en/main/man-openmpi/man1/mpirun.1.html>.

- Ejecuta un programa Open MPI:

`mpirun {{ruta/al/ejecutable}}`

- Ejecuta un programa Open MPI con `n` procesos paralelos:

`mpirun -n {{n}} {{ruta/al/ejecutable}}`

- Permite más procesos que núcleos físicos disponibles:

`mpirun -oversubscribe {{ruta/al/ejecutable}}`
