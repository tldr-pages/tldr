# ltrace

> Display dynamic library calls of a process.
> More information: <https://linux.die.net/man/1/ltrace>.

- Print (trace) library calls of a program binary:

`ltrace ./{{program}}`

- Count library calls. Print a handy summary at the bottom:

`ltrace -c {{path/to/program}}`

- Trace calls to malloc and free, omit those done by libc:

`ltrace -e malloc+free-@libc.so* {{path/to/program}}`

- Write to file instead of terminal:

`ltrace -o {{file}} {{path/to/program}}`
