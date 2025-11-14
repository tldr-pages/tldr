# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/sed.1posix>.

- Replace all `apple` (basic `regex`) occurrences with `mango` (basic `regex`) in all input lines and print the result to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Replace all occurrences of `apple` with `mango` in a specific file and save to another file:

`sed 's/apple/mango/g' {{path/to/input_file}} > {{path/to/output_file}}`

- Replace all occurrences of `apple` with `mango` in a file in-place:

`sed {{[-i|--in-place]}} 's/apple/mango/g' {{path/to/file}}`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Delete lines matching a pattern:

`sed '/{{pattern}}/d' {{path/to/file}}`

- Print just a first line to `stdout`:

`{{command}} | sed -n '1p'`

- Print lines 2 to 5 from a file:

`sed -n '2,5p' {{path/to/file}}`

- Insert a line before every line matching a pattern:

`sed '/{{pattern}}/i\{{new_line}}' {{path/to/file}}`
