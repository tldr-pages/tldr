# procstat

> Display detailed information about processes in FreeBSD.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- Display file descriptors of a specific process:

`procstat -f {{pid}}`

- Show virtual memory mappings of a process:

`procstat -v {{pid}}`

- Display process arguments:

`procstat -c {{pid}}`

- Show resource limits of a process:

`procstat -r {{pid}}`
