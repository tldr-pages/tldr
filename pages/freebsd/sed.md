# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.freebsd.org/cgi/man.cgi?sed>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Delay opening each file until a command containing the related `w` function or flag is applied to a line of input:

`{{command}} | sed -fa {{path/to/script.sed}}`

- Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- Print just a first line to `stdout`:

`{{command}} | sed -n '1p'`

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a specific file and overwrite the original file in place:

`sed -i 's/apple/mango/g' {{path/to/file}}`
