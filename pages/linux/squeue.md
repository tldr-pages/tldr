# squeue

> View the jobs queued in the SLURM scheduler.
> More information: <https://manned.org/squeue>.

- View the queue:

`squeue`

- View jobs queued by a specific user:

`squeue -u {{username}}`

- View the queue and refresh every 5 seconds:

`squeue -i {{5}}`

- View the queue with expected start times:

`squeue --start`
