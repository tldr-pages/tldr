# cat

> Display and concatenate files.
> See also: `tac`.
> More information: <https://www.gnu.org/software/coreutils/cat>.

- Concatenate specific files:

`cat {{path/to/file1 path/to/file2 ...}}`

- Display `stdin`:

`{{echo 'Hello world!'}} | cat`

- Squeeze repeated empty lines:

`cat --squeeze-blank {{path/to/file1 path/to/file2 ...}}`

- Number all/non-blank lines:

`cat --{{number|number-nonblank}} {{path/to/file1 path/to/file2 ...}}`

- Display `tab` as `^I`:

`cat --show-tabs {{path/to/file1 path/to/file2 ...}}`

- Display `$` after each line:

`cat --show-ends {{path/to/file1 path/to/file2 ...}}`

- Display non-printable characters via `^`/`M-` notation:

`cat --show-nonprinting {{path/to/file1 path/to/file2 ...}}`

- Display `^I`, `$` and non-printable characters:

`cat --show-all {{path/to/file1 path/to/file2 ...}}`
