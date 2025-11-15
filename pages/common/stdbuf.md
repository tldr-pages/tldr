# stdbuf

> Run a command with modified buffering operations for its standard streams.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>.

- Change `stdin` buffer size to 512 KiB:

`stdbuf {{[-i|--input]}} 512K {{command}}`

- Change `stdout` buffer to line-buffered:

`stdbuf {{[-o|--output]}} L {{command}}`

- Change `stderr` buffer to unbuffered:

`stdbuf {{[-e|--error]}} 0 {{command}}`
