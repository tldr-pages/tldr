# cat

> Display and concatenate files.
> See also: `tac`.
> More information: <https://manned.org/man/freebsd-13.0/cat>.

- Concatenate specific files:

`cat {{path/to/file1 path/to/file2 ...}}`

- Display `stdin`:

`{{echo 'Hello world!'}} | cat`

- Squeeze repeated empty lines:

`cat -s {{path/to/file1 path/to/file2 ...}}`

- Number all/non-[b]lank lines:

`cat -{{n|b}} {{path/to/file1 path/to/file2 ...}}`

- Display `tab` as `^I`:

`cat -t {{path/to/file1 path/to/file2 ...}}`

- Display `$` after each line:

`cat -e {{path/to/file1 path/to/file2 ...}}`

- Display non-printable characters via `^`/`M-` notation:

`cat -v {{path/to/file1 path/to/file2 ...}}`
