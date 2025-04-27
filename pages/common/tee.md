# tee

> Read from `stdin` and write to `stdout` and files (or commands).
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- Copy `stdin` to each file, and also to `stdout`:

`echo "example" | tee {{path/to/file}}`

- Append to the given files, do not overwrite:

`echo "example" | tee {{[-a|--append]}} {{path/to/file}}`

- Print `stdin` to the terminal, and also pipe it into another program for further processing:

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Create a directory called "example", count the number of characters in "example" and write "example" to the terminal:

`echo "example" | tee >(xargs mkdir) >(wc {{[-c|--bytes]}})`
