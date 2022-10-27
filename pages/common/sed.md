# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Replace all `apple` occurences with `mango` in all input lines and print the result to `stdout`:

`{{command}} | sed '{{s/apple/mango/g}}'`

- Execute a specific script and print the result to `stdout`:

`{{command}} | sed --file={{path/to/script.sed}}`

- Replace all `apple` occurences with `APPLE` in all input lines and print the result to `stdout`:

`{{command}} | sed --regexp-extended '{{s/(apple)/\U\1/g}}'`

- Print just a first line to `stdout`:

`{{command}} | sed --quiet '{{1p}}'`

- Replace all `apple` occurences with `mango` in all input lines and save modifications to a specific file:

`sed --in-place '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace a string with a specific replacement for all lines (`[s]ubstitute` command):

`{{command}} | sed 's/{{regular_expression}}/{{replacement}}/g'`
