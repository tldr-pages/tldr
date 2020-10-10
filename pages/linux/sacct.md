# sacct

> Display accounting data from the Slurm service.
> More information: <https://slurm.schedmd.com/sacct.html>.

- Check basic items such as elapsed time, job name, cpus requested, and memory requested:

`sacct -j {{job_id}} --format=elapsed,jobname,reqcpus,reqmem`

- View the allocations of a job:

`sacct -j {{job_id}} --allocations`
