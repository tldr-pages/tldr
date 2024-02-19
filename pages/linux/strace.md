# strace

> Troubleshooting tool for tracing system calls.
> More information: <https://manned.org/strace>.

- Start tracing a specific [p]rocess by its PID:

`strace -p {{pid}}`

- Trace a [p]rocess and filt[e]r output by system call:

`strace -p {{pid}} -e {{system_call,system_call2,...}}`

- Count time, calls, and errors for each system call and report a summary on program exit:

`strace -p {{pid}} -c`

- Show the [T]ime spent in every system call:

`strace -p {{pid}} -T`

- Start tracing a program by executing it:

`strace {{program}}`

- Start tracing file operations of a program:

`strace -e trace=file {{program}}`

- Start tracing network operations of a program as well as all its [f]orked and child processes, saving the [o]utput to a file:

`strace -f -e trace=network -o {{trace.txt}} {{program}}`
