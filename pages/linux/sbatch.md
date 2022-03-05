# sbatch

> Submit a batch job to the SLURM scheduler.
> More information: <https://manned.org/sbatch>.

- Submit a batch job:

`sbatch {{path/to/job.sh}}`

- Submit a batch job with a custom name:

`sbatch --job-name={{myjob}} {{path/to/job.sh}}`

- Submit a batch job with a time limit of 30 minutes:

`sbatch --time={{00:30:00}} {{path/to/job.sh}}`

- Submit a job and request multiple nodes:

`sbatch --nodes={{3}} {{path/to/job.sh}}`
