# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/sed.1>.

- Execute an expression:

`sed '{{s/apple/mango/g}}'`

- Execute a script:

`sed -f {{path/to/script.sed}}`

- Execute an expression with enabled [E]xtended regular expressions:

`sed -E '{{s/(apple)/\U\1/g}}'`

- Execute am expression without automatic buffer printing:

`sed -n '{{1p}}'`

- Execute an expression and replace the file with the output:

`sed -i '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace a string with the specified replacement for all lines:

`sed 's/{{regular_expression}}/{{replacement}}/g'`

- Print just the first line:

`sed -n '{{1}}p'`
