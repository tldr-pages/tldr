# gops

> List and diagnose Go processes currently running on your system.
> More information: <https://github.com/google/gops>.

- Print all go processes running locally:

`gops`

- Print more information about a process:

`gops {{pid}}`

- Display a process tree:

`gops tree`

- Print the current stack trace from a target program:

`gops stack {{pid|addr}}`

- Print the current runtime memory statistics:

`gops memstats {{pid|addr}}`
