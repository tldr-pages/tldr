# cut

> Cut out fields from stdin or files.
> More information: <https://www.gnu.org/software/coreutils/cut>.

- Print a specific character/field range of each line:

`{{command}} | cut --{{characters|fields}}={{1|1,10|1-10|1-|-10}}`

- Print a range of each line with a specific delimiter:

`{{command}} | cut --delimiter="{{,}}" --{{characters}}={{1}}`

- Print a range of each line of the specific file:

`cut --{{characters}}={{1}} {{path/to/file}}`
