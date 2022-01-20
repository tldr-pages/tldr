# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/sed.1>.

- Execute commands:

`sed '{{s/apple/mango/g}}'`

- Execute a script:

`sed --file={{path/to/script.sed}}`

- Execute commands with enabled extended regular expressions:

`sed --regexp-extended '{{s/(apple)/\U\1/g}}'`

- Execute commands without automatic buffer printing:

`sed --quiet '{{1p}}'`

- Execute commands and replace file with it's output:

`sed --in-place '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace a string with the specified replacement for all lines:

`sed 's/{{regular_expression}}/{{replacement}}/g'`

- Print just the first line:

`sed --quiet '{{1}}p'`
