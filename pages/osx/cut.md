# cut

> Cut out fields from stdin or files.
> There are no options to get help or version.
> More information: <https://manned.org/man/freebsd-13.0/cut.1>.

- Print the specified [c]haracter/[c]haracters/[c]haracter range of each line:

`cut -c {{1|1,10|1-10|1-|-10}}`

- Print the specified [f]ield/[f]ields/[f]ield range of each line:

`cut -f {{1|1,10|1-10|1-|-10}}`

- Print a field/fields/field range of each line with the specified [d]elimiter:

`cut -d "{{,}}" --fields={{1|1,10|1-10|1-|-10}}`

- Print a [f]ield/[f]ields/[f]ield range of each line of the specified file:

`cut -f {{1|1,10|1-10|1-|-10}} {{path/to/file}}`
