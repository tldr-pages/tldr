# scontrol

> View information about running jobs.
> More information: <https://slurm.schedmd.com/scontrol.html>.

- Show information for job:

`scontrol show job {{job_id}}`

- Suspend a running job:

`scontrol suspend {{job_id}}`

- Resume a suspended job:

`scontrol resume {{job_id}}`

- Hold a queued job (gives it least priority):

`scontrol hold {{job_id}}`

- Release a held job:

`scontrol release  {{job_id}}`
