# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Execute a specific expression:

`{{command}} | sed '{{s/apple/mango/g}}'`

- Execute a specific script:

`{{command}} | sed --file={{path/to/script.sed}}`

- Execute a specific expression with enabled extended regular expressions:

`{{command}} | sed --regexp-extended '{{s/(apple)/\U\1/g}}'`

- Execute a specific expression without automatic buffer printing (print just the first line (`[p]rint` command)):

`{{command}} | sed --quiet '{{1p}}'`

- Execute a specific expression and replace the file with it's output:

`sed --in-place '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace the string with a specific replacement for all lines (`[s]ubstitute` command):

`{{command}} | sed 's/{{regular_expression}}/{{replacement}}/g'`
