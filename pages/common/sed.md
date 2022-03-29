# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Execute the specified expression:

`{{command}} | sed '{{s/apple/mango/g}}'`

- Execute the specified script:

`{{command}} | sed --file={{path/to/script.sed}}`

- Execute the specified expression with enabled extended regular expressions:

`{{command}} | sed --regexp-extended '{{s/(apple)/\U\1/g}}'`

- Execute the specified expression without automatic buffer printing:

`{{command}} | sed --quiet '{{1p}}'`

- Execute the specified expression and replace the file with it's output:

`sed --in-place '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace the string with the specified replacement for all lines (`[s]ubstitute` command):

`{{command}} | sed 's/{{regular_expression}}/{{replacement}}/g'`

- Print just the first line (`[p]rint` command):

`{{command}} | sed --quiet '{{1}}p'`
