# pee

> Tee `stdin` to pipes.
> See also: `tee`.
> More information: <https://manned.org/pee>.

- Run each command, providing each one with a distinct copy of `stdin`:

`pee {{command1 command2 ...}}`

- Write a copy of `stdin` to `stdout` (like `tee`):

`pee cat {{command1 command2 ...}}`

- Immediately terminate upon SIGPIPEs and write errors:

`pee --no-ignore-sigpipe --no-ignore-write-errors {{command1 command2 ...}}`
