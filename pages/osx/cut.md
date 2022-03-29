# cut

> Cut out fields from stdin or files.
> More information: <https://manned.org/man/freebsd-13.0/cut.1>.

- Print the specified character/field range of each line (`-{{c|f}} {{1|1,10|1-10|1-|-10}}` is referred later as `{{range}}`):

`cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Print the range of each line with the specified delimiter:

`cut -d "{{,}}" {{range}}`

- Print the range of each line of the specified file:

`cut {{range}} {{path/to/file}}`
