# sed

> Edit text in a scriptable manner.
> See also: `awk`, `ed`.
> More information: <https://manned.org/man/freebsd-13.0/sed.1>.

- Execute commands:

`sed '{{s/apple/mango/g}}'`

- Execute a script:

`sed -f {{path/to/script.sed}}`

- Execute commands with enabled [E]xtended regular expressions:

`sed -E '{{s/(apple)/\U\1/g}}'`

- Execute commands without automatic buffer printing:

`sed -n '{{1p}}'`

- Execute commands and replace file with it's output:

`sed -i '{{s/apple/mango/g}}' {{path/to/file}}`

- Replace a string with the specified replacement for all lines:

`sed 's/{{regular_expression}}/{{replacement}}/g'`

- Print just the first line:

`sed -n '{{1}}p'`
