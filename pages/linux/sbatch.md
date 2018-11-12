# sbatch

> Submit a batch job to the SLURM scheduler.

- Submit a batch job by file:

`sbatch myjob.sh`

- Submit a batch job with a custom name:

`sbatch --job-name=myjob myjob.sh`

- Submit a batch job with a time limit:

`sbatch --time=00:30:00 myjob.sh`

- Submit a job and request multiple nodes:

`sbatch --nodes=3 myjob.sh`
