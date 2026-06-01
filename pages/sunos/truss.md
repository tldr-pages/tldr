# truss

> Troubleshooting tool for tracing system calls.
> SunOS equivalent of strace.
> More information: <https://www.unix.com/man-page/linux/1/truss>.

- Start tracing a program by executing it, following all child processes:

`truss -f {{program}}`

- Start tracing a specific process by its PID:

`truss -p {{process_id}}`

- Start tracing a program by executing it, showing arguments and environment variables:

`truss -a -e {{program}}`

- Count time, calls, and errors for each system call and report a summary on program exit:

`truss -c -p {{process_id}}`

- Trace a process filtering output by system call:

`truss -p {{process_id}} -t {{system_call_name}}`
