# disown

> Allow sub-processes to live beyond the shell that they are attached to.
> See also the `jobs` command.

- Disown the current job:

`disown`

- Disown a specific job:

`disown %{{job_number}}`

- Disown all jobs:

`disown -a`

- Keep job (do not disown it), but mark it so that no future SIGHUP is received on shell exit:

`disown -h %{{job_number}}`
