# waitpid

> Wait for the termination of arbitrary processes.
> See also: `wait`.
> More information: <https://manned.org/waitpid>.

- Sleep until all processes whose PIDs have been specified have exited:

`waitpid {{process_id1 process_id2 ...}}`

- Sleep for at most `n` seconds:

`waitpid {{[-t|--timeout]}} {{n}} {{process_id1 process_id2 ...}}`

- Do not error if specified PIDs have already exited:

`waitpid {{[-e|--exited]}} {{process_id1 process_id2 ...}}`

- Sleep until `n` of the specified processes have exited:

`waitpid {{[-c|--count]}} {{n}} {{process_id1 process_id2 ...}}`

- Display help:

`waitpid {{[-h|--help]}}`
