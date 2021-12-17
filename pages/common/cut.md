# cut

> Cut out fields from stdin or files.
> More information: <https://manned.org/cut.1>.

- Print the specified character range of each line of stdin:

`cut --characters={{1|1,10|1-10|1-|-10}}`

- Print the specified field range of each line of stdin:

`cut --fields={{1|1,10|1-10|1-|-10}}`

- Print a given field range of each line of stdin with the specified delimiter:

`cut --delimiter={{,}} --characters={{1|1,10|1-10|1-|-10}}`

- Print a given field range of each line of the specified file:

`cut --characters={{1|1,10|1-10|1-|-10}} {{path/to/file}}`
