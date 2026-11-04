# dtruss

> Trace system calls and kernel activities on `osx` using DTrace.
> Note: Requires System Integrity Protection to be disabled.
> See also: `strace`.
> More information: <https://keith.github.io/xcode-man-pages/dtruss.1m.html>.

- Trace a running process by PID:

`sudo dtruss -p {{process_id}}`

- Run a program and trace it:

`sudo dtruss {{program}}`

- [W]ait for a process with a matching name and trace it:

`sudo dtruss -W {{name}}`

- Print [e]lapsed time, [o]n-cpu time, and [c]ount of each system call:

`sudo dtruss -eoc -p {{process_id}}`

- Trace a process and [f]ollow children:

`sudo dtruss -f -p {{process_id}}`

- Print occurrences of a specific system call:

`sudo dtruss -t {{syscall}} -p {{process_id}}`
