# cut

> Cut out fields from `stdin` or files.
> More information: <https://www.gnu.org/software/coreutils/cut>.

- Print a specific [c]haracter/[f]ield range of each line:

`{{command}} | cut --{{characters|fields}} {{1|1,10|1-10|1-|-10}}`

- Print a [f]ield range of each line with a specific [d]elimiter:

`{{command}} | cut --delimiter "{{,}}" --fields {{1}}`

- Print a [c]haracter range of each line of the specific file:

`cut --characters {{1}} {{path/to/file}}`

- Print specific [f]ields of `NUL` terminated lines (e.g. as in `find . -print0`) instead of newlines:

`{{command}} | cut --zero-terminated --fields {{1}}`
