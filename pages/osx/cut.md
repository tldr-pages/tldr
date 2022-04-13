# cut

> Cut out fields from stdin or files.
> More information: <https://manned.org/man/freebsd-13.0/cut.1>.

- Print a specific character/field range of each line (`-{{c|f}} {{1|1,10|1-10|1-|-10}}` is referred later as `{{range}}`):

`{{command}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Print a range of each line with a specific delimiter:

`{{command}} | cut -d "{{,}}" {{range}}`

- Print a range of each line of a specific file:

`cut {{range}} {{path/to/file}}`
