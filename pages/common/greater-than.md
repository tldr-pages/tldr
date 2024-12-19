# Greater than

> Redirect output to a file.
> More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Output>.

- Redirect `stdout` to a file:

`{{command}} > {{path/to/file}}`

- Append to a file:

`{{command}} >> {{path/to/file}}`

- Redirect both `stdout` and `stderr` to a file:

`{{command}} &> {{path/to/file}}`

- Redirect `stderr` to `/dev/null` to keep the terminal output clean:

`{{command}} 2> /dev/null`

- Clear the file contents or create a new empty file:

`> {{path/to/file}}`
