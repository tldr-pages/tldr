# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Execute the specified expression:

`sed '{{s/apple/mango/g}}'`

- Execute the specified script:

`sed --file={{path/to/script.sed}}`

- Execute the specified expression with enabled extended regular expressions:

`sed --regexp-extended '{{s/(apple)/\U\1/g}}'`

- Execute the specified expression without automatic buffer printing:

`sed --quiet '{{1p}}'`

- Execute the specified expression and replace the file with it's output:

`sed --in-place '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace the specified string with the specified replacement for all lines (`[s]ubstitute` command):

`sed 's/{{regular_expression}}/{{replacement}}/g'`

- Print just the first line (`[p]rint` command):

`sed --quiet '{{1}}p'`
