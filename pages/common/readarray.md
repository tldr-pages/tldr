# readarray

> Read lines from `stdin` into an array.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Interactively input lines into an array:

`readarray {{array_name}}`

- Read lines from a file and insert them in an array:

`readarray < {{path/to/file.txt}} {{array_name}}`

- Remove trailing deliminators (newline by default):

`readarray < {{path/to/file.txt}} -t {{array_name}}`

- Copy at most `n` lines:

`readarray < {{path/to/file.txt}} -n {{n}} {{array_name}}`

- Display help:

`help mapfile`
