# csplit

> Split a file into pieces.
> This generates files named "xx00", "xx01", and so on.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html>.

- Split a file in two parts, starting the second one at line 10:

`csplit {{path/to/file}} 10`

- Split a file in three parts, starting the latter parts in lines 7 and 23:

`csplit {{path/to/file}} 7 23`

- Start a new part at every 5th line (will fail if number of lines is not divisible by 5):

`csplit {{path/to/file}} 5 {*}`

- Start a new part at every 5th line, ignoring exact-division error:

`csplit {{[-k|--keep-files]}} {{path/to/file}} 5 {*}`

- Split a file above line 5 and use a custom prefix for the output files (default is `xx`):

`csplit {{path/to/file}} 5 {{[-f|--prefix]}} {{prefix}}`

- Split a file above the first line matching a `regex` pattern:

`csplit {{path/to/file}} /{{regex}}/`
