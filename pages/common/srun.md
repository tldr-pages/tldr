# srun

> Run a command under the Slurm workload manager.
> More information: <https://slurm.schedmd.com/srun.html>.

- Run a simple command interactively:

`srun hostname`

- Run a job with 4 CPUs:

`srun -n 4 {{path/to/program}}`

- Allocate memory for a job:
`srun --mem=8G my_program`

- Run a job on a specific partition:
`srun -p gpu my_program`

- Run a job and save output to a file:

`srun {{path/to/program}} > {{path/to/output}}`
