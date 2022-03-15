# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Execute an expression:

`sed '{{s/apple/mango/g}}'`

- Execute a script:

`sed --file={{path/to/script.sed}}`

- Execute an expression with enabled extended regular expressions:

`sed --regexp-extended '{{s/(apple)/\U\1/g}}'`

- Execute an expression without automatic buffer printing:

`sed --quiet '{{1p}}'`

- Execute an expression and replace a file with it's output:

`sed --in-place '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace a string with the specified replacement for all lines:

`sed 's/{{regular_expression}}/{{replacement}}/g'`

- Print just the first line:

`sed --quiet '{{1}}p'`
