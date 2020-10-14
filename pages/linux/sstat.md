# sstat

> View information about running jobs.
> More information: <https://slurm.schedmd.com/sstat.html>.

- Show status information for job:

`sstat --jobs={{job_id}}`

- Show selected information with pipes as column delimiters:

`sstat --parsable --jobs={{job_id}} --format={{comma separated field list}}`

- Show list of fields available:

`sstat --helpformat`
