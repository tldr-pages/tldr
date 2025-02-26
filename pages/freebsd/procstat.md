# procstat

> Display detailed information about processes in FreeBSD.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- Display file descriptors of a specific process:

`procstat fds {{pid}}`

- Show virtual memory mappings of a process:

`procstat vm {{pid}}`

- Display process arguments:

`procstat arguments {{pid}}`

- Show resource limits of a process:

`procstat rlimit {{pid}}`
