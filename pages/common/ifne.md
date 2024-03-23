# ifne

> Run a command depending on the emptyness of `stdin`.
> More information: <https://joeyh.name/code/moreutils/>.

- Run the specified command if and only if `stdin` is not empty:

`ifne {{command options ...}}`

- Run the specified command if and only if `stdin` is empty, otherwise pass `stdin` to `stdout`:

`ifne -n {{command options ...}}`
