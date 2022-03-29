# cut

> Cut out fields from stdin or files.
> More information: <https://www.gnu.org/software/coreutils/cut>.

- Print the specified character/field range of each line (`--{{characters|fields}}={{1|1,10|1-10|1-|-10}}` is referred later as `{{range}}`):

`cut --{{characters|fields}}={{1|1,10|1-10|1-|-10}}`

- Print the range of each line with the specified delimiter:

`cut --delimiter="{{,}}" {{range}}`

- Print the range of each line of the specified file:

`cut {{range}} {{path/to/file}}`
