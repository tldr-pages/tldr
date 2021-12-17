# cut

> Cut out fields from stdin or files.
> More information: <https://manned.org/cut.1>.

- Print the specified character range of each line of stdin:

`cut --characters={{index|index1,index2,...|from-to|from-|-to}}`

- Print the specified field range of each line of stdin:

`cut --fields={{index|index1,index2,...|from-to|from-|-to}}`

- Print a given field range of each line of stdin with the specified delimiter:

`cut --delimiter={{,}} --characters={{index|index1,index2,...|from-to|from-|-to}}`

- Print a given field range of each line of the specified file:

`cut --characters={{index|index1,index2,...|from-to|from-|-to}} {{path/to/file}}`
