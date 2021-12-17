# cut

> Cut out fields from stdin or files.
> More information: <https://manned.org/cut.1>.

- Print the specified character/characters/character range of each line:

`cut --characters={{1|1,10|1-10|1-|-10}}`

- Print the specified field/fields/field range of each line:

`cut --fields={{1|1,10|1-10|1-|-10}}`

- Print a field/fields/field range of each line with the specified delimiter:

`cut --delimiter={{,}} --fields={{1|1,10|1-10|1-|-10}}`

- Print a field/fields/field range of each line of the specified file:

`cut --fields={{1|1,10|1-10|1-|-10}} {{path/to/file}}`

- Print the version:

`cut --version`
