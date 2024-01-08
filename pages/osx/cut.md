# cut

> Cut out fields from `stdin` or files.
> More information: <https://manned.org/man/freebsd-13.0/cut.1>.

- Print a specific character/field range of each line:

`{{command}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Print a field range of each line with a specific delimiter:

`{{command}} | cut -d "{{,}}" -f {{1}}`

- Print a character range of each line of a specific file:

`cut -c {{1}} {{path/to/file}}`
