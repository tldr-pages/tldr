# strace 

> Troubleshooting tool for tracing system calls

- Start tracing a specific PID 

`strace -p {{pid}}`

- Trace a process and filter output by system call

`strace -e {{system call name}} -p {{pid}}`

- Start tracing and produce a summary of system calls at the end, instead of showing individual calls.

`strace -c -p {{pid}}`

