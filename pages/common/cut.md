# cut

> Cut out fields from `stdin` or files.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- Print the 5th character on each line:

`{{command}} | cut {{[-c|--characters]}} 5`

- Print the fifth to tenth character of each line of the specified file:

`cut {{[-c|--characters]}} 5-10 {{path/to/file}}`

- Split each line in a file by a delimiter into fields and print fields two and six (default delimiter is `TAB`):

`cut {{[-f|--fields]}} 2,6 {{path/to/file}}`

- Split each line by the specified delimiter and print all from the second field onward:

`{{command}} | cut {{[-d|--delimiter]}} "{{delimiter}}" {{[-f|--fields]}} 2-`

- Use space as a delimiter and print only the first 3 fields:

`{{command}} | cut {{[-d|--delimiter]}} " " {{[-f|--fields]}} -3`

- Print specific fields of lines that use `NUL` to terminate lines instead of newlines:

`{{find . -print0}} | cut {{[-z|--zero-terminated]}} {{[-d|--delimiter]}} "{{/}}" {{[-f|--fields]}} {{2}}`
