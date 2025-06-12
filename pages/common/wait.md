# wait

> Wait for a process to complete before proceeding.
> See also: `ps` to view information about running processes.
> More information: <https://manned.org/wait>.

- Wait for a process to finish given its process ID (PID) and return its exit status:

`wait {{pid}}`

- Wait for all processes known to the invoking shell to finish:

`wait`

- Wait for a job to finish (run `jobs` to find the job number):

`wait %{{job_number}}`

- Display help:

`wait --help`
