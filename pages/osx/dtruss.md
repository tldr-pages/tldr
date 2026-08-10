# dtruss

> Troubleshooting tool for tracing system calls using DTrace.
> MacOS analog to `strace`.
> Note: requires System Integrity Protection to be disabled.
> More information: <https://manned.org/dtruss>.

- Trace a running process by PID:

`sudo dtruss -p {{pid}}`

- Run a program and trace it:

`sudo dtruss {{program}}`

- [W]ait for a process with a matching name and trace it:

`sudo dtruss -W {{name}}`

- Print [e]lapsed time, [o]n-cpu time, and [c]ount of each system call:

`sudo dtruss -eoc -p {{pid}}`

- Trace a process and [f]ollow children:

`sudo dtruss -f -p {{pid}}`

- Only print occurrences of a single system call:

`sudo dtruss -t {{syscall}} -p {{pid}}`
