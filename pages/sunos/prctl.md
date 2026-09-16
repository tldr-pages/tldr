# prctl

> Get or set the resource controls of running processes, tasks, and projects.
> More information: <https://www.unix.com/man-page/sunos/1/prctl>.

- Examine process limits and permissions:

`prctl {{process_id}}`

- Examine process limits and permissions in machine parsable format:

`prctl -P {{process_id}}`

- Get specific limit for a running process:

`prctl -n process.max-file-descriptor {{process_id}}`
