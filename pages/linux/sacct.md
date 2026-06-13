# sacct

> Display accounting data from the Slurm service.
> More information: <https://slurm.schedmd.com/sacct.html>.

- Display job ID, job name, partition, account, number of allocated cpus, job state, and job exit codes for recent jobs:

`sacct`

- Display job ID, job state, job exit code for recent jobs:

`sacct {{[-b|--brief]}}`

- Display the allocations of a job:

`sacct {{[-j|--jobs]}} {{job_id}} {{[-X|--allocations]}}`

- Display elapsed time, job name, number of requested CPUs, and memory requested of a job:

`sacct {{[-j|--jobs]}} {{job_id}} {{[-o|--format]}} Elapsed,JobName,ReqCPUS,ReqMem`

- Display recent jobs that occurred from one week ago up to the present day:

`sacct {{[-S|--starttime]}} $(date {{[-d|--date]}} "1 week ago" +'%F')`

- Output a larger number of characters for an attribute:

`sacct {{[-o|--format]}} JobID,JobName%100`
