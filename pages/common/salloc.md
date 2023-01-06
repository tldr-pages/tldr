# salloc

> Obtain a Slurm job allocation (a set of nodes), execute a command, and then release the allocation when the command is finished.
> More information: <https://manned.org/salloc>.

- Get an allocation and run a specific application:

`salloc --nodes={{1..infinity}} {{path/to/executable}}`

- Get an allocation and run a specific parallel application:

`salloc --nodes={{1..infinity}} srun --ntasks={{1..infinity}} {{path/to/executable}}`

- Create a heterogeneous job with several components, each allocating a unique set of nodes:

`salloc {{--nodelist=node[from1-to1] path/to/executable1 : --nodelist=node[from2-to2] path/to/executable2 ...}}`
