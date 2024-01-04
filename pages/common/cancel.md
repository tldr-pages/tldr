# cancel

> Cancel print jobs.
> See also: `lp`, `lpmove`, `lpstat`.
> More information: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- Cancel the current job of the default printer (set with `lpoptions -d {{printer}}`):

`cancel`

- Cancel the jobs of the default printer owned by a specific user:

`cancel -u {{username}}`

- Cancel the current job of a specific printer:

`cancel {{printer}}`

- Cancel a specific job from a specific printer:

`cancel {{printer}}-{{job_id}}`

- Cancel all jobs of all printers:

`cancel -a`

- Cancel all jobs of a specific printer:

`cancel -a {{printer}}`

- Cancel the current job of a specific server and then delete job data files:

`cancel -h {{server}} -x`
