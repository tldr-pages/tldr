# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a specific file and overwrite the original file in place:

`sed -i 's/apple/mango/g' {{path/to/file}}`

- Execute a specific script [f]ile and print the result to `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Print just the first line to `stdout`:

`{{command}} | sed -n '1p'`

- [d]elete the first line of a file:

`sed -i 1d {{/path/to/file}}`

- [i]nsert a new line at the first line of a file:

`sed -i '1i\your new line text\' {{/path/to/file}}`
