# ifne

> Run a command depending on the emptyness of `stdin`.
> More information: <https://manned.org/ifne>.

- Run the specified command if and only if `stdin` is not empty:

`ifne {{command}} {{command_options}}`

- Run the specified command if and only if `stdin` is empty, otherwise pass `stdin` to `stdout`:

`ifne -n {{command}} {{command_options}}`
