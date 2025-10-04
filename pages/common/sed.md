# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/sed.1posix>.

- Replace all `apple` (basic `regex`) occurrences with `mango` (basic `regex`) in all input lines and print the result to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Replace only the first occurrence of `apple` in each line:

`{{command}} | sed 's/apple/mango/'`

- Replace only on lines matching a specific pattern:

`{{command}} | sed '/{{pattern}}/s/{{find}}/{{replace}}/g'`

- Delete lines matching a pattern:

`{{command}} | sed '/{{pattern}}/d'`

- Print lines between two patterns (inclusive):

`{{command}} | sed -n '/{{start_pattern}}/,/{{end_pattern}}/p'`

- Execute a specific script file and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Print just a first line to `stdout`:

`{{command}} | sed -n '1p'`

- Apply multiple substitution expressions:

`{{command}} | sed -e 's/{{find1}}/{{replace1}}/g' -e 's/{{find2}}/{{replace2}}/g'`
