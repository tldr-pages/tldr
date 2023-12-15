# lprm

> Cancel queued print jobs of a server.
> See also: `lpq`.
> More information: <https://www.cups.org/doc/man-lprm.html>.

- Cancel current job on the default printer:

`lprm`

- Cancel a job of a specific server:

`lprm -h {{server[:port]}} {{job_id}}`

- Cancel multiple jobs with a [E]ncrypted connection to the server:

`lprm -E {{job_1_id}} {{job_2_id}}`

- Cancel all jobs:

`lprm -`

- Cancel the current job of a specific printer or class:

`lprm -P {{destination[/instance]}}`
