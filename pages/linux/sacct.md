# sacct

> Display accounting data from the Slurm service.
> More information: <https://slurm.schedmd.com/sacct.html>.

- Display job ID, job name, partition, account, number of allocated cpus, job state, and job exit codes for recent jobs:

`sacct`

- Display job ID, job state, job exit code for recent jobs:

`sacct --brief`

- Display the allocations of a job:

`sacct --jobs {{job_id}} --allocations`

- Display elapsed time, job name, number of requested CPUs, and memory requested of a job:

`sacct --jobs {{job_id}} --format=Elapsed,JobName,ReqCPUS,ReqMem`

- Display recent jobs that occurred from one week ago up to the present day:

`sacct --starttime=$(date -d "1 week ago" +'%F')`

- Output a larger number of characters for an attribute:

`sacct --format=JobID,JobName%100`
