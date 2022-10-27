# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Replace all `apple` occurrences with `mango` in all input lines and print the result to `stdout`:

`{{command}} | sed '{{s/apple/mango/g}}'`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Replace all `apple` occurrences with `APPLE` in all input lines and print the result to `stdout`:

`{{command}} | sed -E '{{s/(apple)/\U\1/g}}'`

- Print just a first line to `stdout`:

`{{command}} | sed -n '{{1p}}'`

- Replace all `apple` occurrences with `mango` in all input lines and save modifications to a specific file:

`sed -i '{{s/apple/mango/g}}' {{path/to/file}}`
