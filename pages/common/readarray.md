# readarray

> Read lines from `stdin` into an array.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Interactively input lines into an array:

`readarray {{array_name}}`

- Read lines from a file and insert them in an array:

`readarray {{array_name}} < {{path/to/file.txt}}`

- Remove trailing deliminators (newline by default):

`readarray -t {{array_name}} < {{path/to/file.txt}}`

- Copy at most `n` lines:

`readarray -n {{n}} {{array_name}} < {{path/to/file.txt}}`

- Display help:

`help mapfile`
