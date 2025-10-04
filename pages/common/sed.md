# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/sed.1posix>.

- Replace all `apple` (basic `regex`) occurrences with `mango` (basic `regex`) in all input lines and print the result to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Replace all occurrences of a string in a file and overwrite the file [i]n-place:

`sed {{[-i|--in-place]}} 's/{{find}}/{{replace}}/g' {{path/to/file}}`

- Replace only on lines matching a specific pattern:

`{{command}} | sed '/{{pattern}}/s/{{find}}/{{replace}}/g'`

- Delete lines matching a pattern:

`{{command}} | sed '/{{pattern}}/d'`

- Print lines between two patterns (inclusive):

`{{command}} | sed -n '/{{start_pattern}}/,/{{end_pattern}}/p'`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Print just a first line to `stdout`:

`{{command}} | sed -n '1p'`

- Replace only the first occurrence in each line and write the result to a different file:

`sed 's/{{find}}/{{replace}}/' {{path/to/input_file}} > {{path/to/output_file}}`
