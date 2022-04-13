# cut

> Cut out fields from stdin or files.
> More information: <https://www.gnu.org/software/coreutils/cut>.

- Print a specific character/field range of each line (`--{{characters|fields}}={{1|1,10|1-10|1-|-10}}` is referred later as `{{range}}`):

`{{command}} | cut --{{characters|fields}}={{1|1,10|1-10|1-|-10}}`

- Print a range of each line with a specific delimiter:

`{{command}} | cut --delimiter="{{,}}" {{range}}`

- Print a range of each line of the specific file:

`cut {{range}} {{path/to/file}}`
