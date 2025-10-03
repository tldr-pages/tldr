# srun

> Run a command under the Slurm workload manager.
> More information: <https://slurm.schedmd.com/srun.html>.

- Run a simple command interactively:

`srun hostname`

- Run a job with 4 tasks (CPUs):

`srun {{[-n|--ntasks]}} 4 {{path/to/program}}`

- Allocate 8 GB of memory:

`srun --mem 8G {{path/to/program}}`

- Run a job on a specific partition:

`srun {{[-p|--partition]}} gpu {{path/to/program}}`

- Run a job and save the output to a file:

`srun {{path/to/program}} > {{path/to/output}}`
