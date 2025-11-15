# strace

> Troubleshooting tool for tracing system calls.
> More information: <https://manned.org/strace>.

- Start tracing a specific process by its PID:

`sudo strace {{[-p|--attach]}} {{pid}}`

- Trace a process and filter output by system call [e]xpression:

`sudo strace {{[-p|--attach]}} {{pid}} -e {{system_call,system_call2,...}}`

- Count time, calls, and errors for each system call and report a summary on program exit:

`sudo strace {{[-p|--attach]}} {{pid}} {{[-c|--summary-only]}}`

- Show the time spent in every system call and specify the maximum string size to print:

`sudo strace {{[-p|--attach]}} {{pid}} {{[-T|--syscall-times]}} {{[-s|--string-limit]}} {{32}}`

- Start tracing a program by executing it:

`strace {{program}}`

- Start tracing file operations of a program:

`strace -e trace=file {{program}}`

- Start tracing network operations of a program as well as all its forked and child processes, saving the output to a file:

`strace {{[-f|--follow-forks]}} -e trace=network {{[-o|--output]}} {{trace.txt}} {{program}}`
