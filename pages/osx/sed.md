# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://keith.github.io/xcode-man-pages/sed.1.html>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- Print just a first line to `stdout`:

`{{command}} | sed -n '1p'`

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a `file` and save a backup of the original to `file.bak`:

`sed -i bak 's/apple/mango/g' {{path/to/file}}`
