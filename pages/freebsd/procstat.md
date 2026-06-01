# procstat

> Display detailed information about processes in FreeBSD.
> More information: <https://man.freebsd.org/cgi/man.cgi?procstat>.

- Display file descriptors of a specific process:

`procstat fds {{process_id}}`

- Show virtual memory mappings of a process:

`procstat vm {{process_id}}`

- Display process arguments:

`procstat arguments {{process_id}}`

- Show resource limits of a process:

`procstat rlimit {{process_id}}`
