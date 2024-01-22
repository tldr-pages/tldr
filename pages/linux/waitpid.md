# waitpid

> Wait for the termination of arbitrary processes.
> See also: `wait`.
> More information: <https://manned.org/waitpid.1>.

- Sleep until all processes whose PIDs have been specified have exited:

`waitpid {{pid1 pid2 ...}}`

- Sleep for at most `n` seconds:

`waitpid --timeout {{n}} {{pid1 pid2 ...}}`

- Do not error if specified PIDs have already exited:

`waitpid --exited {{pid1 pid2 ...}}`

- Sleep until `n` of the specified processes have exited:

`waitpid --count {{n}} {{pid1 pid2 ...}}`

- Display help:

`waitpid -h`
