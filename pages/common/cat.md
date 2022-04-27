# cat

> Display and concatenate files.
> See also: `tac`.
> More information: <https://www.gnu.org/software/coreutils/cat>.

- Concatenate specific files:

`cat {{path/to/file1 path/to/file2 ...}}`

- Display `stdin`:

`{{echo 'Hello world!'}} | cat`

- Squeeze repeated empty lines:

`cat -s {{path/to/file1 path/to/file2 ...}}`

- Number all/non-[b]lank lines:

`cat -{{n|b}} {{path/to/file1 path/to/file2 ...}}`

- Display `tab` as `^I`:

`cat -T {{path/to/file1 path/to/file2 ...}}`

- Display `$` after each line:

`cat -E {{path/to/file1 path/to/file2 ...}}`

- Display non-printable characters via `^`/`M-` notation:

`cat -v {{path/to/file1 path/to/file2 ...}}`

- Display `^I`, `$` and non-printable characters:

`cat -A {{path/to/file1 path/to/file2 ...}}`
