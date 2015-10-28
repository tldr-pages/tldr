# prctl

> Get or set the resource controls of running processes,
> tasks, and projects

- examine process limits and permissions

`prctl {{PID}}`

- examine process limits and permissions in machine parseable format

`prctl -P {{PID}}`

- Get specific limit for a running process

`prctl -n process.max-file-descriptor {{PID}}`
