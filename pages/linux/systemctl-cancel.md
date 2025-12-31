# systemctl cancel

> Cancel one or more pending jobs in the system manager or user manager.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#cancel%20JOB%E2%80%A6>.

- Cancel a job by its numeric ID:

`systemctl cancel {{job_id}}`

- Cancel multiple jobs:

`systemctl cancel {{job_id1 job_id2 ...}}`

- Cancel all pending jobs:

`systemctl cancel`

- Cancel a job in the user service manager:

`systemctl cancel {{job_id}} --user`
